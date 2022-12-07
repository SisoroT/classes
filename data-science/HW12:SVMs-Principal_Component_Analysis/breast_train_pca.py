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
X_train = df.drop("diagnosis", axis=1)
y_train = df["diagnosis"]
print(f"X shape = {X_train.shape}, y shape={y_train.shape}")
n = len(df)

# Scale it
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)

# Get the covariance matrix
C = np.cov(X_train_scaled.T)

# Do singular value decomposition
U, S, V = svd(C)
W = U[:, :k]

# Reduce the data to k dimensions
X_train_scaled = X_train_scaled @ W

# Do a grid search for hyperparameters
parameters = {
    "C": [0.5, 1.0, 2.0, 3.0, 4.0],
    "kernel": ["linear", "rbf", "poly", "sigmoid"],
}
classifier = SVC()
grid_search = GridSearchCV(estimator=classifier, param_grid=parameters, cv=5)
grid_search.fit(X_train_scaled, y_train)

# What were the best parameters?
svc_params = grid_search.best_params_
print(f"Best parameters = {svc_params}")

# Make a classifier using the best parameters
svc_classifier = SVC(**svc_params)

t0 = perf_counter()
# Fit the classifier with all the training dta
svc_classifier.fit(X_train_scaled, y_train)
print(
    f"Fitting took {perf_counter() - t0:.6f} seconds with d={X_train_scaled.shape[1]} input."
)

# Save out the scaler, W, and the classifier
with open("pca_classifier.pkl", "wb") as f:
    pickle.dump(scaler, f)
    pickle.dump(W, f)
    pickle.dump(svc_classifier, f)

# Do predictions for the training data
y_pred = svc_classifier.predict(X_train_scaled)

# Show the accuracy for the training data
accuracy = accuracy_score(y_train, y_pred)
print(f"Accuracy on training data = {accuracy * 100.0:.2f}%")

# Make a confusion matrix
cm = confusion_matrix(y_train, y_pred)
print(f"Confusion on training data: \n{cm}")
