# TUNINDEX Price Forecasting Using ARIMA-GARCH Models

This project focuses on forecasting the price of the Tunisian stock index (TUNINDEX) using a combination of ARIMA and GARCH models. The goal is to predict future prices and estimate the confidence intervals based on volatility forecasts.

## Project Overview

This repository contains scripts and code for:

- Downloading and cleaning data.
- Building ARIMA and GARCH models.
- Forecasting future prices.
- Estimating volatility for confidence intervals.

The project is structured to automatically download new data, update the models, and forecast the next business day's TUNINDEX price.

### Main Features:
1. **ARIMA Model**: Used for predicting the TUNINDEX price based on historical data.
2. **GARCH Model**: Applied to the residuals of the ARIMA model to capture volatility and build confidence intervals.
3. **Automation**: Scripts are designed to run automatically, download the latest data, clean it, and update forecasts.
