import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model

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

# Example usage:
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
    
    # Forecast the next business day's volatility
    next_day_volatility = garch_model.forecast_volatility(steps=1)[0] ** 0.5  # Convert to standard deviation
    
    # Get the actual last price (yesterday's price)
    actual_last_price = data['close'].iloc[-1]
    
    # Calculate the difference
    difference = next_day_price_forecast[0] - actual_last_price
    
    # Provide advice based on the forecasts
    if next_day_price_forecast[0] > actual_last_price:
        if next_day_volatility < data['close'].pct_change().std():  # Compare forecasted volatility with historical volatility
            advice = "The forecast suggests the price will increase with low risk. It might be a good time to buy."
        else:
            advice = "The forecast suggests the price will increase but with higher risk. Buy with caution."
    else:
        if next_day_volatility < data['close'].pct_change().std():  # Compare forecasted volatility with historical volatility
            advice = "The forecast suggests the price will decrease with low risk. Consider selling."
        else:
            advice = "The forecast suggests the price will decrease with higher risk. Consider selling or holding off."

    # Print the results and advice
    print(f"Next business day's forecasted price: {next_day_price_forecast}\n"
          f"Yesterday's actual price: {actual_last_price}\n"
          f"Price Difference: {difference}\n"
          f"Forecasted Volatility: {next_day_volatility}\n"
          f"Advice: {advice}")
