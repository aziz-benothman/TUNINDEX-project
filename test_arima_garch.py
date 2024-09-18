import pandas as pd
from statsmodels.tsa.arima.model import ARIMA
from arch import arch_model
import numpy as np

df = pd.read_csv('data/clean/arima_data.csv', index_col='date', parse_dates=True)
df.index = pd.to_datetime(df.index)
df = df.asfreq('B')
model = ARIMA(df['close'], order=(1, 1, 1))
model_fit = model.fit()
residuals = model_fit.resid


# Recheck for any NaNs or Infs in the residuals
print(residuals[~np.isfinite(residuals)])  # This will print any problematic values
print(type(residuals))