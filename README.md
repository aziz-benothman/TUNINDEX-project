# TUNINDEX Price Forecasting Using ARIMA-GARCH Models

This project focuses on forecasting the price of the Tunisian stock index (TUNINDEX) using a combination of ARIMA and GARCH models. The goal is to predict future prices and estimate confidence intervals based on volatility forecasts.

## Project Overview

This repository contains the following components for forecasting TUNINDEX prices:

- **Data Downloading and Cleaning**: Automated scripts to download and preprocess TUNINDEX data.
- **Exploratory Data Analysis (EDA)**: Detailed analysis to uncover trends, seasonality, and volatility in the TUNINDEX data.
- **Parameter Estimation and Model Validation**: Estimating parameters for ARIMA and GARCH models, validating model hypotheses, and checking goodness of fit.
- **ARIMA and GARCH Modeling**: Building models to forecast price movements and volatility.
- **Price Forecasting**: Predicting future prices of TUNINDEX.
- **Volatility Estimation**: Providing confidence intervals with 95% confidence 

The project is designed to automatically download new data, update the models, and forecast the next business day's TUNINDEX price.

### Main Features

1. **Exploratory Data Analysis (EDA)**: Visualizes and analyzes historical trends, seasonality, stationarity, and volatility in the TUNINDEX dataset. This is detailed in the notebooks 
2. **Parameter Estimation and Model Validation**: The notebook focuses on estimating the parameters for ARIMA and GARCH, using mse and validating the model through walk-forward validation.
3. **ARIMA Model**: Utilized for forecasting the TUNINDEX price based on historical time series data.
4. **GARCH Model**: Applied to the residuals of the ARIMA model to capture volatility and estimate confidence intervals.
5. **Automation**: Scripts that automate the process of data downloading, cleaning.
