import pandas as pd
import matplotlib.pyplot as plt
import pymc as pm
import numpy as np
import arviz as az

# Read in the data
df = pd.read_csv("samples.csv")
n = len(df)

# Convert the timestamp to a datetime object
df["timestamp"] = pd.to_datetime(df["timestamp"])

# When is low tide?
starttime = df["timestamp"][0]

# Make seconds from lowtide using timestamps
seconds = (df["timestamp"] - starttime).dt.total_seconds()

# Get the fish counts as a numpy array
fish_counts = df["jellyfish_entering"].values

# How many seconds between lowtides?
period = 12.0 * 60.0 * 60.0

# Create a model
basic_model = pm.Model()
with basic_model:

    # Give priors for unknown model parameters
    magnitude = pm.Uniform("magnitude", lower=0, upper=200)
    sigma = pm.HalfNormal("sigma", sigma=12)

    # Create the model
    mu = magnitude * np.sin(2 * np.pi * seconds / period)
    likelihood = pm.Normal("likelihood", mu=mu, sigma=sigma, observed=fish_counts)

    # Make chains
    trace = pm.sample(2000, tune=500)

    # Find maximum a posteriori estimations
    map_magnitude = pm.find_MAP()["magnitude"]
    map_sigma = pm.find_MAP()["sigma"]

# Let the user know the MAP values
print(f"Based on these {n} measurements, the most likely explanation:")
print(
    f"\tWhen the current is moving fastest, {map_magnitude:.2f} jellyfish enter the bay in 15 min."
)
print(f"\tExpected residual? Normal with mean 0 and std of {map_sigma:.2f} jellyfish.")

# Do a contour/density plot
fig, ax = plt.subplots(1, 1, figsize=(7, 7))
posterior = trace["posterior"]
p_magnitude = posterior["magnitude"]
p_sigma = posterior["sigma"]
ax = az.plot_kde(
    p_magnitude,
    p_sigma,
    contourf_kwargs={"cmap": "Blues"},
)
ax.set_xlabel("magnitude")
ax.set_ylabel("$\sigma$")
ax.set_title("Posterior density of magnitude and $\sigma$")

ax.vlines(
    map_magnitude,
    map_sigma - 4,
    map_sigma + 4,
    linestyle="dashed",
    color="k",
)
ax.hlines(
    map_sigma,
    map_magnitude - 10,
    map_magnitude + 10,
    linestyle="dashed",
    color="k",
)

fig.savefig("pdf.png")

# Plot your function and confidence against the observed data
fig, ax = plt.subplots(figsize=(8, 6))
hours = seconds / 3600
# observed data
ax.plot(
    hours,
    fish_counts,
    "k+",
    label="observed",
)
# predictions
model = map_magnitude * np.sin(2 * np.pi * seconds / period)
ax.plot(
    hours,
    model,
    "r--",
    lw="0.5",
    label="prediction",
)
ax.set_xlabel("Hours since low tide")
ax.set_ylabel("Jellyfish entering bay over 15 minutes")
ax.set_title("Model fit to jellyfish data")
# Plot the 95% confidence interval
ax.plot(hours, model + 2 * map_sigma, "g--", lw="0.5", label="95% Confidence")
ax.plot(hours, model - 2 * map_sigma, "g--", lw="0.5")
ax.legend()
fig.savefig("jellyfish.png")
