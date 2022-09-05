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

# Limit interations
max_steps = 1000

# Get the arg and read in the spreadsheet
infilename = sys.argv[1]
X, Y, labels = util.read_excel_data(infilename)
n, d = X.shape
print(f"Read {n} rows, {d - 1} features from '{infilename}'.")

# Get the mean and standard deviation for each column
## Your code here

# Don't mess with the first column (the 1s)
## Your code here

# Standardize X to be X' 
Xp = ## Your code here

# First guess for B is "all coefficents are zero"
B = ## Your code here

# Create a numpy array to record avg error for each step
errors = ## Your code here

for i in range(max_steps):
 
    # Compute the gradient 
    ## Your code here

    # Compute a new B (use `t`)
    ## Your code here

    # Figure out the average squared error using the new B
    ## Your code here

    # Store it in `errors``
    ## Your code here

    # Check to see if we have converged
    if ## Your code here:
        break

print(f"Took {i} iterations to converge")

# "Unstandardize" the coefficients
## Your code here

# Show the result
print(util.format_prediction(B, labels))

# Get the R2 score
R2 = util.score(B, X, Y)
print(f"R2 = {R2:f}")

# Draw a graph
fig1 = plt.figure(1, (4.5, 4.5))
## Your code ehre
fig1.savefig("err.png")
