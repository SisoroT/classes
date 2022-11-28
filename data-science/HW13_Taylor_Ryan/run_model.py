import pandas as pd
import matplotlib.pyplot as plt
import pymc as pm
import numpy as np
import arviz as az

# Read in the data
df = ## Your code here
n = ## Your code here

# When is low tide?
starttime = ## Your code here

# Make seconds from lowtide using timestamps
seconds = ## Your code here

# Get the fish counts as a numpy array
fish_counts = ## Your code here

# How many seconds between lowtides?
period = 12.0 * 60.0 * 60.0

# Create a model
basic_model = ## Your code here
with basic_model:

    # Give priors for unknown model parameters
    magnitude = ## Your code here
    sigma = ## Your code here

    # Create the model
    ## Your code here

    # Make chains
    trace = ## Your code here

    # Find maximum a posteriori estimations
    map_magnitude = ## Your code here
    map_sigma = ## Your code here

# Let the user know the MAP values
print(f"Based on these {n} measurements, the most likely explanation:")
print(
    f"\tWhen the current is moving fastest, {map_magnitude:.2f} jellyfish enter the bay in 15 min."
)
print(f"\tExpected residual? Normal with mean 0 and std of {map_sigma:.2f} jellyfish.")

# Do a contour/density plot
fig, ax = plt.subplots(1, 1, figsize=(7, 7))
## Your code here
fig.savefig("pdf.png")

# Plot your function and confidence against the observed data
fig, ax = plt.subplots(figsize=(8, 6))
## Your code here
fig.savefig("jellyfish.png")
