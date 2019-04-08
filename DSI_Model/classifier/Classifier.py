# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 12:30:31 2018

@author: ya000
"""

import pandas as pd
import math
import numpy as np
from scipy import interp
import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np
from sklearn import svm, datasets
from sklearn.metrics import roc_curve, auc
from sklearn.model_selection import StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.neural_network import MLPClassifier
from sklearn import svm
# #############################################################################
# Data IO and generation

# Import some data to play with
np.random.seed(0)
frame = pd.read_csv("Evl_41selected_Onehot.csv")
num= len(frame.columns)
data = frame.iloc[:,0:num-1]
X=data.values
target = frame.iloc[:,num-1:num]
G1 = target.replace({"G1": 1,"G2":0, "G3":0, "G4":0,"G5":0,})
G2= target.replace({"G1": 0,"G2":1, "G3":0, "G4":0,"G5":0,})
G3= target.replace({"G1": 0,"G2":0,  "G3":1, "G4":0,"G5":0,})
G4= target.replace({"G1": 0,"G2":0 , "G3":0, "G4":1,"G5":0,})
G5= target.replace({"G1": 0,"G2":0 , "G3":0, "G4":0,"G5":1,})
label= pd.concat([G1,G2,G3,G4,G5], axis=1)

meanTpr=[]
meanFpr=[] 
meanAuc=[]
for j in range(0,5):
    y=label.iloc[:,j:j+1].values
    # Run classifier with cross-validation and plot ROC curves
    cv = StratifiedKFold(n_splits=10)
    #classifier = RandomForestClassifier(n_estimators=30,random_state =100)
    classifier = MLPClassifier(activation = 'tanh', hidden_layer_sizes=(int(1.2*(num-1)),int(1.5*(num-1))), learning_rate='constant',learning_rate_init=0.001)
    #classifier = svm.SVC(kernel='linear',decision_function_shape='ovr',probability=True)
    tprs = []
    aucs = []
    accuracy =[]
    mean_fpr = np.linspace(0, 1, 100)    
    i = 0
    for train, test in cv.split(X, y):
        if 1 in y[test]:
            probas_ = classifier.fit(X[train], y[train]).predict_proba(X[test])
            # Compute ROC curve and area the curve
            fpr, tpr, thresholds = roc_curve(y[test], probas_[:, 1])
            Temparr= interp(mean_fpr, fpr, tpr)
            tprs.append(Temparr)
            #tprs[-1][0] = 0.0
            roc_auc = auc(fpr, tpr)   
            aucs.append(roc_auc)
            plt.plot(fpr, tpr, lw=1, alpha=0.3,
                     label='ROC fold %d (AUC = %0.2f)' % (i, roc_auc))
            #print("fold",i, "AUC=",roc_auc)
           # print("AUC is",roc_auc)
            print(roc_auc)
            i += 1
    mean_tpr = np.mean(tprs, axis=0)
    #mean_tpr[-1] = 1.0
    mean_auc = auc(mean_fpr, mean_tpr)
    print("Group",j+1,"Mean_ROC",mean_auc)
    mean_tpr = np.mean(tprs, axis=0)
    mean_tpr[-1] = 1.0
    std_auc = np.std(aucs)
  #  plt.plot(mean_fpr, mean_tpr, color='b',
  #           label=r'Mean ROC (AUC = %0.2f $\pm$ %0.2f)' % (mean_auc, std_auc),
 #            lw=2, alpha=.8)
    std_tpr = np.std(tprs, axis=0)
    tprs_upper = np.minimum(mean_tpr + std_tpr, 1)
    tprs_lower = np.maximum(mean_tpr - std_tpr, 0)
    #plt.fill_between(mean_fpr, tprs_lower, tprs_upper, color='grey', alpha=.2,
     #              label=r'$\pm$ 1 std. dev.')
   # plt.xlim([-0.05, 1.05])
 #   plt.ylim([-0.05, 1.05])
  #  plt.xlabel('False Positive Rate')
  #  plt.ylabel('True Positive Rate')
  #  plt.title(j+1)
 #   plt.legend(loc="lower right")
  #  plt.show()    
    meanTpr.append(mean_tpr)
    meanFpr.append(mean_fpr)
    meanAuc.append(mean_auc)
    


# Plot all ROC curves
plt.figure()

colors = cycle(['aqua', 'darkorange', 'cornflowerblue','red','yellow'])
for i, color in zip(range(5), colors):
    plt.plot(meanFpr[i], meanTpr[i], color=color,
             label='G {0} (area = {1:0.2f})'
             ''.format(i+1, meanAuc[i]))

#plt.plot([0, 1], [0, 1], 'k--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('ROC curve of Random Forest Classifier')
#lt.title('ROC curve of MLP Classifier')
#plt.title('ROC curve of SVM Classifier')
plt.legend(loc="lower right")
plt.show()