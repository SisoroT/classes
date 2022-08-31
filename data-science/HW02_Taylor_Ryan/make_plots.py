import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as dates
import numpy as np
import sympy

from sklearn.linear_model import LinearRegression

# Read in bikes.csv into a pandas dataframe
bikes_df = pd.read_csv("bikes.csv")

# Read in DOX.csv into a pandas dataframe
# Be sure to parse the 'Date' column as a datetime
dox_df = pd.read_csv("DOX.csv")
dox_df["Date"] = pd.to_datetime(dox_df["Date"])

# Divide the figure into six subplots
# Divide the figure into subplots
fig, axs = plt.subplots(3, 2, figsize=(12, 12))


# PLOT 1 (pie chart)
# Make a pie chart

# create data and labels
data = bikes_df["status"].value_counts()
lbs = sorted(bikes_df["status"].unique())

# set the title of the pie chart
axs[0][0].set_title("Current Status")

# create pie chart and store the different components in variables
wedges, texts, autotexts = axs[0][0].pie(
    data,
    labels=lbs,
    autopct="%1.1f%%",
    textprops={"color": "w"},
)

# for each wedge set the corresponding text to the same color
for i, wedge in enumerate(wedges):
    texts[i].set_color(wedge.get_facecolor())


# PLOT 2 (histogram)
# Make a histogram with quartile lines
# There should be 20 bins
data = bikes_df["purchase_price"]

# data for vertical lines
lower = bikes_df["purchase_price"].min()
quart1, half, quart3 = data.quantile([0.25, 0.5, 0.75])
upper = bikes_df["purchase_price"].max()

# set labels for the title and axes of the graph
axs[0][1].set_title("Price Histogram (1000 bikes)")
axs[0][1].set(xlabel="US Dollars", ylabel="Number of Bikes")
# add dolar sign to x-axis
axs[0][1].xaxis.set_major_formatter("${x:.0f}")

# create histogram
axs[0][1].hist(data, bins=20, ec="teal", fill=False, histtype="step")


# v-line for minimum
axs[0][1].axvline(lower, color="k", linestyle="dashed")
axs[0][1].text(lower + 10, 11, f"min: ${round(lower)}", rotation=90)

# v-line for 1st quartile
axs[0][1].axvline(quart1, color="k", linestyle="dashed")
axs[0][1].text(quart1 + 10, 11, f"25%: ${round(quart1)}", rotation=90)

# v-line for 2nd quartile (half)
axs[0][1].axvline(half, color="k", linestyle="dashed")
axs[0][1].text(half + 10, 11, f"50%: ${round(half)}", rotation=90)

# v-line for 3rd quartile
axs[0][1].axvline(quart3, color="k", linestyle="dashed")
axs[0][1].text(quart3 + 10, 11, f"75%: ${round(quart3)}", rotation=90)

# v-line for maximum
axs[0][1].axvline(upper, color="k", linestyle="dashed")
axs[0][1].text(upper + 10, 11, f"max: ${round(upper)}", rotation=90)


# PLOT 3 (scatter plot)
# Make a scatter plot with a trend line
# make price x axis and weight y axis
x_axis, y_axis = bikes_df["purchase_price"], bikes_df["weight"]

# calculate the equation for the trendline
tl_calc = np.polyfit(x_axis, y_axis, 1)
tl = np.poly1d(tl_calc)

# set labels for the title and axes of the graph
axs[1][0].set_title("Price vs. Weight")
axs[1][0].set(xlabel="Price", ylabel="Weight")
# add dolar sign and unit to axis ticks
axs[1][0].xaxis.set_major_formatter("${x:.0f}")
axs[1][0].yaxis.set_major_formatter("{x:.0f} kg")

# plot scatter plot and line for trend line
axs[1][0].scatter(x_axis, y_axis, s=1, c="teal", alpha=0.75)
axs[1][0].plot(x_axis, tl(x_axis), "r")


# PLOT 4 (line graph)
x_axis, y_axis = dox_df["Date"], dox_df["Close"]

# set the title
axs[1][1].set_title("DOX")

# format dates to just month and day
axs[1][1].xaxis.set_major_formatter(dates.DateFormatter("%m/%d"))
# add dollar sign to y axis
axs[1][1].yaxis.set_major_formatter("${x:.2f}")

# plot line graph
axs[1][1].plot(x_axis, y_axis)

# show the grid
axs[1][1].grid()


# PLOT 5 (boxplot)
# Make a boxplot sorted so mean values are increasing
# Hide outliers

# empty list to hold data
data = []
# create dictionary with all brands and their median prices
medians_dict = bikes_df.groupby(by=["brand"])["purchase_price"].median()

# sort dictionaries by median
unique_brands = dict(sorted(medians_dict.items(), key=lambda item: item[1]))

# create a list of with the pricing info for each brand
for brand in unique_brands.keys():
    data.append(bikes_df.loc[bikes_df["brand"] == brand, "purchase_price"])

# set the title
axs[2][0].set_title("Brand vs. Price")
# add $ to y axis prices
axs[2][0].yaxis.set_major_formatter("${x:.0f}")

# create boxplot
bp = axs[2][0].boxplot(
    data,
    labels=unique_brands,
    showfliers=False,
)

# change colors of different components
for box in bp["boxes"]:
    box.set(color="teal")
for whisker in bp["whiskers"]:
    whisker.set(color="teal")
for med in bp["medians"]:
    med.set(color="g")

# add grid
axs[2][0].grid(True)


# PLOT 6 (violin plot)
# Make a violin plot

# empty list to hold data
data = []
# create dictionary with all brands and their median prices
medians_dict = bikes_df.groupby(by=["brand"])["purchase_price"].median()

# sort dictionaries by median
unique_brands = dict(sorted(medians_dict.items(), key=lambda item: item[1]))

# create a list of with the pricing info for each brand
for brand in unique_brands.keys():
    data.append(bikes_df.loc[bikes_df["brand"] == brand, "purchase_price"])

# set the title
axs[2][1].set_title("Brand vs. Price")
# label x axis ticks
axs[2][1].set_xticks([1, 2, 3, 4, 5, 6])
axs[2][1].set_xticklabels(unique_brands.keys())
# add $ to y axis prices
axs[2][1].yaxis.set_major_formatter("${x:.0f}")

# create violiln plot
axs[2][1].violinplot(data, points=200, showmedians=True, widths=0.7)


# Create some space between subplots
plt.subplots_adjust(
    left=0.1,
    bottom=0.1,
    right=0.9,
    top=0.9,
    wspace=0.4,
    hspace=0.4,
)

# Write out the plots as an image
# plt.savefig("plots.png")

x, y, z = sympy.symbols("x y z")
func = y * sympy.sin(5 * x) + sympy.E ** (y * z) + sympy.ln(z)
df_x = sympy.diff(func, x)
df_y = sympy.diff(func, y)
df_z = sympy.diff(func, z)
print(df_x)
print(df_y)
print(df_z)
