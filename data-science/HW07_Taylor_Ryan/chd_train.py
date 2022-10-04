import pandas as pd
from sklearn.linear_model import LogisticRegression
import pickle
from sklearn.preprocessing import StandardScaler

# Read the training data
print("Reading input...")
## Your code here

print("Scaling...")
## Your code here

print("Fitting...")
## Your code herer

# Get the accuracy on the training data
## Your code here
print(f"Training accuracy = {train_accuracy}")

# Write out the scaler and logisticregression objects into a pickle file
pickle_path = "classifier.pkl"
print(f"Writing scaling and logistic regression model to {pickle_path}...")
## Your code here
