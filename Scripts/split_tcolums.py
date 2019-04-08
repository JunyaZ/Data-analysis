import numpy as np
import sklearn
#address = '\\\\egr-1l11qd2\\CLS_lab\\Junya Zhao\\159_matrix_num_new.csv'
#address_save = '\\\\egr-1l11qd2\\CLS_lab\\Junya Zhao\\159_matrix_num_output.csv'
data = np.loadtxt('1264_SNPs_allele_trans_num.txt', delimiter = ",", dtype = np.int_).tolist()
final_m = []
for row in data:
    row = [str(i) for i in row]
    row = "".join(row)
    row = list(row)
    final_m.append(row)
np.savetxt( '50_SNPs_allele_trans.csv', final_m, fmt="%s", delimiter= ",")
