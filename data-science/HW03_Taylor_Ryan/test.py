import numpy as np
import pandas as pd

df = pd.read_excel("properties.xlsx")

X = df.iloc[:, :-1].to_numpy()
Y = df.iloc[:, -1].to_numpy()
labels = df.iloc[:, :-1].columns.to_list()

pred_string = f"$32,362.85 + ($85.61 x {labels[1]}) + ($2.73 x {labels[2]}) + ($59,195.07 x {labels[3]}) + ($9,599.24 x {labels[4]}) + ($-17,421.84 x {labels[5]})"


print(pred_string)
