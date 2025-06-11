import pandas as pd
import matplotlib.pyplot as plt
from prophet import Prophet

# Step 1: Load the cleaned data
df = pd.read_csv("TCS_stock_data_cleaned.csv", parse_dates=['Date'])

# Step 2: Prepare the data for Prophet
prophet_df = df[['Date', 'Close_TCS.NS']].rename(columns={'Date': 'ds', 'Close_TCS.NS': 'y'})

# Step 3: Initialize and fit the model
model = Prophet()
model.fit(prophet_df)

# Step 4: Create future dates
future = model.make_future_dataframe(periods=30)  # Predict 30 days ahead

# Step 5: Make forecast
forecast = model.predict(future)

# Step 6: Plot the forecast
fig = model.plot(forecast)
plt.title("TCS Stock Forecast with Prophet")
plt.xlabel("Date")
plt.ylabel("Close Price (INR)")
plt.tight_layout()
plt.show()

# Optional: Plot trend/seasonality
model.plot_components(forecast)
plt.tight_layout()
plt.show()
