# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 13:24:05 2018

@author: ya000
"""

import pandas as pd
import numpy as np
import multiprocessing as mp
import glob
import os 
mypath = "\\\\egr-1l11qd2\\CLS_lab\\Junya Zhao\\GWAS SNPs_2018\\newGWAS_data_April18\\orginal_data\\"
Output ="\\\\egr-1l11qd2\\CLS_lab\\Junya Zhao\\GWAS SNPs_2018\\newGWAS_data_April18\\orginal_data\\out\\"
probandpath = "\\\\egr-1l11qd2\\CLS_lab\\Junya Zhao\\GWAS SNPs_2018\\newGWAS_data_April18\\2759proband\\"
proband_out= "\\\\egr-1l11qd2\\CLS_lab\\Junya Zhao\\GWAS SNPs_2018\\newGWAS_data_April18\\2578 proband allele_only\\"

#==========================1mv1 and 1mv3=============================================
def extract_proband(allFiles):
    for csv in allFiles:
        frame = pd.read_csv(csv,header=None)
        frame['allele'] = frame[[6,7]].apply(lambda x: ''.join(x), axis=1)
#        print("unique", frame.allele.nunique())
        frame.rename(columns={'allele': os.path.basename(csv.split(sep=".")[0:][0])}, inplace=True)
        frame.rename(columns={3: "snpid"}, inplace=True)
        snpnumber= frame["snpid"].nunique()
        del frame[0]
        del frame[1]
        del frame[2]
        del frame[4]
        del frame[5]
        del frame[6]
        del frame[7]
        del frame[8]
        del frame[9]
        frame.to_csv(proband_out+ csv.split(sep="\\")[-1:][0],index=False)
        print (csv.split(sep="\\")[-1:][0], "Unique Snps:",snpnumber)
    
def Getinfo(filename,snp,infile):
    with open(filename ) as f1, open(snp) as f2:
        for i in f1:
            a = i.strip('\n')  # delete the \n in each line
            list_.append(a)
        for j in f2:
            b = j.strip('\n')  # delete the \n in each line
            snplist.append(b)
    print(snplist)
    print(list_)
    for df in pd.read_csv(infile,header=None, delimiter=' ',chunksize=10000000):
        df = df[df[8] >= 0.05]
        df = df[df[7] != '-']
        df = df[df[6] != '-']
        df = df[df[1].isin(list_)]
        df = df[df[3].isin(snplist)]
        df.to_csv(Output + "gwas_omni25.csv",mode='a',index= False,header=None)
        p1=df.groupby(1)
        print(p1.ngroups)
        p1.apply(lambda x: x.to_csv(r'\\egr-1l11qd2\\CLS_lab\\Junya Zhao\\GWAS SNPs_2018\\newGWAS_data_April18\\2759proband\\{}.csv'.format(x.name),mode='a',index= False,header=None))
        print("chunk done")
    print("getData done")
    num_1 = df[1].nunique()
    num_2 = df[3].nunique()
    num_3 = len(df)
    print("The unique proband number", num_1)
    print("The unique snp number:",num_2 )
    print("The total row number ", num_3)
if __name__ == "__main__": 
#    list_= []
#    snplist = []
#    allFiles = glob.glob(probandpath+'*.csv')
#    filename = mypath + "proband_list_2759.csv" 
#    snp = mypath + "gwas_oldList.csv"  
#    infile = mypath +"gwas_omni25.csv"
#    df =Getinfo(filename,snp,infile)
    allFiles = glob.glob(probandpath+'*.csv')
    check=pd.read_csv(Output + "list.csv", header=None)
    check=check[0].values.tolist()
    thenewlist = [x for x in allFiles if x.split(sep="\\")[-1:][0] in check]
    extract_proband(thenewlist)


    