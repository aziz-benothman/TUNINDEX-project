import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model
import numpy as np

class ARIMAModel:
    
    def fit(self, data, order=(1, 1, 2)):
        self.model = ARIMA(data, order=order).fit()  
        self.residuals = self.model.resid 
        return self.model

    def forecast(self, steps=1):
        return self.model.forecast(steps=steps)

class GARCHModel:
    
    def fit(self, residuals, p=1, q=1):
        residuals = residuals.dropna()
        self.model = arch_model(residuals, vol='Garch', p=p, q=q).fit(disp="off")
        return self.model

    def forecast_volatility(self, steps=1):
        forecast = self.model.forecast(start=0, horizon=steps)
        return forecast.variance.values[-1]  # Return forecasted variance (volatility squared)

if __name__ == "__main__":
    
    data = pd.read_csv('data/clean/arima_data.csv', index_col='date', parse_dates=True)
    
    # Ensure the index is a DatetimeIndex with a business day frequency
    data.index = pd.to_datetime(data.index)
    data = data.asfreq('B')  # Set frequency to business days

    # Initialize and fit ARIMA model
    arima_model = ARIMAModel()
    arima_model.fit(data['close'])
    
    # Forecast the next business day's price
    next_day_price_forecast = arima_model.forecast(steps=1)
    
    # Initialize and fit GARCH model using ARIMA residuals
    garch_model = GARCHModel()
    garch_model.fit(residuals=arima_model.residuals)
    
    # Forecast the next business day's volatility (standard deviation)
    next_day_volatility = garch_model.forecast_volatility(steps=1)[0] ** 0.5  # Convert variance to standard deviation
    
    # Get the actual last price (yesterday's price)
    actual_last_price = data['close'].iloc[-1]
    
    # Calculate the difference
    difference = next_day_price_forecast[0] - actual_last_price
    
    # Confidence Interval Calculation
    z_score = 1.96  # For a 95% confidence interval
    lower_bound = next_day_price_forecast[0] - z_score * next_day_volatility
    upper_bound = next_day_price_forecast[0] + z_score * next_day_volatility

    
    
    print(f"Next business day's forecasted price: {next_day_price_forecast[0]}\n"
          f"Yesterday's actual price: {actual_last_price}\n"
          f"Price Difference: {difference}\n"
          f"Forecasted Volatility: {next_day_volatility}\n"
          f"95% Confidence Interval: ({lower_bound}, {upper_bound})\n"
          )
