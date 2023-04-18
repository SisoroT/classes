import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from sklearn.metrics import pairwise_distances_argmin
from scipy.stats import mode


def kmeans(X, k, max_iter=20):
    # Initialize centroids randomly
    centroids = X[np.random.choice(X.shape[0], k, replace=False)]

    # Iterate for max_iter times or until convergence
    for _ in range(max_iter):
        # Assign each data point to the nearest centroid
        labels = pairwise_distances_argmin(X, centroids)

        # Update centroids to the mean of the assigned data points
        new_centroids = np.array([X[labels == i].mean(axis=0) for i in range(k)])

        # Check for convergence
        if np.array_equal(centroids, new_centroids):
            break

        centroids = new_centroids

    return centroids, labels


# Calculate the within-group sum of squares (SS)
def calculate_ss(X, centroids, labels):
    ss = 0
    for i in range(centroids.shape[0]):
        # Get the data points in the cluster
        cluster_points = X[labels == i]

        # Calculate the sum of squares for the cluster
        ss += np.sum((cluster_points - centroids[i]) ** 2)

    return ss


def calculate_total_mistake_rate(Y, labels, k):
    mistakes = 0
    for i in range(k):
        # Get the true labels for data points in the cluster
        cluster_labels = Y[labels == i]

        # Determine the majority label for the cluster
        majority_label = mode(cluster_labels).mode[0]

        # Count the mistakes in the cluster
        mistakes += np.sum(cluster_labels != majority_label)

    # Calculate the total mistake rate
    return mistakes / len(Y)


if __name__ == "__main__":
    data = loadmat("digits_partial.mat")
    X = data["X"]
    Y = data["Y"]

    ks = np.arange(1, 6)
    ss_values = []
    total_mistake_rates = []

    # Perform K-means clustering and calculate SS and total mistake rate for each k
    for k in ks:
        centroids, labels = kmeans(X, k)
        ss = calculate_ss(X, centroids, labels)
        total_mistake_rate = calculate_total_mistake_rate(Y, labels, k)

        ss_values.append(ss)
        total_mistake_rates.append(total_mistake_rate)

    # Plot the sum of within-group sum of squares versus k
    plt.figure()
    plt.plot(ks, ss_values, marker="o")
    plt.xlabel("k")
    plt.ylabel("Sum of Within-Group Sum of Squares")
    plt.title("Within-Group Sum of Squares vs k")
    plt.grid()
    plt.savefig("within-group-sum-of-squares-vs-k.png")

    # Plot the total mistake rate versus k
    plt.figure()
    plt.plot(ks, total_mistake_rates, marker="o")
    plt.xlabel("k")
    plt.ylabel("Total Mistake Rate")
    plt.title("Total Mistake Rate vs k")
    plt.grid()
    plt.savefig("total-mistake-rate-vs-k.png")
