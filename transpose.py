import pandas as pd
import numpy as np
df=pd.read_csv('7703_SNPs_allele.csv')
X= df.values
Y =X.T
np.savetxt('7703_SNPs_allele_trans.csv', Y, fmt='%s',delimiter=',')
