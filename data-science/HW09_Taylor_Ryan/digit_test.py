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
y_pred = classifier.predict(X_test)
print(f"Inference: elapsed time = {perf_counter() - start:.2f} seconds")

# Show accuracy
print(f"Accuracy on test data = {accuracy_score(y_test, y_pred)*100:.1f}%")

# Create a confusion matrix
cm = confusion_matrix(y_test, y_pred)
print(f"Confusion:\n{cm}")

# Make a display
fig, ax = plt.subplots()
ax.set_title("MNIST Confusion Matrix")
conf_matrix = ConfusionMatrixDisplay(
    confusion_matrix=cm,
    display_labels=range(10),
)
conf_matrix.plot(ax=ax, cmap="Blues")
fig.savefig("sk_confusion.png")
print("Wrote sk_confusion.png")
