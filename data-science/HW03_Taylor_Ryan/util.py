import pandas as pd
import numpy as np


# Read in the excel file
# Returns:
#   X: first column is 1s, the rest are from the spreadsheet
#   Y: The last column from the spreadsheet
#   labels: The list of headers for the columns of X from the spreadsheet
def read_excel_data(infilename):
    df = pd.read_excel(infilename)
    df["property_id"] = np.ones(df["property_id"].size)

    X = df.iloc[:, :-1].to_numpy()
    Y = df.iloc[:, -1].to_numpy()
    labels = df.iloc[:, :-1].columns.to_list()

    return X, Y, labels


# Make it pretty
def format_prediction(B, labels):
    pred_string = f"${B[0]:,.2f}"
    for i in range(1, len(labels)):
        b = B[i]
        label = labels[i]
        pred_string += f" + (${b:,.2f} x {label})"

    return pred_string


# Return the R2 score for coefficients B
# Given inputs X and outputs Y
def score(B, X, Y):
    # matrix multiplication to find predicted Y
    predictions = X @ B
    # calculate residuals matrix for predictions
    residuals_for_pred = Y - predictions
    # calculate residuals matrix for mean
    residuals_for_mean = Y - np.mean(Y)
    # sum up residual matrices
    nume = np.sum((residuals_for_pred) ** 2)
    denom = np.sum((residuals_for_mean) ** 2)
    # calculate and return R2 score
    R2 = 1 - (nume / denom)
    return R2
