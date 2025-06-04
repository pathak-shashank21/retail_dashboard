# Retail Dashboard

A complete business intelligence and data science solution for retail analytics, combining Power BI dashboards with Python-based data processing and forecasting. This project simulates a real-world retail environment using historical sales and store data from the Rossmann dataset.

---

## 📁 Project Structure

```
retail_dashboard/
├── data/
│   ├── raw/                  # Original Kaggle files (store.csv, train.csv, test.csv)
│   └── processed/            # Cleaned and compressed data
│       ├── cleaned_store.csv
│       ├── cleaned_train.csv.gz
│       └── rossmann_features.csv.gz
├── scripts/
│   ├── data_cleaner.py       # Cleans raw sales/store data
│   └── feature_engineering.py # Adds derived features and flags
├── powerbi/
│   ├── retail_dashboard.pbix # Power BI report file
│   ├── dashboard_1.png       # Executive summary screenshot
│   ├── dashboard_2.png       # Product performance screenshot
│   └── dashboard_3.png       # Regional breakdown screenshot
├── pitch_deck.pptx           # Executive slide deck (3-slide summary)
├── kaggle.json               # API key for automated data pull (optional)
└── README.md
```

---

## 🔑 Key Features

- Built a multi-page Power BI dashboard with KPI cards, trend lines, maps, and product breakdowns.
- Cleaned and standardized raw sales/store data using Python.
- Engineered profit margins, holiday/promo flags, seasonality, and weekday patterns.
- Forecasted next 3 months of sales using Prophet, imported predictions into Power BI.
- Flagged anomalies using 7-day rolling dips (>40%) to detect risks.
- Performed statistical tests (p-values, t-tests, chi-square) to assess promo impact.

---

## ▶️ How to Run

1. **Raw Data**  
   Place `store.csv`, `train.csv`, and `test.csv` in `data/raw/`.

2. **Run Processing Scripts**
   ```
   python scripts/data_cleaner.py
   python scripts/feature_engineering.py
   ```

3. **Open Power BI**
   - Open `powerbi/retail_dashboard.pbix`
   - Click **Refresh**
   - Explore the dashboard pages

---

## 📊 Dashboard Pages

- **Page 1: Executive Summary**  
  KPIs, trendlines, region-level overview

- **Page 2: Product Performance**  
  Top products, categories, sales-profit matrix

- **Page 3: Regional Breakdown**  
  Map view by city/state, orders and returns

- **Page 4: Inventory + Forecast** *(optional)*  
  Forecasted trends, low-stock flags

---

## 🛠️ Tools Used

- **Power BI Desktop** – DAX, dashboards, slicers
- **Python** – Pandas, Prophet, matplotlib
- **Data Modeling** – Star schema with fact/dimension tables
- **Statistical Analysis** – t-tests, chi-square, regression
- **Version Control** – Git + GitHub

---

## 📥 Download

To get the full project as a ZIP:
- Go to [Releases](https://github.com/pathak-shashank21/retail_dashboard/releases)
- Download `retail_dashboard.zip`
