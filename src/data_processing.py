import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean and process the data.
    - Convert timestamps to datetime.
    - Drop rows with missing values.
    - Ensure 'conversion' is an integer.
    - Optionally extract the hour from the timestamp.
    """
    try:
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        df.dropna(inplace=True)
        df['conversion'] = df['conversion'].astype(int)
        df['hour'] = df['timestamp'].dt.hour  # Feature engineering example
        print("Data cleaning and processing completed.")
        return df
    except Exception as e:
        raise Exception(f"Error during data cleaning: {e}")

# Uncomment below for standalone testing:
# if __name__ == '__main__':
#     import data_ingestion
#     df = data_ingestion.load_data('../data/raw/user_interactions.csv')
#     cleaned_df = clean_data(df)
#     print(cleaned_df.head())