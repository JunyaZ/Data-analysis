# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 12:58:03 2018

@author: ya000
"""

import numpy as np
import pandas as pd
import random 
from collections import Counter
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn import metrics
from sklearn.datasets.samples_generator import make_blobs
from sklearn.preprocessing import StandardScaler
# #############################################################################
#data = pd.read_csv('winequality-red.csv') 
data = pd.read_csv('bitsDifftype3_174_SNPs_trans.csv',header = None) 
#data = pd.read_csv('153_matrix_all_num.csv')
#data = pd.read_csv('test.csv',header= None) 
def CateFunc(x,y):
    return (np.sum(np.not_equal(x,y)))/20
# #############################################################################
# Compute DBSCAN

model = DBSCAN(eps=1.8, min_samples=3 ,metric = CateFunc).fit(data)
outliers_df = pd.DataFrame(data)
print(model)
print (Counter(model.labels_))
print(model.labels_)
print("=====")
np.savetxt("labels_dascan.csv", model.labels_)
outliers =outliers_df[model.labels_== -1]
outliers.to_csv("Outliers_type3_174.csv")
#np.savetxt("375_SNPs_outliners.csv", outliers, delimiter=",",fmt='%0.5f')
for i in range(-1,len(model.labels_)):
    Centorid = random.sample(outliers_df[model.labels_== i],3)
    random.seed(0)
    Centorid.to_csv(f"{'label'+str(i)}.csv",index=False)    
        