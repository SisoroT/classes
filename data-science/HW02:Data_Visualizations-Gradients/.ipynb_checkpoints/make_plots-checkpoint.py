import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
from sklearn.linear_model import LinearRegression

# Read in bikes.csv into a pandas dataframe
bikes_df = pd.read_csv("bikes.csv")

# Read in DOX.csv into a pandas dataframe
# Be sure to parse the 'Date' column as a datetime
dox_df = pd.read_csv("DOX.csv")

# Divide the figure into six subplots
# Divide the figure into subplots
fig, axs = plt.subplots(3, 2, figsize=(12, 12))

# Make a pie chart
plt.pie(fig)
plt.title("Current Status")

# Make a histogram with quartile lines
# There should be 20 bins
### Your code here

# Make a scatter plot with a trend line
### Your code here

# Make a boxplot sorted so mean values are increasing
# Hide outliers
### Your code here

# Make a violin plot
### Your code here

# Create some space between subplots
plt.subplots_adjust(left=0.1, bottom=0.1, right=0.9, top=0.9, wspace=0.4, hspace=0.4)

# Write out the plots as an image
plt.savefig("plots.png")
