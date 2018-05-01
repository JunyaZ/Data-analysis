import pandas as pd
import os

df=pd.read_csv("1264_SNPs_allele.csv")
for i in range(len(df)):
    a = df.iloc[i]
    b= a.head(1)
    f= a.values
    re= []
    for j in f[1:]:
        ee = [c for c in j]
        print(ee)
        re.append(ee)
    frame= pd.DataFrame(re)
    frame = frame.fillna(0)
    frame = frame.replace({'A': 1,'C':2,'G':'3','T':4})
    with open(f"\\\\egr-1l11qd2\\CLS_lab\\Junya Zhao\\\GWAS SNPs_2018\\1264_SNPs_file\\{b[0]}.csv","w") as fo:
        fo.write(frame.to_csv())
