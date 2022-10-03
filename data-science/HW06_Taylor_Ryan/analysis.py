import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from scipy.stats import pearsonr
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import sys

# Deal with command-line
if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} <csv>")
    sys.exit(1)
infilename = sys.argv[1]

# Read in the basic data frame
df = pd.read_csv(infilename, index_col="property_id")
X_basic = df.values[:, :-1]
labels_basic = df.columns[:-1]
Y = df.values[:, -1]

# Expand to a 2-degree polynomials
poly = PolynomialFeatures(2)

# Prepare for loop
residual = Y

# We always need the column of zeros to
# include the intercept
feature_indices = [0]

while len(feature_indices) < 3:
    p_values = []

    # Calculate the p-value of the Pearson correlation between each input and the current residual
    for i in range(len(X_basic[0])):
        p_values.append(pearsonr(X_basic[:, i], residual)[1])
        print(f"\t{df.columns[i]} vs residual: p-value={p_values[i]}")

    p_values = np.array(p_values)

    # Sort the inputs so that the p-values are in ascending order
    sorted_indices = np.argsort(p_values)

    # Add the input with the lowest p-value to the list of inputs you are going to actually use
    feature_indices.append(sorted_indices[0])
    X = X_basic[:, feature_indices]

    # create list of features in use
    features = df.columns[feature_indices].to_list()

    # Do linear regression using that list of inputs
    print(f'**** Fitting with ["{feature_indices[1:]}" "{features[1:]}"] ****')
    model = LinearRegression()
    model.fit(X, Y)

    # Print the R2 value
    print(f"R2: {model.score(X, Y)}")
    # Calculate a new residual
    residual = Y - model.predict(X)
    print("Residual is updated\n")

# Any relationship between the final residual and the unused variables?
print("Making scatter plot: age_of_roof vs final residual")
fig, ax = plt.subplots()
ax.scatter(X_basic[:, 3], residual, marker="+")
fig.savefig("ResidualRoof.png")

print("Making a scatter plot: miles_from_school vs final residual")
fig, ax = plt.subplots()
ax.scatter(X_basic[:, 4], residual, marker="+")
fig.savefig("ResidualMiles.png")
