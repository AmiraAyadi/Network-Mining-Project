#merge two csv file
import pandas as pd
import csv
import re


destina=[]
mail=[]
training_info_sid = pd.read_csv('./Datasets/training_info_sid.csv',header=None)
training_set = pd.read_csv('./Datasets/training_set_sid.csv',header=None)

df=training_info_sid.copy()

for i in range(len(training_set.index)):
    destina.append(re.split(' ',training_set[1][i]))
    mail.append(re.split(' ',training_set[0][i]))

for i in range(len(destina)):
    l=destina[i]
    for j in l:
        for a in range(len(training_info_sid.index)):
            if int(training_info_sid[0][a])==int(j):
                df.set_value(a, 4,mail[i][0] )

                
df.to_csv('new_training_info.csv', sep=',', header=False, index = False)


    

    
