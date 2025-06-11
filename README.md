# Stock Market Forecasting App (TCS, INFY, RELIANCE, HDFCBANK)

This is a complete end-to-end stock forecasting project using time series models and real stock market data from Yahoo Finance. The project supports forecasting for multiple Indian stocks and presents the results through an interactive Streamlit dashboard.

---

## 🚀 What This Project Covers

- Collected historical data for 4 top stocks (TCS, INFY, RELIANCE, HDFCBANK)
- Cleaned and preprocessed raw data using Pandas
- Built time series forecasting models using Facebook Prophet
- Compared models using RMSE (vs. ARIMA)
- Developed an interactive dashboard using Streamlit
- Customized visualizations using Matplotlib (no default black dots!)

This project helped me strengthen my skills in time series forecasting, data cleaning, and dashboard development.

---

## 🔧 Tech Stack

- Python (Pandas, NumPy)
- yFinance (stock data)
- Prophet (forecasting)
- ARIMA (comparison)
- Matplotlib (custom plots)
- Streamlit (web app/dashboard)

---

## 📁 Folder Structure

Stock_TimeSeries_Project/
│
├── data/ # Cleaned stock data
│ ├── TCS_stock_data_cleaned.csv
│ ├── INFY_stock_data_cleaned.csv
│ ├── RELIANCE_stock_data_cleaned.csv
│ └── HDFCBANK_stock_data_cleaned.csv
│
├── scripts/ # Core Python scripts
│ ├── get_stock_data.py # Download stock data
│ ├── clean_stock_data.py # Preprocessing and cleanup
│ ├── visualize_stock_data.py # Line chart of actual prices
│ ├── model_comparison.py # ARIMA vs Prophet evaluation
│ ├── arima_forecast.py # Forecast using ARIMA
│ └── prophet_forecast.py # Forecast using Prophet
│
├── app/
│ └── stock_forecast_app.py # Streamlit dashboard
│
├── requirements.txt
└── README.md

---

## 📈 App Features

- Multi-stock support via dropdown (TCS, INFY, RELIANCE, HDFCBANK)
- Forecast slider (predict from 7 to 60 days ahead)
- Clean visualizations (custom Matplotlib graphs)
- Confidence intervals & trend breakdowns
- User-friendly interface via Streamlit

---

## 📷 Screenshots

![Screenshot 2025-06-11 230759](https://github.com/user-attachments/assets/bfa31eae-7bf4-45c3-a344-0a4fcb2c4270)
![Screenshot 2025-06-11 230846](https://github.com/user-attachments/assets/4602ce82-f44e-456c-ba24-26de472a3b9d)
![Screenshot 2025-06-11 230914](https://github.com/user-attachments/assets/cbd5bbbd-0d13-4238-b9f2-31c18f39918d)
![Screenshot 2025-06-11 230904](https://github.com/user-attachments/assets/a2f2a547-2275-4630-9869-ac8ab226b6bd)



---

## 🧪 How to Run This Project

1. Clone the repo:
   ```bash
   git clone https://github.com/Nish0501/stock-forecast-prophet-streamlit.git
   cd stock-forecast-prophet-streamlit
   
Install dependencies:
pip install -r requirements.txt

Run the app:
streamlit run app/stock_forecast_app.py

✅ Key Takeaways
Strong understanding of time series concepts (trend, seasonality, residuals)

Learned to compare ML and statistical models (ARIMA vs Prophet)

Built a clean and informative forecasting dashboard with real-world data

Practiced project structuring and GitHub documentation for real-world visibility

🙋‍♀️ Made by Nishtha Gupta
🔗 LinkedIn Profile
🔗 GitHub Profile

If you liked this project, feel free to ⭐ star the repo or connect with me!










