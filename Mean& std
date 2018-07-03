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

# oldnarriw mean

globbed_files = glob.glob("*csv")
for csv in globbed_files:
    frame = pd.read_csv(csv)
    oldNarrow = frame[15:24]
    with open(mypath+'oldNarroww_mean.csv', 'a') as output:
        oldNarrow.mean().to_csv(output,header= False) 
with open(mypath+'oldNarroww_mean.csv', 'a') as output:
    #output.write(csv)
    output.write("oldNarroww_mean\n")

     
# oldnarrow std
globbed_files = glob.glob("*csv")
for csv in globbed_files:
    frame = pd.read_csv(csv)
    oldNarrow = frame[15:24]
    with open(mypath+'oldNarrow_std.csv', 'a') as output:
        oldNarrow.std().to_csv(output,header= False)
with open(mypath+'oldNarrow_std.csv', 'a') as output:
    #output.write(csv)
    output.write("oldNarrow_std\n")
        

    
# overlap mean
globbed_files = glob.glob("*csv")
for csv in globbed_files:
    frame = pd.read_csv(csv)
    overlap= frame[24:44]
    with open(mypath+'overlap_mean.csv', 'a') as output:
        overlap.mean().to_csv(output,header= False)
with open(mypath+'overlap_mean.csv', 'a') as output:
     # output.write(csv)
      output.write("overlap_mean\n") 

      
# overlap std

globbed_files = glob.glob("*csv")
for csv in globbed_files:
    frame = pd.read_csv(csv)
    overlap= frame[24:44]
    with open(mypath+'overlap_std.csv', 'a') as output:
        overlap.std().to_csv(output,header= False)     
with open(mypath+'overlap_std.csv', 'a') as output:
    #output.write(csv)
    output.write("overlap_std\n") 

# NewSquare mean
globbed_files = glob.glob("*csv")
for csv in globbed_files:
    frame = pd.read_csv(csv)
    NewSquare= frame[44:59]
    with open(mypath+'NewSquare_mean.csv', 'a') as output:
        NewSquare.mean().to_csv(output,header= False)
with open(mypath+'NewSquare_mean.csv', 'a') as output:
    #output.write(csv)
    output.write("NewSquare_mean\n")

    
# NewSquare std

globbed_files = glob.glob("*csv")
for csv in globbed_files:
    frame = pd.read_csv(csv)
    NewSquare= frame[44:59]
    with open(mypath+'NewSquare_std.csv', 'a') as output:
        NewSquare.std().to_csv(output,header= False)
with open(mypath+'NewSquare_std.csv', 'a') as output:
    #output.write(csv)
    output.write("NewSquare_std\n") 
