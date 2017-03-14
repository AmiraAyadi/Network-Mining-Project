import csv
import nltk
from nltk.corpus import stopwords
import nltk.collocations
import collections
import re, string
import pandas

def remove_punctuation ( text ):
    return re.sub('[%s]' % re.escape(string.punctuation), ' ', text)



f = open('./Datasets/training_info_sid_min.csv', 'r')
reader = csv.reader(f, delimiter=',', quotechar='"')
body_list = []
for row in reader:
    body_list.append(row[2])

body_clean_list = []
for email in body_list:
    email = remove_punctuation(email)
    body_clean_list.append([str.lower(word) for word in str.split(email) if (str.lower(word) not in stopwords.words('english'))])

"""
for email in body_clean_list:
    print(*email)
    print("#######################################################")
"""    

pd = pandas.DataFrame(body_clean_list)
pd.to_csv("out.csv")

