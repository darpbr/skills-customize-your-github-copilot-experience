# Statistics with Python - Starter Code
# Assignment: Perform statistical analysis using pandas and numpy

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Task 1: Basic Statistical Analysis
def load_and_analyze_data(file_path):
    """
    Load dataset and perform basic statistical analysis
    """
    # Load the dataset
    df = pd.read_csv(file_path)

    # Display basic information
    print("Dataset shape:", df.shape)
    print("Columns:", list(df.columns))
    print("Data types:")
    print(df.dtypes)
    print("\nFirst 5 rows:")
    print(df.head())

    # Handle missing values
    print("\nMissing values:")
    print(df.isnull().sum())

    # Basic statistics for numerical columns
    numerical_cols = df.select_dtypes(include=[np.number]).columns
    if len(numerical_cols) > 0:
        print("\nDescriptive statistics for numerical columns:")
        print(df[numerical_cols].describe())

        # Additional calculations using numpy
        for col in numerical_cols:
            print(f"\n{col} statistics:")
            print(f"  Mean: {np.mean(df[col].dropna()):.2f}")
            print(f"  Median: {np.median(df[col].dropna()):.2f}")
            print(f"  Standard Deviation: {np.std(df[col].dropna()):.2f}")
            print(f"  Variance: {np.var(df[col].dropna()):.2f}")

    return df

# Task 2: Statistical Calculations and Tests
def perform_statistical_analysis(df):
    """
    Perform advanced statistical analysis
    """
    numerical_cols = df.select_dtypes(include=[np.number]).columns

    if len(numerical_cols) > 1:
        # Correlation matrix
        corr_matrix = df[numerical_cols].corr()
        print("\nCorrelation Matrix:")
        print(corr_matrix)

        # Visualize correlation
        plt.figure(figsize=(10, 8))
        plt.imshow(corr_matrix, cmap='coolwarm', interpolation='none')
        plt.colorbar()
        plt.xticks(range(len(numerical_cols)), numerical_cols, rotation=45)
        plt.yticks(range(len(numerical_cols)), numerical_cols)
        plt.title('Correlation Matrix')
        plt.tight_layout()
        plt.savefig('correlation_matrix.png')
        plt.show()

    # Group by categorical variables if any
    categorical_cols = df.select_dtypes(include=['object', 'category']).columns
    if len(categorical_cols) > 0 and len(numerical_cols) > 0:
        for cat_col in categorical_cols:
            print(f"\nGrouped statistics by {cat_col}:")
            grouped = df.groupby(cat_col)[numerical_cols].agg(['mean', 'std', 'count'])
            print(grouped)

    # Example of simple statistical test (if applicable)
    # This is a placeholder - students should implement appropriate tests
    if len(numerical_cols) >= 2:
        col1, col2 = numerical_cols[:2]
        # Simple correlation test
        correlation = np.corrcoef(df[col1].dropna(), df[col2].dropna())[0, 1]
        print(f"\nCorrelation between {col1} and {col2}: {correlation:.3f}")

# Main execution
if __name__ == "__main__":
    # Replace 'data.csv' with the actual dataset file path
    file_path = 'data.csv'  # You may need to adjust this path

    try:
        # Load and analyze data
        data = load_and_analyze_data(file_path)

        # Perform statistical analysis
        perform_statistical_analysis(data)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found. Please ensure the dataset file exists.")
    except Exception as e:
        print(f"An error occurred: {e}")