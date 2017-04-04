#merge two csv file
import pandas as pd
import csv
import re


destina=[]
mail=[]
file1 = pd.read_csv('./Datasets/training_info_sid.csv',header=None)
file2 = pd.read_csv('./Datasets/training_set_sid.csv',header=None)

df=file1.copy()

for i in range(len(file2.index)):
    destina.append(re.split(' ',file2[1][i]))
    mail.append(re.split(' ',file2[0][i]))

for i in range(len(destina)):
    l=destina[i]
    for j in l:
        for a in range(len(file1.index)):
            if int(file1[0][a])==int(j):
                df.set_value(a, 4,mail[i] )
    
df.to_csv('new_training_info.csv', sep=',',header=False)


    

    
