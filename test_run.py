import pandas as pd
import numpy as np
import cleanframe as cf

# Create a extreme messy dataset with outliers and high missing column
raw_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Bob', 'David'],
    'Age': [25, np.nan, 30, np.nan, 28],
    'Salary': [50000, 60000, 55000, 60000, 999999], # 999999 is a huge outlier!
    'Empty_Col': [np.nan, np.nan, np.nan, np.nan, 'Value'] # 80% missing data
}
df = pd.DataFrame(raw_data)

print("=== ORIGINAL UNCLEANED DATA ===")
print(df)
print("\n" + "="*40 + "\n")

# Run the advanced one-liner magic
cleaned_df = cf.auto_clean(df, missing_threshold=0.5, handle_outliers=True)

print("=== ADVANCED CLEANED DATA ===")
print(cleaned_df)