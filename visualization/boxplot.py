# -*- coding: utf-8 -*-
"""
Created on Thu Oct  4 16:26:12 2018

@author: ya000
"""

import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import glob
# =============================================================================
# dataset_types = {
# # =============================================================================
# #     "New Narrow TP Datasets":       "narrow_(\([0-9]+,[0-9]+\))_(\([0-9]+,[0-9]+\))_typeI_data[0-9]",
# #     "New Square TP Datasets":       "square_(\([0-9]+,[0-9]+\))_(\([0-9]+,[0-9]+\))_typeI_data[0-9]",
# #     "UniBic Narrow Datasets":       "narrow_[0-9]+_[0-9]+_data[0-9]+",
# #     "UniBic Overlap": 	            "overlap_[0-9]+_[0-9]+_data[0-9]+",
# #     "UniBic Square TP":             "square_[0-9]+_[0-9]+_typeI_data[0-9]+",
# #     "UniBic Square Column Const":   "square_[0-9]+_[0-9]+_typeII_data[0-9]+",
# #     "UniBic Square Row Const":      "square_[0-9]+_[0-9]+_typeIII_data[0-9]+",
# #     "UniBic Square Shift-Scale":    "square_[0-9]+_[0-9]+_typeIV_data[0-9]+",
# #     "UniBic Square Shift":          "square_[0-9]+_[0-9]+_typeV_data[0-9]+",
# #     "UniBic Square Scale":          "square_[0-9]+_[0-9]+_typeVI_data[0-9]+"
# # =============================================================================
# # # =============================================================================
# #      "Fabia Noisy":           "datasets/fabia/exp_[1-100]_X.txt (Noisy)", 
# #      "Fabia Noise Free":      "datasets/fabia/exp_[1-100]_Y.txt (Noise Free)"
# # =============================================================================
# }
# =============================================================================

dataset_type= ["Noisy", "Noise Free"]
#dataset_types_list = sorted(list(dataset_types.keys()))

sns.set(style="whitegrid")
globbed_files = glob.glob("*.csv") 
result = pd.DataFrame()
for csv in globbed_files:
    file= pd.read_csv(csv)
    Recovery =["Recovery"] * len(file)
    Relevance =["Relevance"] * len(file)
    Symmetric_Rec =["S_Recovery"] * len(file)
    Symmetric_Rel =["S_Relevance"] * len(file)
    recovery = pd.concat([file.iloc[:,0:2],file.iloc[:,5:6],pd.DataFrame(Recovery)], axis=1).rename(index=str, columns={"algorithm": "algorithm","dataset_name": "dataset_name", "recovery": "score",0:"label"})
    relevance = pd.concat([file.iloc[:,0:2],file.iloc[:,4:5],pd.DataFrame(Relevance)], axis=1).rename(index=str, columns={"algorithm": "algorithm","dataset_name": "dataset_name", "relevance": "score",0:"label"})
    symmetric_recovery = pd.concat([file.iloc[:,0:2],file.iloc[:,3:4],pd.DataFrame(Symmetric_Rec)], axis=1).rename(index=str, columns={"algorithm": "algorithm","dataset_name": "dataset_name", "symmetric_recovery": "score",0:"label"})
    symmetric_relevance =  pd.concat([file.iloc[:,0:2],file.iloc[:,2:3],pd.DataFrame(Symmetric_Rel)], axis=1).rename(index=str, columns={"algorithm": "algorithm","dataset_name": "dataset_name", "symmetric_relevance": "score",0:"label"})
#    df =pd.concat([recovery, relevance, symmetric_recovery,symmetric_relevance])
    df =pd.concat([symmetric_recovery,symmetric_relevance])
    result =result.append(df, ignore_index = True).replace({"ChengChurch": "CC", "PenalizedPlaid": "PPM","EvoBexpa" : "EvoB", "NSGA_II(ASR)":"MOEA"})
print(result)
flatui = ["#9b59b6", "#3498db", "#95a5a6", "#e74c3c", "#34495e", "#2ecc71"]
colors = ["windows blue",  "greyish", "faded green", "dusty purple"]
hatches = ['-', '+', 'x', '\\', '*', 'o']
for i in range(0,len (dataset_type)):
    #dataset_type = dataset_types_list[i]
    matching_results = result[result.xs("dataset_name", axis=1).str.contains(dataset_type[i])]
    means= matching_results.groupby(["algorithm","label"]).score.mean().reset_index().sort_values(by=["algorithm"],ascending=True)
    plt.figure(figsize=(18,13)) 
    plt.ylim(0, 0.7)
    bplot = sns.boxplot(x="algorithm", y="score", hue ='label',width =0.6,linewidth =1.8, data=matching_results, palette="deep")#sns.xkcd_palette(colors)
#    hatches = ["", "","//","o","", "","//","o","", "","//","o","", "","//","o","", "","//","o","", "","//","o","", "","//","o","", "","//","o","", "","//","o"]
#    for hatch, patch in zip(hatches, bplot.artists):
#        patch.set_hatch(hatch)
        
    bplot.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05),ncol=4,prop={'size': 42})
    leg = bplot.get_legend()
#    leg.legendHandles[2].set_hatch('//')
#    leg.legendHandles[3].set_hatch('o')
    plt.yticks(size=30)
    plt.xticks(size=34)
    plt.rc('font', weight='bold')
    plt.vlines(0.5, ymin=0, ymax=1,linestyles='dotted')
    plt.vlines(1.5, ymin=0, ymax=1,linestyles='dotted')
    plt.vlines(2.5, ymin=0, ymax=1,linestyles='dotted')
    plt.vlines(3.5, ymin=0, ymax=1,linestyles='dotted')
    plt.vlines(4.5, ymin=0, ymax=1,linestyles='dotted')
    plt.vlines(5.5, ymin=0, ymax=1,linestyles='dotted')
    plt.vlines(6.5, ymin=0, ymax=1,linestyles='dotted')
    plt.vlines(7.5, ymin=0, ymax=1,linestyles='dotted')
    x1=-0.15
    x2=0.15
    for y in list(means[means["label"]=="Relevance"]["score"]):
        plt.scatter(x1, y, marker='o', s=100,c="orange")
        x1+=1
    for y in list(means[means["label"]=="S_Relevance"]["score"]):
        plt.scatter(x2, y, marker='o', s=100,c="orange")
        x2+=1
    plt.rc('font', weight='bold')
#    bplot.tick_params(labelsize=20)
    plt.rc('font', weight='bold')
    bplot.set_xlabel(' ')
    bplot.set_ylabel('  ')
    
    #bplot.set_title(dataset_type, fontsize=10)
    plot_file_name= dataset_type[i] +".png"
    bplot.figure.savefig(plot_file_name,format='png')
