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
    mat = loadmat("data_bupa.mat")
    # Input data
    X = mat["data"]["X"][0][0]
    # Output labels
    Y = mat["data"]["Y"][0][0].flatten()
    return X, Y


def decision_stump(X, Y, weights):
    """Finds the decision stump that minimizes the weighted error.

    Args:
        X (numpy.ndarray): Features matrix of shape (N, M).
        y (numpy.ndarray): Labels vector of shape (N,).
        w (numpy.ndarray): Weights vector of shape (N,).

    Returns:
        Tuple (j, c, d, error) representing the selected decision stump, where:
            - j: The feature index used by the decision stump.
            - c: The threshold value used by the decision stump.
            - d: The direction (+1 or -1) of the decision stump.
            - error: The weighted error rate of the decision stump.
    """
    best_feature = 0
    best_threshold = 0
    best_direction = 1
    best_error = float("inf")

    for feature in range(X.shape[1]):
        thresholds = np.unique(X[:, feature])
        for threshold in thresholds:
            for direction in [-1, 1]:
                # Compute predictions for the current feature, threshold, and direction
                y_pred = direction * np.ones(Y.shape)
                y_pred[X[:, feature] * direction < threshold * direction] = -1
                # Compute weighted classification error for the current classifier
                error = np.sum(weights[y_pred != Y])
                # Update best classifier if the current one has lower error
                if error < best_error:
                    best_feature = feature
                    best_threshold = threshold
                    best_direction = direction
                    best_error = error
    return best_feature, best_threshold, best_direction, best_error


def adaboost(X, Y, num_iterations):
    """Runs AdaBoost using decision stumps as weak classifiers.

    Args:
        X (numpy.ndarray): Input data.
        Y (numpy.ndarray): Target labels for input data.
        num_iterations (int): Number of AdaBoost iterations.

    Returns:
        A tuple containing:
            - classifiers (list): A list of (j, c, d) tuples representing the
            decision stumps selected at each iteration, where j is the feature
            index, c is the threshold value, and d is the direction (+1 or -1).
            - alphas (list): A list of alpha values representing
            the weights assigned to each decision stump.
    """
    N = X.shape[0]
    # Initialize weights uniformly
    weights = np.ones(N) / N
    # List of decision stump classifiers
    classifiers = []
    # List of weights for each classifier
    alphas = []

    for _ in range(num_iterations):
        j, c, d, error = decision_stump(X, Y, weights)
        # Compute weight for current classifier
        alpha = 0.5 * np.log((1 - error) / error)
        # Add current classifier to list
        classifiers.append((j, c, d))
        # Add current weight to list
        alphas.append(alpha)
        y_pred = d * np.ones(Y.shape)
        # Compute predictions for current classifier
        y_pred[X[:, j] * d < c * d] = -1
        # Update weights based on classification accuracy
        weights *= np.exp(-alpha * Y * y_pred)
        # Normalize weights so that they sum to 1
        weights /= np.sum(weights)
    return classifiers, alphas


def adaboost_cv(X, Y, num_iterations):
    """
    Trains using AdaBoost and cross-validates its performance.

    Args:
        X (numpy.ndarray): Input data.
        Y (numpy.ndarray): Target labels for input data.
        num_iterations (int): Number of AdaBoost iterations.

    Returns:
        A tuple (train_errors, test_errors) containing the training and testing
        error rates for each iteration of the AdaBoost algorithm.

    Notes:
        Cross-validates performance over multiple data splits.
        Uses a 90/10 split for each split.
    """
    train_errors = np.zeros(num_iterations)
    test_errors = np.zeros(num_iterations)
    num_splits = 50
    for _ in range(num_splits):
        X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.1)
        classifiers, alphas = adaboost(X_train, Y_train, num_iterations)
        train_errors_i = np.zeros(num_iterations)
        test_errors_i = np.zeros(num_iterations)
        for t in range(num_iterations):
            # Compute predictions for each classifier at iteration t
            y_train_pred = np.zeros(Y_train.shape)
            y_test_pred = np.zeros(Y_test.shape)
            for j in range(t + 1):
                j_t, c_t, d_t = classifiers[j]
                alpha_t = alphas[j]
                y_train_pred += alpha_t * np.sign(X_train[:, j_t] * d_t - c_t)
                y_test_pred += alpha_t * np.sign(X_test[:, j_t] * d_t - c_t)
            # Compute training and testing error for iteration t
            train_errors_i[t] = np.mean(np.sign(y_train_pred) != Y_train)
            test_errors_i[t] = np.mean(np.sign(y_test_pred) != Y_test)
        train_errors += train_errors_i
        test_errors += test_errors_i
    train_errors /= num_splits
    test_errors /= num_splits
    return train_errors, test_errors


def plot_error_graph(train_errors, test_errors):
    """
    Plots the training and testing error rates
    for each iteration of the AdaBoost algorithm.

    Parameters:
        train_errors (list of floats): Training error at each iteration.
        test_errors (list of floats): Testing error at each iteration.

    Returns:
        None
    """
    # Plot training and testing error
    fig, ax = plt.subplots()
    ax.plot(train_errors, label="Training error")
    ax.plot(test_errors, label="Testing error")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Error")
    ax.set_title("AdaBoost Error vs. Iteration")
    ax.legend()
    # plt.savefig("adaboost_error.png")
    plt.show()


if __name__ == "__main__":
    X, Y = load_data()

    # HW Question 5.1
    num_iterations = 10
    classifiers, alphas = adaboost(X, Y, num_iterations)
    for i in range(num_iterations):
        j, c, d = classifiers[i]
        C1 = d
        if c < np.mean(X[:, j]):
            C2 = -d
        else:
            C2 = d
        # Print selected feature component, threshold,
        # and class label for current iteration
        print(
            f"Iteration {i+1}: feature component(j) = {j}, threshold(c) = {c}, C1 = {C1}"
        )

    # HW Question 5.2
    train_errors, test_errors = adaboost_cv(X, Y, 100)
    plot_error_graph(train_errors, test_errors)
