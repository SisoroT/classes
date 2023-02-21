import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.io import loadmat
from sklearn.model_selection import train_test_split

# Load the Breast Cancer dataset from
# data_breastcancer.mat and convert it to a dataframe
data = loadmat("data_breastcancer.mat")

print(data)
