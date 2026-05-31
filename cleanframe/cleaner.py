import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        """
        Initialize the cleaner with a pandas DataFrame.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Input must be a valid pandas DataFrame.")
        self.df = df.copy()  # Explicit copy to safeguard original data

    def drop_duplicates(self) -> 'DataCleaner':
        """
        Removes duplicate rows from the dataset.
        """
        self.df = self.df.drop_duplicates()
        return self

    def handle_missing(self, numerical_strategy: str = 'median', categorical_strategy: str = 'mode') -> 'DataCleaner':
        """
        Automatically handles missing values based on column data types without ChainedAssignment.
        """
        for col in self.df.columns:
            if self.df[col].isnull().sum() > 0:
                # Handle Numerical Columns
                if pd.api.types.is_numeric_dtype(self.df[col]):
                    if numerical_strategy == 'median':
                        fill_value = self.df[col].median()
                    elif numerical_strategy == 'mean':
                        fill_value = self.df[col].mean()
                    else:
                        fill_value = 0
                    # Standard assignment avoids Copy-on-Write warnings
                    self.df[col] = self.df[col].fillna(fill_value)
                
                # Handle Categorical/Object Columns
                else:
                    if categorical_strategy == 'mode':
                        fill_value = self.df[col].mode()[0] if not self.df[col].mode().empty else "Unknown"
                    else:
                        fill_value = "Unknown"
                    self.df[col] = self.df[col].fillna(fill_value)
                    
        return self

    def get_df(self) -> pd.DataFrame:
        """
        Returns the final cleaned DataFrame.
        """
        return self.df