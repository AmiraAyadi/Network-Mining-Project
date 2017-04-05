import csv
import nltk
from nltk.corpus import stopwords
import nltk.collocations
import collections
import re, string
import pandas
from emails import *
import datetime
from dateutil.parser import *
from TextUtils import *
#dt = parser.parse("Aug 28 1999 12:00AM")

"""
training_info_sid_min.csv C'est un fichier qui est un extrait du fichier training_info_sid.csv
On l'a fait pour minimiser les temps du execution
"""
f = open('./Datasets/new_training_info.csv', 'r')
reader = csv.reader(f, delimiter=',', quotechar='"')
steamer = Steamer()


"""
On mettre le text brut du fichier CSV (colonne 2) dans une list (body_list)
"""
id_list = []
date_list = []

"""
Initialisation des listes des champs pour email
"""

body_list = []
destinataires_list = []
expediteurs_list = []
for row in reader:
    id_list.append(row[1])
    date_list.append(row[2])
    body_list.append(row[3])
    destinataires_list.append(row[4])
    expediteurs_list.append(row[5])

#(DATE)
"""
Initialisation de la date:
"""
year_date_list = []
month_date_list = []
day_date_list = []
weekday_date_list = []
for i in range(0,len(date_list)):
    #DEBUG
    #print(str(id_list[i]), " ")
    #print(date_list[i])
    if(date_list[i] == ""):
        continue
        
    dt = parse(date_list[i])
    year_date_list.append(dt.year)
    month_date_list.append(dt.month)
    day_date_list.append(dt.day)
    weekday_date_list.append(dt.isoweekday())

"""
Initialisation des emails
"""
email_list = []    
for i in range(0,len(id_list)):
    email_list.append(Email(ID_mail=id_list[i], text=body_list[i], date=date_list[i], destinataires=destinataires_list[i],expediteurs=expediteurs_list[i].split()))

"""
Nettoyage des emails (le text nettoyé s'est mis sur email.tokenise comme un vecteur des mots)
"""
for email in email_list:
    email.text = steamer.clean(*email.text)
    email.tokenise = steamer.removeStopWords(steamer.tokenise(email.text))
    email.print()

"""
pd = pandas.DataFrame(id_list, date_list, destinataires_list, body_clean_list)
pd.to_csv("out.csv")
"""                                         
