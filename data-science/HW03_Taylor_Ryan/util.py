import pandas as pd
import numpy as np


# Read in the excel file
# Returns:
#   X: first column is 1s, the rest are from the spreadsheet
#   Y: The last column from the spreadsheet
#   labels: The list of headers for the columns of X from the spreadsheet
def read_excel_data(infilename):
    df = pd.read_excel(infilename)

    X = df.iloc[:, :-1].to_numpy()
    Y = df.iloc[:, -1].to_numpy()
    labels = df.iloc[:, :-1].columns.to_list()

    return X, Y, labels


# Make it pretty
def format_prediction(B, labels):
    pred_string = f"""
    ${B[0]:.2f}
    + (${B[1]:.2f} x {labels[1]})
    + (${B[2]:.2f} x {labels[2]})
    + (${B[3]:.2f} x {labels[3]})
    + (${B[4]:.2f} x {labels[4]})
    + (${B[5]:.2f} x {labels[5]})"""

    return pred_string


# Return the R2 score for coefficients B
# Given inputs X and outputs Y
def score(B, X, Y):
    ## Your code here
    return R2
