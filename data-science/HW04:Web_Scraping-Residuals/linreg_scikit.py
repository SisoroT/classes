import numpy as np
from sklearn.linear_model import LinearRegression
from scipy.stats import kstest, norm
import matplotlib.pyplot as plt
import sys
import util

# Check command line
if len(sys.argv) != 2:
    print(f"{sys.argv[0]} <xlsx>")
    exit(1)

# Read in the argument
infilename = sys.argv[1]

# Read the spreadsheet
X, Y, labels = util.read_excel_data(infilename)

rows, cols = X.shape
print(f"Read {rows} rows, {cols-1} features from '{infilename}'.")

# Don't need the intercept added -- X has column of 1s
lin_reg = LinearRegression(fit_intercept=False)

# Fit the model
lin_reg.fit(X, Y)

# Pretty print coefficients
print(util.format_prediction(lin_reg.coef_, labels))

# Get residual
residual = Y - lin_reg.predict(X)

# Make a histogram of the residual and save as "res_hist.png"
fig, ax = plt.subplots()
ax.hist(residual, bins=18)
ax.set_title("Residual Histogram")
ax.set_xlabel("Residual")
ax.set_ylabel("Density")

# format x axis to use K's instead of just thousands
ax.xaxis.set_major_formatter(lambda x, pos: f"${x/1000:.0f}K")

plt.savefig("res_hist.png")

# Do a Kolmogorov-Smirnov to see if the residual is normally
# distributed
ks_stat, p_value = kstest(residual, norm.cdf)
print(f"Kolmogorov-Smirnov: P-value = {p_value}")


# Calculate the standard deviation
variance = residual @ residual / (rows - cols - 1)
standard_deviation = np.sqrt(variance)
# standard_deviation = np.std(residual)

print(
    f"68% of predictions with this formula will be within ${standard_deviation:,.02f} of the actual price."
)
print(
    f"95% of predictions with this formula will be within ${2.0 * standard_deviation:,.02f} of the actual price."
)
