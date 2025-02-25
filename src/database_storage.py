import pandas as pd
from sqlalchemy import create_engine
from pymongo import MongoClient

def store_to_sql(df: pd.DataFrame, db_path: str = 'sqlite:///analytics.db'):
    """
    Store the DataFrame into a SQL database using SQLAlchemy.
    """
    try:
        engine = create_engine(db_path)
        df.to_sql('user_data', con=engine, if_exists='replace', index=False)
        print("Data stored in SQL database successfully.")
    except Exception as e:
        raise Exception(f"Error storing data in SQL database: {e}")

def store_to_mongodb(df: pd.DataFrame, uri: str = 'mongodb://localhost:27017/', db_name: str = 'analytics_db'):
    """
    Store the DataFrame into a MongoDB collection.
    """
    try:
        client = MongoClient(uri)
        db = client[db_name]
        collection = db['user_data']
        collection.delete_many({})  # Clear existing data
        collection.insert_many(df.to_dict('records'))
        print("Data stored in MongoDB successfully.")
    except Exception as e:
        raise Exception(f"Error storing data in MongoDB: {e}")

# Uncomment below for standalone testing:
# if __name__ == '__main__':
#     import data_ingestion, data_processing
#     df = data_ingestion.load_data('../data/raw/user_interactions.csv')
#     cleaned_df = data_processing.clean_data(df)
#     store_to_sql(cleaned_df)
#     store_to_mongodb(cleaned_df)