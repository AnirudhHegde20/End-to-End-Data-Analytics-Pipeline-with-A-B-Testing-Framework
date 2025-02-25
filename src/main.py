from data_ingestion import load_data
from data_processing import clean_data
from database_storage import store_to_sql, store_to_mongodb
from ab_testing import perform_ab_test
from visualization import plot_conversion_rates, plot_engagement_distribution

def main():
    # 1. Data Ingestion: Load the attached CSV dataset
    raw_data_path = '../data/raw/user_interactions.csv'
    df = load_data(raw_data_path)

    # 2. Data Processing: Clean and transform the data
    cleaned_df = clean_data(df)

    # Optionally, save the processed data for reference
    processed_path = '../data/processed/cleaned_data.csv'
    cleaned_df.to_csv(processed_path, index=False)
    print("Processed data saved to:", processed_path)

    # 3. Database Storage: Save data to SQL (SQLite) and NoSQL (MongoDB)
    store_to_sql(cleaned_df)
    store_to_mongodb(cleaned_df)

    # 4. A/B Testing Analysis: Evaluate the effectiveness of feature variants
    results = perform_ab_test(cleaned_df)

    # 5. Visualization: Plot conversion rates and engagement distributions
    plot_conversion_rates(results)
    plot_engagement_distribution(cleaned_df)

if __name__ == '__main__':
    main()