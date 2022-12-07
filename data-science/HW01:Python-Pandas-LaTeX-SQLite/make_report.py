import pandas as pd
from datetime import date
import sys
import sqlite3


def series_report(
    series,
    is_ordinal=False,
    is_continuous=False,
    is_categorical=False,
):
    """Takes in a series from a pandas dataframe and reports various
    information depending on the type of data inputted.
    """
    # print series name and type
    print(f"{series.name}: {series.dtype}")
    # find amount of missing information
    missing_count = series.isnull().sum()

    if missing_count > 0:
        # show percentage missing
        percentage = round(missing_count / len(series) * 100, 2)
        print(f"\tMissing in {missing_count} rows ({percentage}%)")

    if is_ordinal:
        # print range
        print(f"\tRange: {series.min()} - {series.max()}")

    if is_continuous:
        # find mean, SD, and median
        stats = series.describe()
        print(f"\tMean: {stats['mean']:.2f}")
        print(f"\tStandard deviation: {stats['std']:.2f}")
        print(f"\tMedian: {stats['50%']:.2f}")

    if is_categorical:
        # find the number of entries for each value in the series
        series_counts = series.value_counts()
        for value in series_counts.index:
            print(f"\t\t{series_counts.loc[value]}: {value}")


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
series_report(df.index, is_ordinal=True)
series_report(df["gender"], is_categorical=True)
series_report(df["height"], is_ordinal=True, is_continuous=True)
series_report(df["waist"], is_ordinal=True, is_continuous=True)
series_report(df["salary"], is_ordinal=True, is_continuous=True)
series_report(df["dob"], is_ordinal=True)
series_report(df["death"], is_ordinal=True)

# connect to database
with sqlite3.connect("employees.db") as conn:
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
