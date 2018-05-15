import os, shutil
import random

path = '\\\\egr-1l11qd2\\CLS_lab\\Junya Zhao\\GWAS SNPs_2018\\1264_SNPs_file\\'
moveto = '\\\\egr-1l11qd2\\CLS_lab\\Junya Zhao\\GWAS SNPs_2018\\50_combination_1264\\'

for i in range(0,50):
    f = random.choice(os.listdir(path))
    src = path+f
    dst = moveto+f
    shutil.copy(src,dst)
