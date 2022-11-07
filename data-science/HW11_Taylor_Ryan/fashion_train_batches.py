from keras.datasets import fashion_mnist
import numpy as np
import torch
import torch.optim as optim
import torch.nn as nn
import FashNet
from time import perf_counter
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Constants
WEIGHT_PATH = "weights.pt"
PLOT_PATH = "learning.png"
IN_D = 28 * 28
OUT_D = 10
MAX_ITERATIONS = 501
BATCH_SIZE = 100

# Read in training data
## Your code here

# How many samples are we training on?
n = ## Your code here

# Make each image into a long vector with range 0 to 1.0
## Your code here

# Convert to pytorch tensors
## Your code here

# Create the model with randomly initialized weights and biases
model = FashNet.FashNet(IN_D, OUT_D)

# List the parameters for each layer
print("Model parameters:")
total_params = 0
for name, param in model.named_parameters():
    # We only care about the parameters we can train
    if param.requires_grad:

        # What are the dimensions of param.data?
        the_size = list(param.data.size())
        print(f"\t{name}:{list(the_size)}")

        # How many numbers are in param.data?
        layer_sum = 1
        for s in the_size:
            layer_sum *= s
        total_params += layer_sum
print(f"Total parameters: {total_params:,}")

# Create an ADAM optimizer for model(learning rate = 0.0004)
## Your code here

# Use cross entropy as the loss to optimize
## Your code here

print("Training:")

# Note the time training started
t1 = perf_counter()

# Create arrays to hold diagnostic data
loss_log = np.zeros(MAX_ITERATIONS)
accuracy_log = np.zeros(MAX_ITERATIONS)

# Start training
for i in range(MAX_ITERATIONS):
    # Will be doing backpropagation (put model in training mode)
    ## Your code here

    # Make a random permutation of the numbers 1 through n-1
    ## Your code here

    # Step through each BATCH_SIZE chuck of the permuation
    for j in range(0, n, BATCH_SIZE):
        indices = ## Your code here

        # Make small tensors of the selected rows of the
        # training data set
        X_batch = ## Your code here
        y_batch = ## Your code here

        # For each image, make a vector of 10 "probabilities"
        ## Your code here

        # Compute the cross-entropy loss
        ## Your code here

        # Do a step of gradient descent
        ## Your code here

    # Get stats from last batch
    ## Your code here

    # Compute accuracy
    ## Your code here

    # Every 50th iterations, print some diagnostics
    if i % 50 == 0:
        print(
            f"{i:4d}: loss: {loss_log[i]:>5f},  accuracy: {accuracy_log[i] * 100.0:>2.2f}%"
        )

print(f"Training took {perf_counter() - t1:.2f} seconds")

# Save out the model's state dictionary
torch.save(model.state_dict(), WEIGHT_PATH)
print(f"Wrote {WEIGHT_PATH}")

# Plot the cross entropy loss and accuracy vs iterations
fig, axs = plt.subplots(2, 1, figsize=(10, 8))
## Your code here

# Write out the plot
fig.savefig(PLOT_PATH)
