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

# Read in training data
(X_train, y_train_np), (_, _) = fashion_mnist.load_data()

# How many samples are we training on?
n = X_train.shape[0]

# Make each image into a long vector with range 0 to 1.0
X_train = X_train.reshape(-1, IN_D).astype(np.float32) / 255.0

# Convert to pytorch tensors
X_train = torch.from_numpy(X_train)
y_train = torch.from_numpy(y_train_np)

# Create the model with randomly initialized weights and biases
model = FashNet.FashNet(IN_D, OUT_D)

# List the parameters for each layer
print("Model parameters:")
total_params = 0

# Step through the layers
for name, param in model.named_parameters():

    # We are only interested in the ones
    # we can learn
    if param.requires_grad:

        # What are the dimensions of the para.data tensor?
        the_size = list(param.data.size())
        print(f"\t{name}:{list(the_size)}")

        # Calculate how many weights are in this
        # tensor
        layer_sum = 1
        for s in the_size:
            layer_sum *= s

        # Add it to the total
        total_params += layer_sum

# Display the total
print(f"Total parameters: {total_params:,}")

# Create an ADAM optimizer (learning rate = 0.01)
optimizer = optim.Adam(model.parameters(), lr=0.01)

# Use cross entropy as the loss to optimize
loss_fn = nn.CrossEntropyLoss()

print("Training:")

# Note the time training started
t1 = perf_counter()

# Create arrays to hold diagnostic data
loss_log = np.zeros(MAX_ITERATIONS)
accuracy_log = np.zeros(MAX_ITERATIONS)

# Start training
for i in range(MAX_ITERATIONS):

    # Will be doing backpropagation (put the model in "train" mode)
    model.train()

    # For each image, make a vector of 10 "probabilities"
    y_pred = model(X_train)

    # Compute the cross-entropy loss
    loss = loss_fn(y_pred, y_train)

    # Do a step of gradient descent
    optimizer.zero_grad()
    loss.backward()
    optimizer.step()

    loss_log[i] = loss.item()

    # Compute accuracy
    accuracy = (y_pred.argmax(dim=1) == y_train).float().mean()

    accuracy_log[i] = accuracy

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
axs[0].plot(loss_log)
axs[0].set_ylabel("Cross Entropy Loss")
axs[0].set_title("Training Loss")
axs[0].yaxis.set_major_formatter(mtick.FormatStrFormatter("%.1f"))

axs[1].plot(accuracy_log)
axs[1].set_ylabel("Accuracy")
axs[1].set_xlabel("Iteration")
axs[1].set_title("Training Accuracy")
axs[1].yaxis.set_major_formatter(mtick.FormatStrFormatter("%.2f"))

# Write out the plot
fig.savefig(PLOT_PATH)
