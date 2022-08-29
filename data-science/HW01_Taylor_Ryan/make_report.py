import pandas as pd
from datetime import date
import sys
import sqlite3

from sklearn.preprocessing import OrdinalEncoder


def series_report(series, is_ordinal=False, is_continuous=False, is_categorical=False):
    """Takes in a series from a pandas dataframe and reports various
    information depending on the type of data inputted.
    """
    if is_categorical:
        # print series name and type
        print(f"{series.name}: {series.dtype}")

        missing = series.isnull()
        # show percentage missing
        missing_pct = missing.sum() / len(series) * 100
        print(f"\tMissing in {missing.sum()} rows ({round(missing_pct, 1)}%)")

        series_counts = series.value_counts()
        # print results
        for value in series_counts.index:
            print(f'\t\t{series_counts.loc[value]}: "{value}"')

    elif is_ordinal and not is_continuous:
        series = df[series.name]
        # print series name and type
        print(f"{series.name}: {series.dtype}")

        # find range
        rng = f"{series.min()} - {series.max()}"

        # print results
        print(f"\tRange: {rng}")

    elif is_ordinal and is_continuous:
        # print series name and type
        print(f"{series.name}: {series.dtype}")

        missing = series.isnull()
        # show percentage missing
        missing_pct = missing.sum() / len(series) * 100
        if missing_pct != 0:
            print(f"\tMissing in {missing.sum()} rows ({round(missing_pct, 1)}%)")

        # find range, mean, SD, and median
        rng = f"{series.min()} - {series.max()}"
        mean = round(series.mean(), 2)
        st_dev = round(series.std(), 2)
        median = round(series.median(), 2)

        # print results
        print(f"\tRange: {rng}")
        print(f"\tMean: {mean}")
        print(f"\tStandard deviation: {st_dev}")
        print(f"\tMedian: {median}")

    else:
        print("Not a valid series...")


# Check command line arguments
if len(sys.argv) < 2:
    print(f"Usage: python3 {sys.argv[0]} <input_file>")
    exit(1)

# Read in the data
df = pd.read_csv(sys.argv[1], index_col="employee_id")

# Convert strings to dates for dob and death
df["dob"] = df["dob"].apply(lambda x: date.fromisoformat(x))
df["death"] = df["death"].apply(lambda x: date.fromisoformat(x))

# Show the shape of the dataframe
(row_count, col_count) = df.shape
print("*** Basics ***")
print(f"Rows: {row_count:,}")
print(f"Columns: {col_count}")

# Do a report for each column
print("\n*** Columns ***")
# series_report(df.index, is_ordinal=True)
series_report(df["gender"], is_categorical=True)
series_report(df["height"], is_ordinal=True, is_continuous=True)
series_report(df["waist"], is_ordinal=True, is_continuous=True)
series_report(df["salary"], is_ordinal=True, is_continuous=True)
series_report(df["dob"], is_ordinal=True)
series_report(df["death"], is_ordinal=True)

# connect to database
conn = sqlite3.connect("employees.db")
# create a cursor
curse = conn.cursor()

curse.execute(
    """
        SELECT rowid, AVG(height)
        FROM Employee
        WHERE salary > 35000
        """
)
items = curse.fetchall()

for item in items:
    print(item)

# commit command
conn.commit()
# close connection
conn.close()
