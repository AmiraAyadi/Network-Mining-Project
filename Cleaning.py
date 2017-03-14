import csv
import nltk
from nltk.corpus import stopwords
import nltk.collocations
import collections
f = open('./Datasets/C.csv', 'r')
reader = csv.reader(f, delimiter=',', quotechar='"')
textlist = []
for row in reader:
    textlist.append(row[2])
    
f = [word for word in textlist if word not in stopwords.words('english')]
print(f)



##bgm = nltk.collocations.BigramAssocMeasures()
##finder = nltk.collocations.BigramCollocationFinder.from_words(documents.split())
