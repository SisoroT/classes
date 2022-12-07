import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import ConfusionMatrixDisplay, confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
import pickle

# Read in the testing data
df = pd.read_csv("test_breast.csv", index_col="id")
X_test = df.drop("diagnosis", axis=1)
y_test = df["diagnosis"]
print(f"X shape = {X_test.shape}, y shape={y_test.shape}")

# Read in the scaler, W, and the SVC
with open("pca_classifier.pkl", "rb") as f:
    scaler = pickle.load(f)
    W = pickle.load(f)
    classifier = pickle.load(f)

# Scale the input data
X_test_scaled = scaler.transform(X_test)

# Reduce dimension using PCA
X_test_scaled = X_test_scaled @ W

# Do a prediction using the test data
y_pred = classifier.predict(X_test_scaled)

# Show the accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy on testing data = {accuracy * 100.0:.2f}%")

# Make a confusion matrix
cm = confusion_matrix(y_test, y_pred)
print(f"Confusion on testing data: \n{cm}")

# Make it into a pretty plot
fig, ax = plt.subplots(figsize=(9, 7))
ax.set_title("Breast Cancer Confusion Matrix (testing data)")
disp = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=["Benign", "Malignant"],
)
disp.plot(ax=ax, cmap=plt.cm.Blues)
fig.savefig("test_confusion_pca.png")
print("Wrote test_confusion_pca.png")
