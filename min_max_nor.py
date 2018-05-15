# -*- coding: utf-8 -*-
"""
@author: Junya 
"""

from sklearn import preprocessing
import csv
import numpy as np

#SOLUTION: Use csv library to convert to numpy.narray
data_file_name = "7703_SNPs_allele_trans_num.csv"

f  = open(data_file_name, 'r')
f = list(f)
for i in range(len(f)):
    f[i] = f[i].strip('\n')
    f[i] = f[i].split(',')

f  = np.asanyarray(f)
min_max_scaler = preprocessing.MinMaxScaler()
normalized_f = min_max_scaler.fit_transform(f)
output_file_name = data_file_name.split('.')[0] +'minmax_Nom.csv'
with open(output_file_name, 'w', newline = '') as ff:
    writer = csv.writer(ff)
    writer.writerows(normalized_f)
