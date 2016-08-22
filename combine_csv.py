import os
import csv
import pandas as pd


df = pd.DataFrame()

for f in ['1.csv', '2.csv','3.csv','4.csv','5.csv']:
    data = pd.read_csv(f)
    df = df.append(data)

df.to_csv("all.csv")
