# scripts/combined_script.py
import os

from scripts.data_downloader import DataDownloader
from scripts.data_cleaner import DataCleaner
from scripts.trading_day_checker import TradingDayChecker

def main():
    project_folder_path = os.getcwd()
    downloader = DataDownloader(project_folder_path)
    cleaner = DataCleaner()
    clean_file_name = 'TUNINDEX_data.csv'
    clean_data_path = os.path.join(project_folder_path, 'data', 'clean', clean_file_name)
    input_file_name = 'cotations_px1.csv'
    input_file_path = os.path.join(project_folder_path, 'data', 'raw', input_file_name)
    
    checker = TradingDayChecker(clean_data_path)

    print("Step 1: Downloading data...")
    try:
        downloader.download_data()
    except Exception as e:
        print(f"An error occurred during the download: {e}")
        exit(1)

    print("Step 2: Cleaning data...")
    try:
        cleaner.clean_ilboursa_data(input_file_path, clean_data_path)
    except Exception as e:
        print(f"An error occurred during data cleaning: {e}")
        exit(1)
    print("Step 3: Checking for missed entries ...")
 
    checker.check_missing_trading_days()

    print("Main script completed.")

if __name__ == "__main__":
    main()
