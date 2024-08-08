import pandas as pd

class TradingDayChecker:

    def __init__(self, filepath,start_date='2024-08-01'):
        self.filepath = filepath
        self.dataframe = pd.read_csv(filepath,index_col='date', parse_dates=['date'])
        self.start_date = pd.to_datetime(start_date)
    def check_missing_trading_days(self):
        """
        Checks for any missing stock trading days (Monday to Friday) in the dataset.
        
        :return: A list of missing dates if any, or an empty list if none are missing.
        """
        # Generate the full range of trading days between the minimum and maximum dates in the DataFrame
        all_trading_days = pd.date_range(start=self.start_date, 
                                         end=self.dataframe.index.max(), 
                                         freq='B')  # 'B' stands for business day

        # Identify missing days
        missing_days = all_trading_days.difference(self.dataframe.index)

        if not missing_days.empty:
            print(f"Missing stock trading days: {missing_days.tolist()}")
        else:
            print("No missing trading days found.")

        return missing_days.tolist()

        