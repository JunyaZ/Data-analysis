import pandas
import random

n = 157 #number of rows in the file
s = 7703 #desired sample size
file = "7703_SNPs_allele_trans_numminmax_Nom.csv"
#skip = sorted(random.sample(range(n),n-s))
df = pandas.read_csv(file)
n = random.randint(0,10)
for i in range(n):
    result = df.sample(7703,axis=1)
    print(result)
    with open(f"\\\\egr-1l11qd2\\CLS_lab\\Junya Zhao\\GWAS SNPs_2018\\random50_combo_Nonoverlap_\\{i}_random_7703.csv","w") as fo:
        fo.write(result.to_csv())
