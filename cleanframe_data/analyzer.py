import pandas as pd

class DatasetAnalyzer:
    def __init__(self, df: pd.DataFrame):
        """
        Initialize the analyzer with a pandas DataFrame.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Input must be a valid pandas DataFrame.")
        self.df = df

    def get_summary(self) -> pd.DataFrame:
        """
        Generates a complete diagnostic summary of the dataset.
        Includes Data Type, Missing Values count, and Missing Percentage.
        """
        total_rows = len(self.df)
        
        # Calculate missing values and their percentage
        missing_count = self.df.isnull().sum()
        missing_percentage = (missing_count / total_rows) * 100
        
        # Get data types
        data_types = self.df.dtypes
        
        # Combine metrics into a structured summary DataFrame
        summary_df = pd.DataFrame({
            'Data Type': data_types,
            'Missing Values': missing_count,
            'Missing (%)': missing_percentage.round(2)
        })
        
        return summary_df

    def check_duplicates(self) -> int:
        """
        Returns the total number of duplicate rows in the dataset.
        """
        return int(self.df.duplicated().sum())