import pandas as pd
import os

stocks = ["TCS", "INFY", "RELIANCE", "HDFCBANK"]

for stock in stocks:
    try:
        # Load raw CSV
        df_raw = pd.read_csv(f"{stock}_stock_data.csv", header=[0, 1])
        df_raw.columns = [f"{col[0]}_{col[1]}" for col in df_raw.columns]

        # Load 'Date' column separately
        df_date = pd.read_csv(f"{stock}_stock_data.csv", skiprows=[1], usecols=['Date'])
        df_date['Date'] = pd.to_datetime(df_date['Date'], dayfirst=True)

        # Merge and clean
        df_raw['Date'] = df_date['Date']
        df_raw.set_index('Date', inplace=True)
        df_clean = df_raw.dropna()
        df_clean = df_clean[~df_clean.index.duplicated()]

        # Save to data folder
        os.makedirs("data", exist_ok=True)
        df_clean.to_csv(f"data/{stock}_stock_data_cleaned.csv")
        print(f"Cleaned: data/{stock}_stock_data_cleaned.csv")

    except FileNotFoundError:
        print(f"File not found: {stock}_stock_data.csv. Skipping...")
