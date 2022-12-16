import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.ensemble import GradientBoostingRegressor
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import cross_val_score

# You run a shop that buys and sells classic bowling balls to collectors.

# bowling_balls.csv contains information about the bowling balls that you have sold:
# 	ball_id: a unique number that identifies each ball
# 	year: the year the ball was produced
# 	radius: the radius of the ball in centimeters
# 	mass: the mass of the ball in grams
# 	core: what the heavy core of the ball is made of
# 	coverstock: what the core is covered so it doesn't damage the floor
# 	opaque: 1 if the ball is opaque, 0 if it is transparent or translucent
# 	value: The price you sold the ball for

# You have a new shipment of 7 balls. You don't know the value of any of them. For three of them, you don't
# know what the core is made out of.  The data you have for them is in shipment.csv

# Create a python program called analyze_balls.py.  It should do each of these things:

# 0) (3 points) Make a pandas dataframes by reading in bowling_balls.csv. I will refer to this as the training dataframe.
train_df = pd.read_csv("bowling_balls.csv")
X = train_df.values[:, :-1]
Y = train_df.values[:, -1]

# 1) (4 points) Using the training dataframe, what is the mass of the lightest and heaviest balls?
# What is the average mass of the balls?
Min = train_df["mass"].min()
Max = train_df["mass"].max()
Average = train_df["mass"].mean()

print(f"Min: {Min}")
print(f"Max: {Max}")
print(f"Average: {Average}")

# 2) (6 points) Using the training data frame, make a scatter plot that shows the year on the x axis
# and the value on the y axis. Save it as year_value.png.
years = train_df["year"]
values = train_df["value"]
plt.scatter(years, values)
plt.xlabel("Year")
plt.ylabel("Value")
plt.title("Year vs Value")
plt.savefig("year_value.png")

# 3) (4 points) Compute the Pearson Correlation Coefficient for the year vs value.

# print(np.corrcoef(years, values)[0, 1])

# Answer = -0.6214918961777607

# 4) (7 points) Do linear regression to predict the value based only on the year. Generally how much should
# you expect the value of your classic bowling ball to increase each year?
X = train_df["year"].values.reshape(-1, 1)
Y = train_df["value"].values.reshape(-1, 1)
lin_reg = LinearRegression().fit(X, Y)
print(lin_reg.coef_)

# Answer = $-0.26


# REVISIT:
# 5) (6 points) Make a density plot of the mass of the balls. (Use matplotlib and gaussian_kde)
# Save it as mass_density.png.
mass = train_df["mass"]
density = gaussian_kde(mass)
xs = np.linspace(0, 1000, 200)
density.covariance_factor = lambda: 0.25
density._compute_covariance()
plt.plot(xs, density(xs))
plt.xlabel("Mass")
plt.ylabel("Density")
plt.title("Mass Density")
plt.savefig("mass_density.png")

# 6) (6 points) Create new columns in the training dataframe that contain the volume and the density of the ball.
# The volume of a sphere is 4 * PI * radius^3 / 3.  The density is mass / volume.
train_df["volume"] = 4 * np.pi * train_df["radius"] ** 3 / 3
train_df["density"] = train_df["mass"] / train_df["volume"]

# print(f"First row Volume: {train_df['volume'][0]} ")
# print(f"First row Density: {train_df['density'][0]} ")

# Volume of the first row of data in cubic centimenters = 10536.717453371153

# Density of the first row of data in grams per cubic centimeters = 1.3614961266148584

# 7) (10 points) Create and train a classifier that can predict the bowling ball's core material based on the year
#  and density of the ball. Use the sklearn.ensemble.RandomForestClassifier.
classifier = RandomForestClassifier(n_estimators=60)
classifier.fit(train_df[["year", "density"]], train_df["core"])

# 8) (2 points) Create a pandas dataframe by reading in shipment.csv. Give it volume and density columns too.
# I will refer to this as the testing data frame.
test_df = pd.read_csv("shipment.csv")
test_df["volume"] = 4 * np.pi * test_df["radius"] ** 3 / 3
test_df["density"] = test_df["mass"] / test_df["volume"]

# 9) (10 points) Some of the balls in the testing data don't have their core material listed.  Use your
# classifier to fill that in.
test_df["core"] = classifier.predict(test_df[["year", "density"]])

print(test_df[test_df["ball_id"] == 18]["core"])
print(test_df[test_df["ball_id"] == 25032]["core"])
print(test_df[test_df["ball_id"] == 4005]["core"])

# What do you think the missing entries are?
# Core for 000018 = bismuth
# Core for 025032 = bismuth
# Core for 004005 = barium

# 9) (8 points) Use 6-fold cross-validation on the training data to estimate how accurate you
# think your guesses are.
grid_searcher = GridSearchCV(
    RandomForestClassifier(),
    {"n_estimators": [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]},
    cv=6,
)
# grid_searcher.fit(train_df[["year", "density"]], train_df["core"])
# print(grid_searcher.best_score_)
# print(grid_searcher.best_params_)


# Expected accuracy = 0.8733333333333334%

# 10) (8 points) Convert the columns core and coverstock into one-hot columns in both data frames.

train_df = pd.get_dummies(train_df, columns=["core", "coverstock"])
test_df = pd.get_dummies(test_df, columns=["core", "coverstock"])
test_df["coverstock_resin"] = 0
test_df["coverstock_urethane"] = 0

# You are going to do regression using a numpy array with the following columns:
# 	The one-hot encodings for the core materials (3 columns)
# 	The one-hot encodings for the coverstock materials (5 columns)
# 	year
# 	radius
# 	mass
# 	opaque
# 	volume
# 	density

# Create X_train and X_test with these columns from the training data and the testing data respectively.
X_train = train_df.drop(columns=["value", "ball_id"])
X_test = test_df.drop(columns=["ball_id"])

# Create y_train, a column vector containing the value column.
y_train = train_df["value"].values.reshape(-1, 1)

# 11) (6 points) Create a GradientBoostingRegressor and train it on X_train
reg = GradientBoostingRegressor()
reg.fit(X_train, y_train)

# 12) (5 points) What are the values for the balls in the shipment?
y_test = reg.predict(X_test)
# print(y_test)

# Value for 000018 = 69.08616583826785
# Value for 035588 = 74.94761313250072
# Value for 025032 = 66.61785799328383
# Value for 036508 = 85.47609219338891
# Value for 004005 = 58.7938579150883
# Value for 026485 = 89.60027321971839

# 14) (1 point) Write out your predictions (including core and value) for the balls in shipment.csv.
# The file should be named predictions.csv.
test_df["value"] = y_test
test_df.to_csv("predictions.csv", columns=["ball_id", "value"], index=False)

# 14) (8 points) You can assume the residual has a mean of zero and is normally distributed.
# Use 6-fold cross-validation on the training data to estimate the standard error of your predictions.
print(np.average(cross_val_score(reg, X_train, y_train, cv=6)))

# Standard error = 0.9030454556225723 watts

# 15) (2 points) What is your margin of error for 95% confidence?
std = np.std(y_train)
ninety_five_percent = 1.96 * std / np.sqrt(len(y_train))
print(ninety_five_percent)

# 1.6485225408533382

# 16) (5) The length of adult Venks Mussels are normally distributed with a mean of 56mm and a standard deviation of 6mm.
# What is the smallest range (centered at 56mm) that will capture 50% of all Venks Mussels?

# the smallest range that will capture 50% of all Venks Mussels is 56mm +/- 4mm
# so 50% of all Venks Mussels are between 52mm and 60mm

# Once you are done. Zip this directory and submit it to iCollege. The zip file should contain:
# 	Final.txt (with all the ??? filled in)
# 	analyze_balls.py (your code that I will be able to run)
# 	year_value.png
# 	mass_density.png
# 	predictions.csv
# 	bowling_balls.csv (unedited training data that you were given)
# 	shipment.csv (unedited testing data that you were given)
