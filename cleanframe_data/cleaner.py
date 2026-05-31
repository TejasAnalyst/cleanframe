import pandas as pd
import numpy as np

class DataCleaner:
    def __init__(self, df: pd.DataFrame):
        """
        Initialize the cleaner with a pandas DataFrame.
        """
        if not isinstance(df, pd.DataFrame):
            raise TypeError("Input must be a valid pandas DataFrame.")
        self.df = df.copy()

    def drop_duplicates(self) -> 'DataCleaner':
        """
        Removes duplicate rows from the dataset.
        """
        self.df = self.df.drop_duplicates()
        return self

    def drop_high_missing_columns(self, threshold: float = 0.5) -> 'DataCleaner':
        """
        Drops columns where the percentage of missing values is above the threshold.
        Example: threshold=0.5 will drop columns with more than 50% missing data.
        """
        total_rows = len(self.df)
        for col in self.df.columns:
            missing_pct = self.df[col].isnull().sum() / total_rows
            if missing_pct > threshold:
                self.df = self.df.drop(columns=[col])
        return self

    def handle_missing(self, numerical_strategy: str = 'median', categorical_strategy: str = 'mode') -> 'DataCleaner':
        """
        Automatically handles missing values based on column data types without ChainedAssignment.
        """
        for col in self.df.columns:
            if self.df[col].isnull().sum() > 0:
                if pd.api.types.is_numeric_dtype(self.df[col]):
                    if numerical_strategy == 'median':
                        fill_value = self.df[col].median()
                    elif numerical_strategy == 'mean':
                        fill_value = self.df[col].mean()
                    else:
                        fill_value = 0
                    self.df[col] = self.df[col].fillna(fill_value)
                else:
                    if categorical_strategy == 'mode':
                        fill_value = self.df[col].mode()[0] if not self.df[col].mode().empty else "Unknown"
                    else:
                        fill_value = "Unknown"
                    self.df[col] = self.df[col].fillna(fill_value)
                    
        return self

    def handle_outliers(self, method: str = 'iqr') -> 'DataCleaner':
        """
        Detects and caps numerical outliers using the Interquartile Range (IQR) method.
        Values beyond 1.5 * IQR are capped to the lower and upper bounds.
        """
        for col in self.df.columns:
            if pd.api.types.is_numeric_dtype(self.df[col]):
                q1 = self.df[col].quantile(0.25)
                q3 = self.df[col].quantile(0.75)
                iqr = q3 - q1
                
                lower_bound = q1 - 1.5 * iqr
                upper_bound = q3 + 1.5 * iqr
                
                # Capping the outlier values to bounds
                self.df[col] = np.where(self.df[col] < lower_bound, lower_bound, self.df[col])
                self.df[col] = np.where(self.df[col] > upper_bound, upper_bound, self.df[col])
                
        return self

    def get_df(self) -> pd.DataFrame:
        """
        Returns the final cleaned DataFrame.
        """
        return self.df