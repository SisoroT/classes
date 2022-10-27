import pandas as pd
from sklearn.metrics import r2_score
import pycaret.regression as carreg
from time import perf_counter
import glob
import os

# Read in testing data (none of the colums are an index)
## Your code here

# Break into two dataframes
X_test = ## Your code here
y_test = ## Your code here

# Get a list of all the pkl files in the current directory
## Your code here

# Hack off the .pkl extension
model_names = [os.path.splitext(p)[0] for p in model_files]

# For each model
for model_name in model_names:

    # Load the model
    model = ## Your code here

    # Do the inference
    t1 = perf_counter()
    y_pred = ## Your code here
    t2 = perf_counter()

    # Get the R2 score
    r2 = ## Your code here

    # Print the results
    print(f"{model_name}:")
    print(f"\tInference: {t2 - t1:.4f} seconds")
    print(f"\tR2 on test data = {r2:.4f}")
