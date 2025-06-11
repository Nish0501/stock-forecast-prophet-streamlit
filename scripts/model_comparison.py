import pandas as pd
from sklearn.metrics import mean_squared_error
from math import sqrt
from statsmodels.tsa.arima.model import ARIMA
from prophet import Prophet

# Step 1: Load data
df = pd.read_csv("TCS_stock_data_cleaned.csv", parse_dates=['Date'])
df.set_index('Date', inplace=True)
close_series = df['Close_TCS.NS']

# Step 2: Split into train/test
train_size = int(len(close_series) * 0.8)
train, test = close_series[:train_size], close_series[train_size:]

# -------- ARIMA --------
model_arima = ARIMA(train, order=(5, 1, 0))
arima_fit = model_arima.fit()
forecast_arima = arima_fit.forecast(steps=len(test))

# Calculate RMSE for ARIMA
rmse_arima = sqrt(mean_squared_error(test, forecast_arima))
print(f"ARIMA RMSE: {rmse_arima:.2f}")

# -------- Prophet --------
# Step 3: Prepare for Prophet
prophet_df = df[['Close_TCS.NS']].reset_index().rename(columns={'Date': 'ds', 'Close_TCS.NS': 'y'})
prophet_train = prophet_df.iloc[:train_size]

# Step 4: Train and forecast with Prophet
model_prophet = Prophet()
model_prophet.fit(prophet_train)

# Create future dates for test period
future = model_prophet.make_future_dataframe(periods=len(test))
forecast = model_prophet.predict(future)

# Extract forecasted y values
forecast_prophet = forecast['yhat'].iloc[-len(test):].values

# Calculate RMSE for Prophet
rmse_prophet = sqrt(mean_squared_error(test, forecast_prophet))
print(f" Prophet RMSE: {rmse_prophet:.2f}")

# Final comparison
print("\nBetter model:", "ARIMA" if rmse_arima < rmse_prophet else "Prophet")
