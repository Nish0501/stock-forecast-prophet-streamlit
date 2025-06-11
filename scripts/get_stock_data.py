import yfinance as yf
import pandas as pd

# List of stocks and their ticker symbols
stocks = {
    "TCS": "TCS.NS",
    "INFY": "INFY.NS",
    "RELIANCE": "RELIANCE.NS",
    "HDFCBANK": "HDFCBANK.NS"
}

# Date range for data collection
start_date = "2020-01-01"
end_date = "2024-12-31"

# Download and save CSV for each stock
for name, symbol in stocks.items():
    print(f"Downloading data for {name} ({symbol})...")
    df = yf.download(symbol, start=start_date, end=end_date, auto_adjust=True)
    
    if not df.empty:
        df.to_csv(f"{name}_stock_data.csv")
        print(f"Saved: {name}_stock_data.csv")
    else:
        print(f"No data for {name}. Skipping...")
