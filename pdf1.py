import pandas as pd
import numpy as np

df = pd.read_csv("all.csv")
table = pd.pivot_table(df,index=["Winner"],
               values=["Village Name"],
               aggfunc=[np.count_nonzero],fill_value=0)

ax = table.plot()
fig = ax.get_figure()
fig.savefig('as1.png')
