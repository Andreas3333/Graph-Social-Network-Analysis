import pandas as pd
import csv
import json

df = pd.read_csv(
    "node_edge_updated.txt",
    sep=r"\t+",
    header=None,
    names=["Source", "Target"],
    engine="python",
)

df.to_csv("node_egde_updated.cvs", sep=",", index=False)
