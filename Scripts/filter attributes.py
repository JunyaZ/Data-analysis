
from tkinter.filedialog import askopenfilename
import csv
import numpy as np
import re
threshold = 0.8
input_file_name= askopenfilename() #Initial data file with data only 
output_file_name = askopenfilename() #Output address data
#original_data_file = askopenfilename() #spss output data

attr_dict = dict()

data_peak = np.recfromcsv(input_file_name, delimiter = ',')
num_cols = len(data_peak[0])
num_rows = len(data_peak)
data  = np.zeros([num_rows , num_cols]) # num_cols - 1 means skip label col


with open(input_file_name) as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    for row in reader:
        if count == 0:
            for col in range(len(row)):
                attr_dict[col] = [row[col],'Accepted']
        else:
            for i in range(len(row)):
                row[i] =  re.findall(r"[-+]?\d*\.\d+|\d+", row[i])[0]
            data[count-1] = row
        count +=1
        
data = np.transpose(data)

attr_dict[0][1] = 'Accepted'
row_c = 0 
for r in data:
    col_c = 0
    for c in r:
        if row_c == col_c:
            break
        if abs(c) >= threshold:
                attr_dict[row_c][1] = 'Rejected'
                break
        col_c+=1
    row_c+=1
drop_v = []
with open(output_file_name, 'w', newline='', encoding='utf-8') as text_file:
    csv_file= csv.writer(text_file)
    csv_file.writerow(["Accepted", "Rejected"])
    for i in range(len(attr_dict)):
        if attr_dict[i][1]=='Accepted':
            csv_file.writerow([ attr_dict[i][0],''])
        else:
            drop_v.append(i)
            csv_file.writerow(['', attr_dict[i][0]])

#import pandas as pd
#removed =pd.read_csv(original_data_file)
#removed_filtered =removed.drop(removed.columns[drop_v], axis = 1)
#removed_filtered.to_csv("rfiltered.csv", index = False)
            

    


        
