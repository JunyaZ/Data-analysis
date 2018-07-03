import pandas as pd
import glob
import numpy as np 
df= pd.read_csv("\\\\egr-1l11qd2\\CLS_lab\\Junya Zhao\\help graph data_7\\All algorithm\\"+"Rel&Rec.csv")

globbed_files = glob.glob("*csv")
for csv in globbed_files:
    frame = pd.read_csv(csv)
    print(frame)
    #frame.fillna("")
    #print(frame)
    df = pd.concat([df,frame], axis = 1)
    df.to_csv("\\\\egr-1l11qd2\\CLS_lab\\Junya Zhao\\help graph data_7\\All algorithm\\"+"SRel&SRec_result.csv",index=False)
