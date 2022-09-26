import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <csv>")
    sys.exit(1)

infilename = sys.argv[1]

df = pd.read_csv(infilename, index_col="property_id")

print("Making new features...")

## Your code here
