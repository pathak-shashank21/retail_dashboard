import os
import pandas as pd

def load_and_clean_csv(path):
    # Load with relaxed memory parsing
    df = pd.read_csv(path, low_memory=False)

    # Normalize column names
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "").str.replace("-", "").str.replace("_", "")

    # Auto-handle common nulls
    for col in df.columns:
        if df[col].isnull().sum() > 0:
            if df[col].dtype == "object":
                df[col] = df[col].fillna("None")
            elif df[col].dtype in ["int64", "float64"]:
                df[col] = df[col].fillna(df[col].median())
    
    return df

def save_df(df, output_path):
    df.to_csv(output_path, index=False)
    print(f"✅ Saved: {output_path}")

if __name__ == "__main__":
    PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
    RAW_DIR = os.path.join(PROJECT_ROOT, "data", "raw")
    PROCESSED_DIR = os.path.join(PROJECT_ROOT, "data", "processed")

    files_to_clean = ["train.csv", "store.csv"]  # easily expandable

    for filename in files_to_clean:
        input_path = os.path.join(RAW_DIR, filename)
        output_path = os.path.join(PROCESSED_DIR, f"cleaned_{filename}")
        df = load_and_clean_csv(input_path)
        save_df(df, output_path)
