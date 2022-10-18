import pickle as pkl
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from time import perf_counter
import numpy as np
from keras.datasets import mnist


def show_stats(cv_results):
    ## Your code here

# Read in the MNIST Training DAta
d = 28 * 28
(X_train, y_train), (_, _) = mnist.load_data()
X_train = X_train.reshape((-1, d))
n = X_train.shape[0]

# Make a dictionary with all the parameter values you want to test
## Your code here

# Create a KNN classifier
## Your code here

# Create a GridSearchCV to determine the best values for the parameters
grid_searcher = ## Your code here

# Run it
start = perf_counter()
## Your code here
print(f"Took {perf_counter() - start:.1f} seconds")

# List out the combinations and their scores
show_stats(grid_searcher.cv_results_)

# Get the best values
best_combo_index = ## Your code here
best_params = ## Your code here

print(f"Best parameters: {best_params}")

# Create a new classifier with the best hyperparameters
classifier = ## Your code here

# Fit to training data
## Your code here

# Do predictions for the training data, and print the accuracy
## Your code here

# Write the classifier out to a pickle file
with open("knn_model.pkl", "wb") as f:
    pkl.dump(classifier, f)
print("Wrote knn_model.pkl")
