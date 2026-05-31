import pandas as pd
from cleanframe_data.cleaner import DataCleaner

def auto_clean(df: pd.DataFrame, 
               missing_threshold: float = 0.5,
               numerical_strategy: str = 'median', 
               categorical_strategy: str = 'mode',
               handle_outliers: bool = True) -> pd.DataFrame:
    """
    Advanced automated data cleaning pipeline.
    1. Drops duplicates
    2. Drops columns with high missing data
    3. Imputes missing values
    4. Caps numerical outliers (Optional)
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a valid pandas DataFrame.")
        
    cleaner = DataCleaner(df)
    
    # Execute step-by-step cleaning pipeline
    cleaner.drop_duplicates()
    cleaner.drop_high_missing_columns(threshold=missing_threshold)
    cleaner.handle_missing(numerical_strategy=numerical_strategy, 
                           categorical_strategy=categorical_strategy)
    
    if handle_outliers:
        cleaner.handle_outliers()
                  
    return cleaner.get_df()