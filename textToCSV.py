import pandas as pd
import csv
import json

df = pd.read_csv(
    "node_edge.txt", sep=r"\s+", header=None, names=["N", "M", "W"], engine="python"
)

df.to_csv("node_edge.cvs", sep=",", index=False)
