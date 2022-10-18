import pickle as pkl
from sklearn.metrics import confusion_matrix, accuracy_score
import matplotlib.pyplot as plt
from sklearn.metrics import ConfusionMatrixDisplay
from time import perf_counter
from keras.datasets import mnist

# Read in the MNIST data
d = 28 * 28
(_, _), (X_test, y_test) = mnist.load_data()
X_test = X_test.reshape((-1, d))

# Read in the classifier
with open("knn_model.pkl", "rb") as f:
    classifier = pkl.load(f)

start = perf_counter()
# Make predictions for the test data
## Your code here
print(f"Inference: elapsed time = {perf_counter() - start:.2f} seconds")

# Show accuracy
## Your code here

# Create a =onfusion matrix
## Your code here

# Make a display
fig, ax = plt.subplots()
ax.set_title("MNIST Confusion Matrix")
## Your code here
fig.savefig("sk_confusion.png")
print("Wrote sk_confusion.png")
