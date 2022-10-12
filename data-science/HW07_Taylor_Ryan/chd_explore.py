import pandas as pd
from pandas_profiling import ProfileReport

report_filename = "data_report.html"

# Read in the data
df = pd.read_csv("framingham.csv", index_col=None)
print(df.head())

# Create a report and save it to a file
profile = ProfileReport(df, title="Framingham Heart Study", explorative=True)
profile.to_file(report_filename)

print(f"Wrote report to {report_filename}")
