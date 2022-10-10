import pandas as pd
import numpy as np
import pickle as pkl

TRAIN_PATH = "train_gn.csv"
PARAMETERS_PATH = "parameters_gn.pkl"

def show_array(category_label, array, labels):
    print(f"\t{category_label} -> ", end="")
    for i in range(len(array)):
        print(f"{labels[i]}:{array[i]: >7.4f}     ", end="")
    print()

train_df = pd.read_csv(TRAIN_PATH)
X_df = train_df.iloc[:, :-1]
Y_df = train_df.iloc[:, -1]
n = len(X_df)
d = len(X_df.columns)
print(f"Read {n} samples with {d} attributes from {TRAIN_PATH}")

## Your code here

print(f"Wrote parameters to {PARAMETERS_PATH}")
