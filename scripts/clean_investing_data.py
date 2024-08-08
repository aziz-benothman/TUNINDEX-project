import pandas as pd

file_path = r'data\raw\Tunindex Historical Data (2).csv'
df = pd.read_csv(file_path)

# Convert the 'Date' column to a datetime object with the format month/day/year
df['Date'] = pd.to_datetime(df['Date'], format='%m/%d/%Y')

# Set the 'Date' column as the index of the DataFrame
df.set_index('Date', inplace=True)

# Drop the 'Change %' and 'Vol.' columns as they are not needed
df.drop(columns=['Change %', 'Vol.'], inplace=True)

# Rename the index name to 'date'
df.index.name = 'date'

# Remove commas from each cell and convert the values to float
for col in df.columns:
    df[col] = df[col].str.replace(',', '').astype(float)

# Rename the columns    
df.rename(columns={'Price': 'close', 'Open': 'open', 'High': 'high', 'Low': 'low'}, inplace=True)

# Save the cleaned DataFrame to a new CSV file
df.to_csv(r'data\clean\TUNINDEX_data.csv')
