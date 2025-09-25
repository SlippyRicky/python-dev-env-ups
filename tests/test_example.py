#!/usr/bin/env python3
"""
Test file for example.py using pytest.
This demonstrates how to write unit tests for your Python code.
"""

import sys
import os
import pytest

# Add the src directory to the path to import our module
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from example import calculate_statistics, create_sample_dataframe


class TestCalculateStatistics:
    """Test class for the calculate_statistics function."""
    
    def test_basic_statistics(self):
        """Test basic statistics calculation with simple data."""
        data = [1, 2, 3, 4, 5]
        result = calculate_statistics(data)
        
        assert result["mean"] == 3.0
        assert result["median"] == 3.0
        assert abs(result["std"] - 1.4142135623730951) < 1e-10
    
    def test_empty_list(self):
        """Test statistics calculation with empty list."""
        data = []
        result = calculate_statistics(data)
        
        assert result["mean"] == 0
        assert result["median"] == 0
        assert result["std"] == 0
    
    def test_single_value(self):
        """Test statistics calculation with single value."""
        data = [42]
        result = calculate_statistics(data)
        
        assert result["mean"] == 42.0
        assert result["median"] == 42.0
        assert result["std"] == 0.0
    
    def test_negative_numbers(self):
        """Test statistics calculation with negative numbers."""
        data = [-5, -3, -1, 1, 3, 5]
        result = calculate_statistics(data)
        
        assert result["mean"] == 0.0
        assert result["median"] == 0.0
        assert abs(result["std"] - 3.415650255319866) < 1e-10


class TestCreateSampleDataframe:
    """Test class for the create_sample_dataframe function."""
    
    def test_dataframe_creation(self):
        """Test that DataFrame is created correctly."""
        df = create_sample_dataframe()
        
        # Check shape
        assert df.shape == (5, 3)
        
        # Check columns
        expected_columns = ["name", "age", "score"]
        assert list(df.columns) == expected_columns
        
        # Check data types
        assert df["name"].dtype == "object"
        assert df["age"].dtype in ["int64", "int32"]  # Can vary by platform
        assert df["score"].dtype == "float64"
    
    def test_dataframe_content(self):
        """Test that DataFrame contains expected content."""
        df = create_sample_dataframe()
        
        # Check some specific values
        assert df.loc[0, "name"] == "Alice"
        assert df.loc[0, "age"] == 25
        assert df.loc[0, "score"] == 85.5
        
        # Check that all names are strings
        assert all(isinstance(name, str) for name in df["name"])
        
        # Check that all ages are positive integers
        assert all(isinstance(age, (int, int)) and age > 0 for age in df["age"])
        
        # Check that all scores are positive floats
        assert all(isinstance(score, float) and score > 0 for score in df["score"])


def test_integration_example():
    """Integration test that uses both functions together."""
    df = create_sample_dataframe()
    ages = df["age"].tolist()
    scores = df["score"].tolist()
    
    age_stats = calculate_statistics(ages)
    score_stats = calculate_statistics(scores)
    
    # Basic sanity checks
    assert age_stats["mean"] > 0
    assert score_stats["mean"] > 0
    assert len(ages) == len(scores) == 5


if __name__ == "__main__":
    # Run tests when script is executed directly
    pytest.main([__file__, "-v"])