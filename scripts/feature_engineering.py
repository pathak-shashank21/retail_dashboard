import os
import pandas as pd
import numpy as np

# === Paths ===
PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
PROCESSED_DIR = os.path.join(PROJECT_ROOT, "data", "processed")
train_path = os.path.join(PROCESSED_DIR, "cleaned_train.csv")
store_path = os.path.join(PROCESSED_DIR, "cleaned_store.csv")
output_path = os.path.join(PROCESSED_DIR, "rossmann_features.csv")

# === Load Data ===
train_df = pd.read_csv(train_path, parse_dates=["date"])
store_df = pd.read_csv(store_path)
df = train_df.merge(store_df, on="store", how="left")

# === Dates ===
df["year"] = df["date"].dt.year
df["month"] = df["date"].dt.month
df["day"] = df["date"].dt.day
df["weekday"] = df["date"].dt.weekday
df["weekofyear"] = df["date"].dt.isocalendar().week
df["quarter"] = df["date"].dt.quarter
df["isweekend"] = df["weekday"].isin([5, 6])
df["ismonthstart"] = df["date"].dt.is_month_start
df["ismonthend"] = df["date"].dt.is_month_end
df["monthname"] = df["date"].dt.month_name()
df["dayofweekname"] = df["date"].dt.day_name()

# === Composite flags ===
season_map = {12: "Winter", 1: "Winter", 2: "Winter",
              3: "Spring", 4: "Spring", 5: "Spring",
              6: "Summer", 7: "Summer", 8: "Summer",
              9: "Autumn", 10: "Autumn", 11: "Autumn"}
df["season"] = df["month"].map(season_map)

df["storetype_assortment"] = df["storetype"] + "_" + df["assortment"]
df["storetype_enc"] = df["storetype"].map({'a': 3, 'b': 2, 'c': 1, 'd': 0})
df["assortment_enc"] = df["assortment"].map({'a': 1, 'b': 2, 'c': 3})

# === Promo2 Flag ===
def is_promo2_running(row):
    if row["promo2"] != 1 or pd.isna(row["promointerval"]):
        return False
    return row["date"].month_name() in row["promointerval"].split(',')

df["ispromo2active"] = df.apply(is_promo2_running, axis=1)

# === Competition time-based ===
df["competitionopen"] = pd.to_datetime(
    dict(year=df["competitionopensinceyear"], month=df["competitionopensincemonth"], day=1),
    errors="coerce"
)
df["competitionagedays"] = (df["date"] - df["competitionopen"]).dt.days.clip(lower=0).fillna(0).astype(int)

# === Log Sales and Derived Logic ===
df["logsales"] = np.log1p(df["sales"])
df["isnosales"] = df["sales"] <= 0
df["salesbin"] = pd.qcut(df["sales"], q=5, labels=["verylow", "low", "medium", "high", "veryhigh"])

# === Per-customer Sales ===
if "customers" in df.columns:
    df["salespercustomer"] = df["sales"] / df["customers"]
    df["salespercustomer"] = df["salespercustomer"].replace([np.inf, -np.inf], 0).fillna(0)
else:
    df["salespercustomer"] = 0

# === Profit Logic ===
if "profit" not in df.columns:
    df["profit"] = df["sales"] * 0.1
df["profitmargin"] = df["profit"] / df["sales"]
df["profitmargin"] = df["profitmargin"].replace([np.inf, -np.inf], 0).fillna(0)
df["isloss"] = df["profit"] < 0

# === Smart Business Flags ===
df["ispromoactive"] = df["promo"].astype(bool) if "promo" in df.columns else False
df["hascompetition"] = df["competitiondistance"] < 2000
df["hascompetition"] = df["hascompetition"].fillna(False)

df["needsboost"] = (df["salespercustomer"] < df["salespercustomer"].mean()) & ~df["ispromoactive"]
df["riskflag"] = (df["profitmargin"] < 0.05) & (df["sales"] < df["sales"].mean())

# === Store-level Aggregates ===
store_grp = df.groupby("store").agg(
    avg_store_sales=("sales", "mean"),
    avg_store_customers=("customers", "mean"),
    avg_store_profit=("profit", "mean"),
)
df = df.merge(store_grp, on="store", how="left")
df["sales_deviation"] = df["sales"] - df["avg_store_sales"]
df["profit_deviation"] = df["profit"] - df["avg_store_profit"]

# === Lag & Rolling Features ===
df = df.sort_values(by=["store", "date"])
df["sales_lag1"] = df.groupby("store")["sales"].shift(1)
df["sales_pct_change"] = df.groupby("store")["sales"].pct_change().fillna(0)
df["sales_rolling7"] = df.groupby("store")["sales"].transform(lambda x: x.rolling(7, min_periods=1).mean())

# === Final Output ===
df.to_csv(output_path, index=False)
print(f"✅ Feature dataset saved to: {output_path}")
