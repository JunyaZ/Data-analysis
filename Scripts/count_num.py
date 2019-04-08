import os
import pandas as pd
import glob
import csv

#creates a list of all csv files
globbed_files = glob.glob("*.csv") 

data = [] # pd.concat takes a list of dataframes as an agrument
for csv in globbed_files:
    frame = pd.read_csv(csv)
    del frame['Unnamed: 0']
    total = frame.label.count()
    print (csv, total)
