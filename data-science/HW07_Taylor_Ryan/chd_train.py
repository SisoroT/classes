import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.preprocessing import StandardScaler

# Read the training data
print("Reading input...")
df = pd.read_csv("train.csv")
X = df.values[:, :-1]
Y = df.values[:, -1]

# Standardize X
print("Scaling...")
scaler = StandardScaler().fit(X)
X_scaled = scaler.transform(X)

# Do logistic regression
print("Fitting...")
logreg = LogisticRegression()
logreg.fit(X_scaled, Y)

# Get the accuracy on the training data
train_accuracy = logreg.score(X_scaled, Y)
print(f"Training accuracy = {train_accuracy}")

# Write out the scaler and logistic regression objects into a pickle file
pickle_path = "classifier.pkl"
print(f"Writing scaling and logistic regression model to {pickle_path}...")
with open(pickle_path, "wb") as f:
    pickle.dump((scaler, logreg), f)
