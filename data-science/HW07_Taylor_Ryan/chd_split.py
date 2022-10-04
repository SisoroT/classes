import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv("framingham.csv", index_col=False)
print(f"Read {df.shape[0]} rows")

# Drop rows with missing values
## Your code here

print(f"Using {df.shape[0]} rows")

# Split into training and testing dataframes
## Your code here

# Write out each as a CSV
## Your code here
