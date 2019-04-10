# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 12:42:53 2019

@author: ya000
"""

import pandas as pd
import glob
inputD="\\\\egr-1l11qd2\\CLS_lab\\TBI data\\Cobrit_data_2019-04-03T15-34-41\\"
path="\\\\egr-1l11qd2\\CLS_lab\\TBI data\\Output\\"
datasets=glob.glob(inputD +"*.csv")
DF=pd.DataFrame()
for file in datasets:
    af=pd.read_csv(file)
    column=af.columns.values.tolist()
    print(file)
    dr=[]
    for i in column:
        ar=[i + " :" + str(len(af[af[i].notnull()]))]
        dr=dr+ar
    Dr=pd.DataFrame(dr)
    Dr=Dr[0].str.split(":", n=2,expand = True)
    Dr=Dr.rename(columns={0:file.split(sep="result")[-1].split(sep="2019")[0],1:"Count"})
    DF = pd.concat([DF, Dr],axis=1)
DF.to_csv(path+"Out.csv",index=False)

writer = pd.ExcelWriter(path+'TBI data.xlsx', engine='xlsxwriter')
counter=[0,10,20,30,40,50,60,70,80,90,100,110]
for i in counter:
    df= DF.iloc[:,i:i+10]
    df.to_excel(writer, sheet_name="file "+str(int(i/2+1))+"_"+str(int(i/2+5)),index=False)
writer.save()   
