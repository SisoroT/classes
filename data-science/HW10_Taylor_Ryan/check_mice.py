import numpy as np
import pandas as pd
from scipy.stats import chi2

# Read in the data
mice_df = pd.read_csv("mice.csv")

# Figure out the possible gene types
gene_types = list(mice_df.gene_type.unique())
print(f"Possible gene types:{gene_types}")

## Your code here
