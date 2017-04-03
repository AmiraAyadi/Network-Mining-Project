import csv
import nltk
from nltk.corpus import stopwords
import nltk.collocations
import collections
import re, string
import pandas


def remove_punctuation ( text ):
    return re.sub('[%s]' % re.escape(string.punctuation), ' ', text)

"""
training_info_sid_min.csv C'est un fichier qui est un extrait du fichier training_info_sid.csv
On l'a fait pour minimiser les temps du execution
"""
f = open('./Datasets/training_info_sid_min.csv', 'r')
reader = csv.reader(f, delimiter=',', quotechar='"')



"""
On mettre le text brut du fichier CSV (colonne 2) dans une list (body_list)
"""
id_list = []
date_list = []
body_list = []
destinataires_list = []
expediteurs_list = []
for row in reader:
    id_list.append(row[0])
    date_list.append(row[1])
    body_list.append(row[2])
    destinataires_list.append(row[3])
    #expediteurs_list.append(row[4])

"""
On nettoie le text brut pour simplifier le utilisation de l'algorithme de Machine Learning (après)
la sortie c'est une liste de mots en minuscule sans les stopwords
"""
body_clean_list = []
for email in body_list:
    email = remove_punctuation(email)
    body_clean_list.append([str.lower(word) for word in str.split(email) if (str.lower(word) not in stopwords.words('english'))])

"""
for email in body_clean_list:
    print(*email)
    print("#######################################################")
"""    

pd = pandas.DataFrame(id_list, date_list, destinataires_list, body_clean_list)
pd.to_csv("out.csv")


        
    
    
    
    
    
    
    
