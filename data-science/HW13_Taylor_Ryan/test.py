import pandas as pd

df = pd.read_csv("samples.csv")

df["timestamp"] = pd.to_datetime(df["timestamp"])
starttime = df["timestamp"][0]

print(starttime)

seconds = (df["timestamp"] - starttime).dt.total_seconds()

print(seconds)
