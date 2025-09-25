#!/usr/bin/env python3
"""
Example Python script for UPS M1 SGM programming class.
This demonstrates basic Python concepts and good coding practices.
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def calculate_statistics(data):
    """
    Calculate basic statistics for a list of numbers.
    
    Args:
        data (list): List of numbers
        
    Returns:
        dict: Dictionary containing mean, median, and standard deviation
    """
    if not data:
        return {"mean": 0, "median": 0, "std": 0}
    
    np_data = np.array(data)
    return {
        "mean": np.mean(np_data),
        "median": np.median(np_data),
        "std": np.std(np_data)
    }


def create_sample_dataframe():
    """
    Create a sample pandas DataFrame for demonstration.
    
    Returns:
        pd.DataFrame: Sample data
    """
    data = {
        "name": ["Alice", "Bob", "Charlie", "Diana", "Eve"],
        "age": [25, 30, 35, 28, 32],
        "score": [85.5, 92.0, 78.5, 88.0, 95.5]
    }
    return pd.DataFrame(data)


def plot_sample_data(df):
    """
    Create a simple plot from the sample data.
    
    Args:
        df (pd.DataFrame): Data to plot
    """
    plt.figure(figsize=(10, 6))
    
    # Bar plot of scores by name
    plt.bar(df["name"], df["score"])
    plt.title("Scores by Person")
    plt.xlabel("Name")
    plt.ylabel("Score")
    plt.xticks(rotation=45)
    plt.tight_layout()
    
    # Show plot
    plt.show()


def main():
    """Main function to demonstrate the functionality."""
    print("=== Python Environment Demo ===")
    
    # Example 1: Basic statistics
    sample_data = [10, 15, 20, 25, 30, 35, 40]
    stats = calculate_statistics(sample_data)
    print(f"Sample data: {sample_data}")
    print(f"Statistics: {stats}")
    
    # Example 2: Pandas DataFrame
    df = create_sample_dataframe()
    print("\nSample DataFrame:")
    print(df)
    
    print(f"\nDataFrame info:")
    print(f"Shape: {df.shape}")
    print(f"Columns: {list(df.columns)}")
    
    # Example 3: Data analysis
    print(f"\nData analysis:")
    print(f"Average age: {df['age'].mean():.1f}")
    print(f"Average score: {df['score'].mean():.1f}")
    print(f"Highest score: {df['score'].max()}")
    
    # Uncomment the next line to show the plot
    # plot_sample_data(df)


if __name__ == "__main__":
    main()