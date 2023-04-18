import numpy as np
import matplotlib.pyplot as plt
from scipy.io import loadmat
from sklearn.decomposition import PCA


# Load the data from 'digitdata.mat' file
def load_data(file_name):
    data = loadmat(file_name)
    X = data["X"]
    Y = data["Y"]
    return X, Y


# Plot the first 9 principal components as images
def plot_principal_components(components):
    plt.figure(figsize=(10, 10))
    for i, component in enumerate(components[:9]):
        plt.subplot(3, 3, i + 1)
        plt.imshow(component.reshape(28, 28), cmap="gray")
        plt.axis("off")
    plt.savefig("principal_components.png")


# Plot the eigenvalues in decreasing order
def plot_eigenvalues(eigenvalues):
    plt.figure(figsize=(10, 5))
    plt.plot(np.arange(1, len(eigenvalues) + 1), eigenvalues, marker="o")
    plt.xlabel("Eigenvalue Index")
    plt.ylabel("Eigenvalue")
    plt.savefig("eigenvalues.png")


# Reconstruct the images using different numbers of principal components
def reconstruct_images(X_pca, components, n_components_list):
    fig, axes = plt.subplots(2, len(n_components_list), figsize=(20, 5))

    for index, n_components in enumerate(n_components_list):
        reconstructed_X = X_pca[:, :n_components] @ components[:n_components]

        for i in range(2):
            ax = axes[i, index]
            ax.imshow(reconstructed_X[i].reshape(28, 28), cmap="gray")
            ax.axis("off")
            ax.set_title(f"{n_components} Components", fontsize=12)

    fig.subplots_adjust(hspace=0.4, wspace=0.4)
    plt.savefig("reconstructed_images.png")


if __name__ == "__main__":
    file_name = "digitdata.mat"
    X, Y = load_data(file_name)

    pca = PCA()
    X_pca = pca.fit_transform(X)

    plot_principal_components(pca.components_)
    plot_eigenvalues(pca.explained_variance_)

    n_components_list = [1, 2, 5, 10, 21, 44, 94, 200, 784]
    reconstruct_images(X_pca, pca.components_, n_components_list)
