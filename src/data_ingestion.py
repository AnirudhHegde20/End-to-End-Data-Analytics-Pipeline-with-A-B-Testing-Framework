import pandas as pd
import os

def load_data(file_path: str) -> pd.DataFrame:
    """
    Load raw data from a CSV file.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File {file_path} does not exist.")
    try:
        df = pd.read_csv(file_path)
        print("Dataset loaded successfully.")
        return df
    except Exception as e:
        raise Exception(f"Error loading dataset: {e}")

# Uncomment below for standalone testing:
# if __name__ == '__main__':
#     df = load_data('../data/raw/user_interactions.csv')
#     print(df.head())