import pandas as pd
import numpy as np
import cleanframe as cf  # Importing our library just like a pro!

# 1. Create dummy raw dataset
raw_data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Bob', None],
    'Age': [25, np.nan, 30, np.nan, 22],
    'City': ['Mumbai', 'Delhi', None, 'Delhi', 'Pune']
}
df = pd.DataFrame(raw_data)

print("=== ORIGINAL UNCLEANED DATA ===")
print(df)
print("\n" + "="*40 + "\n")

# 2. THE ONE-LINE MAGIC MAGIC 🪄
cleaned_df = cf.auto_clean(df)

print("=== CLEANED DATA USING cf.auto_clean(df) ===")
print(cleaned_df)