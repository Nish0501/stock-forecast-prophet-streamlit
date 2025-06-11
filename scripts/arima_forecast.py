import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
import warnings
warnings.filterwarnings("ignore")

# Step 1: Load cleaned data
df = pd.read_csv("TCS_stock_data_cleaned.csv", parse_dates=['Date'], index_col='Date')

# Step 2: Use only the closing price
close_series = df['Close_TCS.NS']

# Step 3: Split data into train and test (80% train, 20% test)
train_size = int(len(close_series) * 0.8)
train, test = close_series[:train_size], close_series[train_size:]

# Step 4: Fit ARIMA model (basic version)
model = ARIMA(train, order=(5, 1, 0))  # (p,d,q)
model_fit = model.fit()

# Step 5: Forecast for the length of test set
forecast = model_fit.forecast(steps=len(test))

# Step 6: Plot actual vs predicted
plt.figure(figsize=(12, 6))
plt.plot(train.index, train, label='Train Data')
plt.plot(test.index, test, label='Actual Test Data', color='blue')
plt.plot(test.index, forecast, label='Forecasted Data', color='red')
plt.title("ARIMA Model Forecast vs Actual")
plt.xlabel("Date")
plt.ylabel("Close Price")
plt.legend()
plt.tight_layout()
plt.show()
