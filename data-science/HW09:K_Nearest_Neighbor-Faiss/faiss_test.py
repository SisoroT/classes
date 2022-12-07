import pickle as pkl
import faiss
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from time import perf_counter
from keras.datasets import mnist
import numpy as np
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} (exact | approximate)")
    exit(-1)

K = 3

# Read in the MNIST test data
## Your code here

# Read the values for the index from values.pkl
## Your code here

if sys.argv[1] == "exact":
    index_path = "exact.faiss"
    plot_path = "exact_confusion.png"
else:
    index_path = "approx.faiss"
    plot_path = "approx_confusion.png"
# Read in the index itself
index = ## Your code here
print(f"Read {index_path}: Index has {index.ntotal} data points.")

start = perf_counter()

# Do prediction (This is the hardest part)

print(f"Inference: elapsed time = {perf_counter() - start:.2f} seconds")

# Print the accuracy
## Your code here

# Create a confusion matrix
cm = ## Your code here
print(f"Confusion: \n{cm}")

# Save it to a display
fig, ax = plt.subplots()
## Your code here
ax.set_title(f"MNIST with Faiss (k={K})")
fig.savefig(plot_path)
print(f"Wrote {plot_path}")
