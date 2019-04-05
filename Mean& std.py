# -*- coding: utf-8 -*-
"""
Created on Mon Jul  2 08:22:12 2018

@author: ya000
"""
import glob
import pandas as pd
# creates a list of all csv files
mypath = "\\\\egr-1l11qd2\\CLS_lab\\Junya Zhao\\help graph data_7\\All algorithm\\SRec&SRel\\result\\"
#globbed_files = glob.glob(mypath +"*csv")

# newnarrow mean
 
globbed_files = glob.glob("*csv")
for csv in globbed_files:
    frame = pd.read_csv(csv)
    NewNarrow = frame[0:15]
    with open(mypath+'NewNarrow_mean.csv', 'a') as output:
        NewNarrow.mean().to_csv(output,header= False)
with open(mypath+'NewNarrow_mean.csv', 'a') as output:
    #output.write(csv)
    output.write("NewNarrow_mean\n") 
    
# newnarrow std
globbed_files = glob.glob("*csv")
for csv in globbed_files:
    frame = pd.read_csv(csv)
    NewNarrow = frame[0:15]
    with open(mypath+'NewNarrow_std.csv', 'a') as output:
        NewNarrow.std().to_csv(output,header= False)
with open(mypath+'NewNarrow_std.csv', 'a') as output:
    #output.write(csv)
    output.write("NewNarrow_std\n")

