import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load CSV with two header rows
df_raw = pd.read_csv("TCS_stock_data.csv", header=[0, 1])

# Step 2: Flatten column names → 'Close_TCS.NS', etc.
df_raw.columns = [f"{col[0]}_{col[1]}" for col in df_raw.columns]

# Step 3: Load 'Date' column safely (skip 2nd header row)
df_date = pd.read_csv("TCS_stock_data.csv", skiprows=[1], usecols=['Date'])
df_date['Date'] = pd.to_datetime(df_date['Date'], dayfirst=True)

# Step 4: Add Date to DataFrame and set as index
df_raw['Date'] = df_date['Date']
df_raw.set_index('Date', inplace=True)

# Step 5: Plot correct column
sns.set_style("whitegrid")
plt.figure(figsize=(12, 6))
plt.plot(df_raw['Close_TCS.NS'], label='Close Price', color='blue')
plt.title("TCS Stock Closing Price Over Time")
plt.xlabel("Date")
plt.ylabel("Price (INR)")
plt.legend()
plt.tight_layout()
plt.show()
