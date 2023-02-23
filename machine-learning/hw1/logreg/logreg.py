import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from sklearn.model_selection import train_test_split


def load_data():
    """
    Load the Bupa liver disorders dataset.

    Returns:
        X (numpy.ndarray): Input data.
        Y (numpy.ndarray): Target labels for input data.
    """
    mat = loadmat("data_breastcancer.mat")
    # Number of samples
    n = mat["data"]["n"][0][0][0][0]
    # Number of attributes
    d = mat["data"]["d"][0][0][0][0]
    # Input data
    X = mat["data"]["X"][0][0]
    # Output labels
    Y = mat["data"]["Y"][0][0].flatten()
    return X, Y


def sigmoid(x):
    """Define a sigmoid function that takes
    an input x and returns 1 / (1 + exp(-x))
    """
    return 1 / (1 + np.exp(-x))


def get_accuracy(fraction):
    """Define a function that takes a fraction of the training set and returns
    the accuracy score on the test set using logistic regression from
    scratch with no regularization (λ = 0)
    """
    # Split the data into training and test sets
    # with 2/3 for training and 1/3 for testing
    X_train, X_test, y_train, y_test = train_test_split(
        X,
        Y,
        train_size=fraction * 2 / 3,
    )

    # Add a column of ones to the training and test sets for the intercept term
    X_train = np.c_[np.ones(X_train.shape[0]), X_train]
    X_test = np.c_[np.ones(X_test.shape[0]), X_test]

    # Initialize the weight vector with random values
    weight = np.random.randn(X_train.shape[1])

    # Set the learning rate and the maximum number of iterations
    alpha = 0.01
    max_iter = 1000

    # Repeat until convergence or a maximum number of iterations:
    for _ in range(max_iter):
        # For each training example:
        for x, y in zip(X_train, y_train):
            # Compute the predicted probability
            pred = sigmoid(weight.dot(x))
            # Compute the error
            error = y - pred
            # Update the weight vector
            weight = weight + alpha * error * x

    # Predict the labels on the test set by computing the predicted
    # probabilities and assigning them to class 1 if >=0.5 or class 0 otherwise
    y_pred = sigmoid(X_test.dot(weight)) >= 0.5

    # Compute and return the accuracy score by comparing the
    # predicted labels with the true labels
    score = np.mean(y_pred == y_test)
    return score


if __name__ == "__main__":
    # Load the data
    X, Y = load_data()
    # Define a list of fractions [.01, .02, .03, .125, .625, 1] and an empty
    # list to store the average accuracy scores
    fractions = [0.01, 0.02, 0.03, 0.125, 0.625, 1]
    avg_scores = []

    # For each fraction in the list:
    for fraction in fractions:
        # Create an empty temporary list to storethe
        # accuracy scores for each random split
        temp_scores = []

        # Repeat 5 times:
        for _ in range(5):

            # Call the function defined earlier with the fraction
            # and append the accuracy score to the temporary list
            score = get_accuracy(fraction)
            temp_scores.append(score)

        # Compute the mean of the temporary list and
        # append it to the average accuracy list
        avg_score = np.mean(temp_scores)
        avg_scores.append(avg_score)

    # Plot line graph with fractions on x-axis and accuracy scores on y-axis
    fig, ax = plt.subplots()
    ax.plot(fractions, avg_scores, marker="o")
    ax.set_xlabel("Size of training set")
    ax.set_ylabel("Average accuracy score")
    ax.set_title("Learning curve of logistic regression")
    # plt.savefig("logreg.png")
    plt.show()
