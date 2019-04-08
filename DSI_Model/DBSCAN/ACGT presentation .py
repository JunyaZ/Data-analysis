
import os
import pandas as pd
import glob
import csv

#creates a list of all csv files
globbed_files = glob.glob("*.csv") 

data = [] # pd.concat takes a list of dataframes as an agrument
for csv in globbed_files:
    frame = pd.read_csv(csv)
    out = frame.replace({"AA": 11,"AC": 12, "AG":13, "AT":14,'CC':22, 'CG':23, 'GG':33,"TT" :44})
    #data.append(frame)
    #del frame['Unnamed: 0']
    out.to_csv("375_bits_difference.csv")
    #total = frame.snpid.count()
    #print (csv, total)