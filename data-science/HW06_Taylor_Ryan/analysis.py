import pandas as pd
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
X = poly.fit_transform(X_basic)
labels = poly.get_feature_names(labels_basic)
rows, cols = X.shape

# Prepare for loop
residual = Y

# We always need the column of zeros to
# include the intercept
feature_indices = [0]

model = LinearRegression()
print("First time through: using original price data as the residual")

while len(feature_indices) < 3:
    p_vals = []

    # Calculate the p-value of the Pearson correlation
    # between each input and the current residual
    for i in range(1, cols):
        p_vals.append((pearsonr(X[:, i], residual)[1], i))

    # Sort p-values in ascending order
    sorted_p_vals = sorted(p_vals)

    for i in range(cols - 1):
        p_value, idx = sorted_p_vals[i]
        print(f'\t"{labels[idx]}" vs residual: p-value={p_value}')

    # Add the input with the lowest p-value to the list of
    # inputs you are going to actually use
    best_idx = sorted_p_vals[0][1]
    feature_indices.append(best_idx)

    # List off the attributes we will use to create the next residual
    print("**** Fitting with [", end="")
    for idx in feature_indices:
        print(f'"{labels[idx]}" ', end="")
    print("] ****")

    # Fit the model with the current set of inputs
    sub_X = X[:, feature_indices]
    model.fit(sub_X, Y)

    # Print the R2 score
    print(f"R2: {model.score(sub_X, Y)}")

    # Update the residual for the next time
    print("Residual is updated")
    residual = Y - model.predict(sub_X)

# Any relationship between the final residual and the unused variables?
print("Making scatter plot: age_of_roof vs final residual")
fig, ax = plt.subplots()
ax.scatter(X_basic[:, 3], residual, marker="+")
fig.savefig("ResidualRoof.png")

print("Making a scatter plot: miles_from_school vs final residual")
fig, ax = plt.subplots()
ax.scatter(X_basic[:, 4], residual, marker="+")
fig.savefig("ResidualMiles.png")
