import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

# Load the data file
mat = loadmat("data_breastcancer.mat")
# Number of samples
n = mat["data"]["n"][0][0][0][0]
# Number of attributes
d = mat["data"]["d"][0][0][0][0]
# Input data
X = mat["data"]["X"][0][0]
# Output labels
Y = mat["data"]["Y"][0][0].flatten()


def get_accuracy(fraction):
    """Define a function that takes a fraction of the training
    set and returns the accuracy score on the test set using
    logistic regression with no regularization (λ = 0)"""

    # Split the data into training and test sets with 2/3 for
    # training and 1/3 for testing using random_state as an argument
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        Y,
        train_size=fraction * 2 / 3,
        random_state=np.random.randint(100),
    )

    # Create and fit a logistic regression model with no regularization (λ = 0)
    model = LogisticRegression(C=1e9)  # C is the inverse of λ
    model.fit(X_train, y_train)

    # Predict the labels on the test set and compute the accuracy score
    y_pred = model.predict(X_test)
    score = accuracy_score(y_test, y_pred)

    # Return the accuracy score
    return score


# Define a list of fractions [.01, .02, .03, .125, .625, 1] and an
# empty list to store the average accuracy scores
fractions = [0.01, 0.02, 0.03, 0.125, 0.625, 1]
avg_scores = []

# For each fraction in the list:
for fraction in fractions:

    # Create an empty temporary list to store the
    # accuracy scores for each random split
    temp_scores = []

    # Repeat 5 times:
    for _ in range(5):

        # Call the function defined earlier with the fraction and
        # append the accuracy score to the temporary list
        score = get_accuracy(fraction)
        temp_scores.append(score)

    # Compute the mean of the temporary list and
    # append it to the average accuracy list
    avg_score = np.mean(temp_scores)
    avg_scores.append(avg_score)

# Plot a line graph with fractions as x-axis
# and average accuracy scores as y-axis
fig, ax = plt.subplots()
ax.plot(avg_scores, fractions)
ax.set_xlabel("Average accuracy score")
ax.set_ylabel("Size of training set")
ax.set_title("Learning curve of logistic regression")
plt.savefig("logreg.png")
# plt.show()
