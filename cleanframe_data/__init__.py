from cleanframe_data.pipeline import auto_clean
from cleanframe_data.analyzer import DatasetAnalyzer
from cleanframe_data.cleaner import DataCleaner

# Standalone convenience wrapper to handle outliers globally
def remove_outliers(df):
    """
    Convenience wrapper for exposing the class method globally.
    """
    return DataCleaner(df).handle_outliers().get_df()

__all__ = ['auto_clean', 'DatasetAnalyzer', 'DataCleaner', 'remove_outliers']