import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, recall_score, precision_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pickle
import logging

# Configure logger
## Your code here
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(levelname)s@%(asctime)s: %(message)s", datefmt="%H:%M:%S"
)

# Read in test data
## Your code here
df = pd.read_csv("test.csv")
X_basic = df.values[:, :-1]
Y = df.values[:, -1]

# Read in model
## Your code here
with open("classifier.pkl", "rb") as f:
    model = pickle.load(f)

# Scale X
## Your code here
scaler = StandardScaler()
X = scaler.fit_transform(X_basic)

# Check accuracy on test data
## Your code here
test_accuracy = model.score(X, Y)
print(f"Test Accuracy = {test_accuracy}")

# Show confusion matrix
## Your code here
pred = model.predict(X)
cm = confusion_matrix(Y, pred)
print(f"Confusion matrix = \n{cm}")

# Try a bunch of thresholds
threshold = 0.0
best_f1 = -1.0
thresholds = []
recall_scores = []
precision_scores = []
f1_scores = []
while threshold <= 1.0:
    thresholds.append(threshold)
    ## Your code here
    pred = model.predict_proba(X)[:, 1] > threshold
    recall = recall_score(Y, pred)
    precision = precision_score(Y, pred)
    f1 = 2 * (precision * recall) / (precision + recall)

    recall_scores.append(recall)
    precision_scores.append(precision)
    f1_scores.append(f1)
    logger.info(
        f"Threshold={threshold:.3f} Accuracy={accuracy:.3f} Recall={recall:.2f} Precision={precision:.2f} F1 = {f1:.3f}"
    )
    threshold += 0.02

# Make a confusion matrix for the best threshold
## Your code here
best_threshold = thresholds[np.argmax(f1_scores)]
pred = model.predict_proba(X)[:, 1] > best_threshold
cm = confusion_matrix(Y, pred)
print(f"Confusion matrix = \n{cm}")

# Plot recall, precision, and F1 vs Threshold
fig, ax = plt.subplots()
ax.plot(thresholds, recall_scores, "b", label="Recall")
ax.plot(thresholds, precision_scores, "g", label="Precision", color="g")
ax.plot(thresholds, f1_scores, "r", label="F1", color="r")
ax.vlines(best_threshold, 0, 1, "r", linewidth=0.5, linestyle="dashed")
ax.set_xlabel("Threshold")
ax.legend()
fig.savefig("threshold.png")
