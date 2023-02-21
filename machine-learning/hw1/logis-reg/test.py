from scipy.io import loadmat

# Load the Breast Cancer dataset and convert it to a dataframe
mat = loadmat("data_breastcancer.mat")
# Number of samples
n = mat["data"]["n"][0][0][0][0]
# Number of attributes
d = mat["data"]["d"][0][0][0][0]
# Input data
X = mat["data"]["X"][0][0]
# Output labels
Y = mat["data"]["Y"][0][0].flatten()

print(n)
