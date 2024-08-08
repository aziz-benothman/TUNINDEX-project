# scripts/data_cleaner.py
import pandas as pd
import os

class DataCleaner:
    def clean_ilboursa_data(self, input_file_path, output_file_path):
        print(f"Starting data cleaning for {input_file_path}...")
        df = pd.read_csv(input_file_path, delimiter=';')

        # Convert columns to appropriate data types
        df['date'] = pd.to_datetime(df['date'], format='%d/%m/%Y')
        for col in ['ouverture', 'haut', 'bas', 'cloture']:
            df[col] = df[col].str.replace(' ', '').str.replace(',', '.').astype(float)

        # Drop symbol column
        df.drop(columns=['symbole', 'volume'], inplace=True)

        # Set 'date' as the df index
        df.set_index('date', inplace=True)

        # Reorder columns to match the investing.com format
        new_order = ['cloture', 'ouverture', 'haut', 'bas']
        df = df[new_order]

        # Rename columns to English
        df.rename(columns={'cloture': 'close', 'ouverture': 'open', 'haut': 'high', 'bas': 'low'}, inplace=True)

        # Sort by date
        df.sort_index(ascending=False, inplace=True)

        # Read old data and find new entries
        df_old = pd.read_csv(os.path.join('data', 'clean', 'TUNINDEX_data.csv'), index_col='date', parse_dates=['date'])
        new_entries = df[~df.index.isin(df_old.index)]

        # Combine old data and the new entries
        combined_data = pd.concat([new_entries, df_old])

        # Save the combined data to a new CSV file
        combined_data.to_csv(output_file_path, index=True)

        # Delete the original unorganized data file
        if os.path.exists(input_file_path):
            os.remove(input_file_path)
            print(f"Deleted the original unorganized data file: {input_file_path}")
        else:
            print(f"The file {input_file_path} does not exist and could not be deleted.")

        print(f"Data cleaning for {input_file_path} completed.")

if __name__ == '__main__':
    cleaner = DataCleaner()
    cleaner.clean_ilboursa_data('data/raw/cotations_PX1.csv', 'data/clean/TUNINDEX_data.csv')