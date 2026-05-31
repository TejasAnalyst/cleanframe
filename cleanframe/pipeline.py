import pandas as pd
from cleanframe.cleaner import DataCleaner

def auto_clean(df: pd.DataFrame, numerical_strategy: str = 'median', categorical_strategy: str = 'mode') -> pd.DataFrame:
    """
    Automatically cleans a pandas DataFrame in one line.
    Removes duplicates and fills missing values.
    
    Usage:
        import cleanframe as cf
        df_clean = cf.auto_clean(df)
    """
    if not isinstance(df, pd.DataFrame):
        raise TypeError("Input must be a valid pandas DataFrame.")
        
    # Instantiate DataCleaner and execute the baseline pipeline
    cleaner = DataCleaner(df)
    cleaned_df = (cleaner
                  .drop_duplicates()
                  .handle_missing(numerical_strategy=numerical_strategy, 
                                  categorical_strategy=categorical_strategy)
                  .get_df())
                  
    return cleaned_df