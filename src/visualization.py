import matplotlib.pyplot as plt
import pandas as pd

def plot_conversion_rates(results: dict):
    """
    Plot a bar chart for conversion rates of variants A and B.
    """
    variants = ['A', 'B']
    conversion_rates = [results.get("conv_rate_A", 0), results.get("conv_rate_B", 0)]
    plt.figure(figsize=(8, 6))
    plt.bar(variants, conversion_rates, color=['blue', 'green'])
    plt.xlabel('Feature Variant')
    plt.ylabel('Conversion Rate')
    plt.title('Conversion Rates for Feature Variants A and B')
    plt.ylim(0, 1)
    for i, rate in enumerate(conversion_rates):
        plt.text(i, rate + 0.02, f"{rate:.2%}", ha='center', fontsize=12)
    plt.show()

def plot_engagement_distribution(df: pd.DataFrame, group_col: str = 'feature_variant', metric_col: str = 'engagement_metric'):
    """
    Plot histograms showing the distribution of engagement metrics for both groups.
    """
    group_A = df[df[group_col] == 'A']
    group_B = df[df[group_col] == 'B']
    plt.figure(figsize=(10, 6))
    plt.hist(group_A[metric_col], bins=20, alpha=0.5, label='Variant A', color='blue')
    plt.hist(group_B[metric_col], bins=20, alpha=0.5, label='Variant B', color='green')
    plt.xlabel('Engagement Metric')
    plt.ylabel('Frequency')
    plt.title('Engagement Metric Distribution by Feature Variant')
    plt.legend()
    plt.show()

# Uncomment below for standalone testing:
# if __name__ == '__main__':
#     import data_ingestion, data_processing
#     df = data_ingestion.load_data('../data/raw/user_interactions.csv')
#     cleaned_df = data_processing.clean_data(df)
#     from ab_testing import perform_ab_test
#     results = perform_ab_test(cleaned_df)
#     plot_conversion_rates(results)
#     plot_engagement_distribution(cleaned_df)