Retail_dashboard

A complete business intelligence and data science solution for retail analytics, combining Power BI dashboards with Python-based data processing and forecasting. The project simulates a real-world retail environment using historical sales and store data from the Rossmann dataset.

Project Overview
This project showcases an end-to-end analytics pipeline for retail performance monitoring. It integrates data cleaning, feature engineering, forecasting, and BI dashboarding to support decision-making at both executive and operational levels.

Directory Structure


retail_dashboard/
├── data/
│   ├── raw/                          # Kaggle Rossmann Original data
│   │   ├── store.csv
│   │   ├── test.csv
│   │   └── train.csv
│   └── processed/                    # Cleaned and engineered datasets
│       ├── cleaned_store.csv
│       ├── cleaned_train.csv
│       └── rossmann_features.csv
├── kaggle.json                       # Kaggle API token for automated download
├── pitch_deck.pptx                   # Executive summary presentation
├── powerbi/
│   ├── dashboard_1.png               # Power BI page screenshots
│   ├── dashboard_2.png
│   ├── dashboard_3.png
│   └── retail_dashboard.pbix         # Main Power BI dashboard file
├── scripts/
│   ├── data_cleaner.py               # Cleans raw CSVs and standardizes formats
│   └── feature_engineering.py        # Adds derived columns and analytical flags
├── README.md


Key Features
Built a multi-page Power BI dashboard with KPI cards, trend lines, maps, and product breakdowns.

Cleaned and standardized raw sales and store data using Python.

Engineered features such as profit margin, holiday/promo flags, seasonality, and weekday effects.

Integrated Prophet model to forecast 3-month sales, imported into Power BI for visual comparison.

Detected anomalies via 7-day rolling sales dips (>40%) to flag risk zones and stock issues.

Performed regression analysis (linear, logistic) with p-values and t-tests to assess promotion impact.

How to Run
Place raw data in data/raw/

Run scripts/data_cleaner.py to clean store and train data.

Run scripts/feature_engineering.py to generate rossmann_features.csv

Open powerbi/retail_dashboard.pbix in Power BI Desktop and refresh the data.

Use filters, slicers, and visuals to explore insights across KPIs, regions, products, and forecasted trends.

Tools Used
Power BI Desktop – Dashboard design and DAX-based metrics

Python (Pandas, Prophet, NumPy) – Data cleaning and forecasting

Statistical Analysis – t-tests, chi-square, regression for causal inference

Star Schema Modeling – Fact and dimension table structure

Business Applications
This project simulates a scalable retail analytics system suitable for:

Sales monitoring and trend forecasting

Regional and product performance tracking

Inventory planning and risk detection

Promo impact analysis and planning optimization

