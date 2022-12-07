import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, recall_score, precision_score
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import pickle
import logging

# Configure logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler()
formatter = logging.Formatter(
    "%(levelname)s@%(asctime)s: %(message)s", datefmt="%H:%M:%S"
)
handler.setFormatter(formatter)
logger.addHandler(handler)

# Read in test data
df = pd.read_csv("test.csv")
X = df.values[:, :-1]
Y = df.values[:, -1]

# Read in model
with open("classifier.pkl", "rb") as f:
    scaler, logreg = pickle.load(f)

# Scale X
X_scaled = scaler.transform(X)

# Check accuracy on test data
test_accuracy = logreg.score(X_scaled, Y)
print(f"Test Accuracy = {test_accuracy}")

# Show confusion matrix
pred = logreg.predict(X_scaled)
cm = confusion_matrix(Y, pred)
print(f"Confusion matrix = \n{cm}")

# Try a bunch of thresholds
threshold = 0.0
best_f1 = -1.0
thresholds = []
recall_scores = []
precision_scores = []
f1_scores = []
best_threshold = 0.0

while threshold <= 1.0:
    thresholds.append(threshold)
    pred = logreg.predict_proba(X_scaled)[:, 1] > threshold

    # calculate metrics
    accuracy = logreg.score(X_scaled, pred)
    recall = recall_score(Y, pred)
    precision = precision_score(Y, pred, zero_division=1)
    f1 = 2 * (precision * recall) / (precision + recall)

    # add metrics to lists
    recall_scores.append(recall)
    precision_scores.append(precision)
    f1_scores.append(f1)

    # update best f1 score
    if f1 > best_f1:
        best_f1 = f1
        best_threshold = threshold

    logger.info(
        f"Threshold={threshold:.3f} Accuracy={accuracy:.3f} Recall={recall:.2f} Precision={precision:.2f} F1 = {f1:.3f}"
    )
    threshold += 0.02

# Make a confusion matrix for the best threshold
pred = logreg.predict_proba(X_scaled)[:, 1] > best_threshold
cm = confusion_matrix(Y, pred)
print(f"Confusion matrix with {best_threshold:.3f} threshold: \n{cm}")


# Plot recall, precision, and F1 vs Threshold
fig, ax = plt.subplots()
ax.plot(thresholds, recall_scores, "b", label="Recall")
ax.plot(thresholds, precision_scores, label="Precision", color="g")
ax.plot(thresholds, f1_scores, label="F1", color="r")
ax.vlines(best_threshold, 0, 1, color="r", linewidth=0.5, linestyle="dashed")
ax.set_xlabel("Threshold")
ax.legend()
fig.savefig("threshold.png")
