import pandas as pd
import numpy as np
from numpy.linalg import svd
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import confusion_matrix, accuracy_score
import pickle
from time import perf_counter

# How many dimension will we actually use for the SVM?
k = 11

# Read in the data
df = pd.read_csv("train_breast.csv", index_col="id")
X_train = ## Your code here
y_train = ## Your code here
print(f"X shape = {X_train.shape}, y shape={y_train.shape}")
n = len(df)

# Scale it
## Your code here
X_train_scaled = ## Your code here

# Get the covariance matrix
C = ## Your code here

# Do singular value decomposition
## Your code here
W = ## Your code here

# Reduce the data to k dimensions
X_train_scaled = ## Your code here

# Do a grid search for hyperparameters
parameters = ## Your code here
classifier = ## Your code here
## Your code here

# What were the best parameters?
svc_params = ## Your code here
print(f"Best parameters = {svc_params}")

# Make a classifier using the best parameters
svc_classifier = ## Your code here

t0 = perf_counter()
# Fit the classifier with all the training dta
## Your code here
print(
    f"Fitting took {perf_counter() - t0:.6f} seconds with d={X_train_scaled.shape[1]} input."
)

# Save out the scaler, W, and the classifier
with open("pca_classifier.pkl", "wb") as f:
    pickle.dump(scaler, f)
    pickle.dump(W, f)
    pickle.dump(svc_classifier, f)

# Do predictions for the training data
y_pred = ## Your code here

# Show the accuracy for the training data
accuracy = ## Your code here
print(f"Accuracy on training data = {accuracy * 100.0:.2f}%")

# Make a confusion matrix
cm = ## Your code here
print(f"Confusion on training data: \n{cm}")
