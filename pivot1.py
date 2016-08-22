import pandas as pd
import numpy as np

df = pd.read_csv("all.csv")
table = pd.pivot_table(df,index=["Winner"],
               values=["Total"],
               aggfunc=[np.count_nonzero],fill_value=0)

table.to_csv("pivot1.csv")
