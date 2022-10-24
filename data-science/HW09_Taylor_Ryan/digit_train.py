import pickle as pkl
from sklearn.model_selection import GridSearchCV
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from time import perf_counter
import numpy as np
from keras.datasets import mnist


def show_stats(cv_results):
    for params, mean_score in zip(cv_results["params"], cv_results["mean_test_score"]):
        print(f"{params} : Mean accuracy={mean_score*100:.2f}%")


# Read in the MNIST Training DAta
d = 28 * 28
(X_train, y_train), (_, _) = mnist.load_data()
X_train = X_train.reshape((-1, d))
n = X_train.shape[0]

# Make a dictionary with all the parameter values you want to test
param_grid = {
    "metric": ["euclidean", "manhattan"],
    "n_neighbors": [1, 3, 5, 7],
    "weights": ["uniform", "distance"],
}

# Create a KNN classifier
knn = KNeighborsClassifier()

# Create a GridSearchCV to determine the best values for the parameters
grid_searcher = GridSearchCV(knn, param_grid, cv=4, verbose=3)

# Run it
start = perf_counter()
grid_searcher.fit(X_train, y_train)
end = perf_counter()
print(f"Took {perf_counter() - start:.1f} seconds")

# List out the combinations and their scores
show_stats(grid_searcher.cv_results_)

# Get the best values
best_combo_index = grid_searcher.cv_results_["rank_test_score"].argmin()
best_params = grid_searcher.cv_results_["params"][best_combo_index]

print(f"Best parameters: {best_params}")

# Create a new classifier with the best hyperparameters
classifier = KNeighborsClassifier(**best_params)

# Fit to training data
classifier.fit(X_train, y_train)

# Do predictions for the training data, and print the accuracy
y_pred = classifier.predict(X_train)
print(f"Accuracy: {accuracy_score(y_train, y_pred):.3f}")

# Write the classifier out to a pickle file
with open("knn_model.pkl", "wb") as f:
    pkl.dump(classifier, f)
print("Wrote knn_model.pkl")
