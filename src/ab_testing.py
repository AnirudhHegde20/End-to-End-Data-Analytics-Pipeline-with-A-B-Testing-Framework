import pandas as pd
from scipy import stats

def perform_ab_test(df: pd.DataFrame, group_col: str = 'feature_variant', metric_col: str = 'conversion'):
    """
    Perform A/B testing on the dataset.
    Splits the DataFrame into two groups and calculates conversion rates.
    Conducts a t-test to check for statistical significance.
    Returns a dictionary with the results.
    """
    try:
        group_A = df[df[group_col] == 'A']
        group_B = df[df[group_col] == 'B']
        conv_rate_A = group_A[metric_col].mean()
        conv_rate_B = group_B[metric_col].mean()
        t_stat, p_value = stats.ttest_ind(group_A[metric_col], group_B[metric_col])
        results = {
            "conv_rate_A": conv_rate_A,
            "conv_rate_B": conv_rate_B,
            "t_stat": t_stat,
            "p_value": p_value
        }
        print(f"Conversion Rate for Variant A: {conv_rate_A:.2%}")
        print(f"Conversion Rate for Variant B: {conv_rate_B:.2%}")
        print(f"T-statistic: {t_stat:.3f}, P-value: {p_value:.3f}")
        return results
    except Exception as e:
        raise Exception(f"Error during A/B testing: {e}")

# Uncomment below for standalone testing:
# if __name__ == '__main__':
#     import data_ingestion, data_processing
#     df = data_ingestion.load_data('../data/raw/user_interactions.csv')
#     cleaned_df = data_processing.clean_data(df)
#     perform_ab_test(cleaned_df)