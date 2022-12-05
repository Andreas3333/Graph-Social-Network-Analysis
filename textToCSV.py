import pandas as pd
import csv
import json

df = pd.read_csv(
    "New_1.csv",
    sep=r"\t+",
    header=None,
    names=["Source", "Target"],
    engine="python",
)

df.to_csv("New_1.csv", sep=",", index=False)
