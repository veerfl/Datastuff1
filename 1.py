import pandas as pd
import csv
import glob
import os
path = '.'
files_in_dir = [f for f in os.listdir(path) if f.endswith('csv')]
for filenames in files_in_dir:
    df = pd.read_csv(filenames)
    df.to_csv('out.csv', mode='a')
