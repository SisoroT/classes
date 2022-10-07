import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.preprocessing import StandardScaler

# Read the training data
print("Reading input...")
## Your code here
df = pd.read_csv("train.csv")
X_basic = df.values[:, :-1]
Y = df.values[:, -1]

print("Scaling...")
## Your code here
X = StandardScaler().fit_transform(X_basic)

print("Fitting...")
## Your code herer
logreg = LogisticRegression()
logreg.fit(X, Y)

# Get the accuracy on the training data
## Your code here
train_accuracy = logreg.score(X, Y)
print(f"Training accuracy = {train_accuracy}")

# Write out the scaler and logisticregression objects into a pickle file
pickle_path = "classifier.pkl"
print(f"Writing scaling and logistic regression model to {pickle_path}...")
## Your code here
with open(pickle_path, "wb") as f:
    pickle.dump((StandardScaler(), logreg), f)
