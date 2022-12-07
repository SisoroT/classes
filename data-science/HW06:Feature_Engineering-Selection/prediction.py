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


# save prices column as label
labels = df.values[:, -1]
# create new feature
df["is_close_to_school"] = df["miles_to_school"] < 2
df["lot_size"] = df["lot_width"] * df["lot_depth"]
# extract features to use
cols = df[["sqft_hvac", "lot_size", "is_close_to_school"]]
col_names = cols.columns.to_list()
features = cols.values

print(f"Using only the useful ones: {col_names}...")
# train model
model = LinearRegression()
model.fit(features, labels)
print(f"R2 = {model.score(features, labels):.5f}")

print("*** Prediction ***")
print(
    f"Price = ${model.intercept_:,.2f} + (sqft x ${model.coef_[0]:,.2f}) + (lot_size x ${model.coef_[1]:,.2f})"
)
print(
    f"\tLess than 2 miles from a school? You get ${model.coef_[-1]:,.2f} added to the price!"
)
