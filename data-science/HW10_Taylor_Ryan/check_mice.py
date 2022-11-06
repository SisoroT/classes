import numpy as np
import pandas as pd
from scipy.stats import chi2

# Read in the data
mice_df = pd.read_csv("mice.csv")

# Figure out the possible gene types
gene_types = list(mice_df.gene_type.unique())
print(f"Possible gene types:{gene_types}")

# create contingency table with totals
print("------------------------- Create contingency table ------------------------")
contingency_table = pd.crosstab(
    mice_df["gene_type"],
    mice_df["has_cancer"],
    margins=True,
)
observed_matrix = np.array(contingency_table)
print(contingency_table)

# create contingency table with proportions
print("\n------------------------- Conditional proportions -------------------------")
conditional_table = pd.crosstab(
    mice_df["gene_type"],
    mice_df["has_cancer"],
    margins=True,
    normalize="index",
)
print(conditional_table)

# show expected values
print("\n---------- Expected counts if the gene & cancer were independent ----------")
group_totals = np.sum(observed_matrix, axis=1)
cat_totals = np.sum(observed_matrix, axis=0)
expected_proportions = cat_totals / np.sum(cat_totals)
expected_matrix = np.outer(group_totals, expected_proportions)
print(expected_matrix.round(2))


# calculate the chi-squared statistic
print("\n------------------ chi2, Degrees of Freedom, and p-value ------------------")
numerator = np.square(observed_matrix - expected_matrix)
x2 = np.sum(numerator / expected_matrix)
print(f"chi2 = {x2}")

# note degrees of freedom
dof = (len(gene_types) - 1) * (2 - 1)
print(f"dof = {dof}")

# calculate the p-value
p = 1 - chi2.cdf(x2, dof)
print(f"p-value = {p}")

print("Gene type and cancer are likely NOT independent.")
