import numpy as np
import pandas as pd
import sys
import util
import matplotlib.pyplot as plt

# Check the command line
if len(sys.argv) != 2:
    print(f"{sys.argv[0]} <xlsx>")
    exit(1)

# Learning rate
t = 0.001

# Limit iterations
max_steps = 1000

# Get the arg and read in the spreadsheet
infilename = sys.argv[1]
X, Y, labels = util.read_excel_data(infilename)
rows, cols = X.shape
print(f"Read {rows} rows, {cols - 1} features from '{infilename}'.")

# Get the mean and standard deviation for each column
means = X.mean(axis=0)
std = X.std(axis=0)

# Don't mess with the first column (the 1s)
means[0] = 0.0
std[0] = 1.0

# Standardize X to be X'
Xp = (X - means) / std

# First guess for B is "all coefficients are zero"
B = np.zeros(cols)

# Create a numpy array to record avg error for each step
errors = np.zeros(max_steps)

for i in range(max_steps):
    # Compute the gradient
    residuals_inv = Xp @ B - Y
    gradient = Xp.T @ residuals_inv

    # Compute a new B (use `t`)
    B = B - t * gradient

    # Figure out the average squared error using the new B
    prediction = Xp @ B

    # Store it in `errors`
    errors[i] = np.mean((prediction - Y) ** 2)

    # Check to see if we have converged
    if np.linalg.norm(gradient) < 10**-2:
        break

print(f"Took {i} iterations to converge")

# "Unstandardize" the coefficients
B[1:] = B[1:] / std[1:]
B[0] = B[0] - np.sum(B[1:] * means[1:])

# Show the result
print(util.format_prediction(B, labels))

# Get the R2 score
R2 = util.score(B, X, Y)
print(f"R2 = {R2:f}")

# Draw a graph
fig, ax = plt.subplots(figsize=(4.5, 4.5))
ax.set_title("Convergence")
ax.set_xlabel("Iterations")
ax.set_ylabel("Mean Squared Error")
ax.set_yscale("log")
ax.set_xscale("log")
ax.plot(errors[:i])
plt.savefig("err.png")
