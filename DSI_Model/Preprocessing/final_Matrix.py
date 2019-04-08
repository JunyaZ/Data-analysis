import os
import pandas as pd
import glob
import csv
#check=["11000","11001", "11002","11006" ,"11008"] 
#mv1list= pd.read_csv('C:\data\check1mv1.csv',header=None)
#check= mv1list[0].values.tolist()
#check = [str(x) for x in check]
df= pd.read_csv('C:\data\p_le0.2snplist.csv',header= None).rename(columns={0: "snpid"})
individual= pd.read_csv('C:\data\proband_ados.csv')
path = "\\\\egr-1l11qd2\\CLS_lab\\Junya Zhao\\GWAS SNPs_2018\\newGWAS_data_April18\\2587 proband allele_only\\"
Output ="\\\\egr-1l11qd2\\CLS_lab\\Junya Zhao\\GWAS SNPs_2018\\newGWAS_data_April18\\orginal_data\\out\\"
globbed_files = glob.glob(path + "*.csv") 
#globbed_files = [x for x in globbed_files if x.split(sep="\\")[-1].split(sep=".")[0] in check]
for csv in globbed_files:
    frame = pd.read_csv(csv, index_col=None, header=0)
    frame.rename(columns={0: "snpid"}, inplace=True)
    frame.drop_duplicates(inplace= True)
    df = df.merge(frame, how ='left', on=['snpid'])  
    print("read",csv.split(sep= "\\")[-1:][0])
print("Finished Reading")
#Trans =df.set_index(df.columns[0]).T.reset_index().rename(columns={"index":"individual"})
final= df.fillna(0)
final.to_csv(Output +'2587_Matrix_p_le0.2.csv',index=False)
