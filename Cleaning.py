import csv
import nltk
from nltk.corpus import stopwords
import nltk.collocations
import collections
f = open('./Datasets/training_info_sid_min.csv', 'r')
reader = csv.reader(f, delimiter=',', quotechar='"')
body_list = []
for row in reader:
    body_list.append(row[2])

body_clean_list = []
for email in body_list:
    body_clean_list.append([str.lower(word) for word in str.split(email) if (str.lower(word) not in stopwords.words('english'))])
    
for email in body_clean_list:
    print(email)
    print("#######################################################")



##bgm = nltk.collocations.BigramAssocMeasures()
##finder = nltk.collocations.BigramCollocationFinder.from_words(documents.split())
