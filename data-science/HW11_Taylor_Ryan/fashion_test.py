from keras.datasets import fashion_mnist
import numpy as np
import torch
import FashNet
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix, accuracy_score

# Constants
WEIGHT_PATH = "weights.pt"
IN_D = 28 * 28
OUT_D = 10

# Read in test data
(_, _), (X_test, y_test_np) =  ## Your code here
print(f"Input: {X_test.shape}")

# How many samples are we testing on?
n = ## Your code here

# Make each image into a long vector with range 0 to 1.0
X_test = ## Your code here

# Convert to pytorch tensors
## Your code here

# Create the model
model = ## Your code here

# Read in the weights created in fashion_train.py
model.load_state_dict(torch.load("weights.pt"))

# We are doing inference (no need for backpropagation)
# Put the model in eval mode
## Your code here

# Make For each image, make a vector of 10
# "probabilities" -- one for each class
y_pred = ## Your code here

# Convert back to numpy so we can do stats on it
y_pred = y_pred.detach().numpy()

# Take the most likely for each image
predictions = ## Your code here

# Get the accuracy
accuracy = ## Your code here
print(f"Accuracy on test data: {accuracy * 100.0:>2.2f}%")

# Make a confusion matrix
cm = ## Your code here
print(f"Confusion: \n{cm}")

# Make it into a pretty plot
fig, ax = plt.subplots(figsize=(9, 7))
ax.set_title("Fashion Confusion Matrix")
## Your code here
fig.savefig("confusion.png")
print("Wrote confusion.png")
