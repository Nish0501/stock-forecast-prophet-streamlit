import pandas as pd
from prophet import Prophet
import streamlit as st
import matplotlib.pyplot as plt
import os

# Streamlit page config
st.set_page_config(page_title="Stock Forecast App", layout="wide")

# Title
st.title("Multi-Stock Forecasting App using Facebook Prophet")
st.markdown("Forecast closing prices for top Indian stocks using time series analysis.")

#  Dropdown to choose stock
stock_options = {
    "TCS": "TCS_stock_data_cleaned.csv",
    "INFY": "INFY_stock_data_cleaned.csv",
    "RELIANCE": "RELIANCE_stock_data_cleaned.csv",
    "HDFCBANK": "HDFCBANK_stock_data_cleaned.csv"
}

stock_choice = st.sidebar.selectbox("Choose a stock:", list(stock_options.keys()))
n_days = st.sidebar.slider("Forecast days:", 7, 60, 30)

# Load cleaned data
data_path = f"data/{stock_options[stock_choice]}"
df = pd.read_csv(data_path, parse_dates=['Date'])

#  Rename for Prophet
df = df.rename(columns={'Date': 'ds', f'Close_{stock_choice}.NS': 'y'})

#  Train Prophet model
model = Prophet()
model.fit(df)

# Make future predictions
future = model.make_future_dataframe(periods=n_days)
forecast = model.predict(future)

# Plot forecast
st.subheader(f"Forecast for {stock_choice} - Next {n_days} Days")
fig1 = model.plot(forecast)
st.pyplot(fig1)

# Trend and seasonality components
st.subheader("Forecast Components")
fig2 = model.plot_components(forecast)
st.pyplot(fig2)
