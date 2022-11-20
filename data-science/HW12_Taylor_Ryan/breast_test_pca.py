import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import pickle

# Read in the testing data
## Your code here

# Read in the scaler, W, and the SVC
## Your code here
    scaler = ## Your code here
    W = ## Your code here
    classifier = ## Your code here

# Scale the input data
X_test_scaled = ## Your code here

# Reduce dimension using PCA
X_test_scaled = ## Your code here

# Do a prediction using the test data
y_pred = ## Your code here

# Show the accuracy
accuracy = ## Your code here
print(f"Accuracy on testing data = {accuracy * 100.0:.2f}%")

# Make a confusion matrix
cm = ## Your code here
print(f"Confusion on testing data: \n{cm}")

# Make it into a pretty plot
fig, ax = plt.subplots(figsize=(9, 7))
## Your code here
fig.savefig("test_confusion_pca.png")
print("Wrote test_confusion_pca.png")
