import pickle as pkl
import faiss
import numpy as np
from keras.datasets import mnist
import sys

if len(sys.argv) != 2:
    print(f"Usage: {sys.argv[0]} (exact | approximate)")
    exit(-1)

# Read in the MNIST training data
## Your code here

if sys.argv[1] == "exact":
    index = ## Your code here
    print("Using IndexFlatL2 for true KNN")
    path_prefix = "exact"
else:
    ## Your code here
    index = ## Your code here
    print("Using HNSW/IVFPQ for approximate KNN")
    path_prefix = "approx"

# Train and add with the training data
## Your code here

print(f"Index has {index.ntotal} data points.")

path = f"{path_prefix}.faiss"
# Write out the index and the classes it indexes
## Your code here
print(f"Wrote index to values.pkl and {path}")
