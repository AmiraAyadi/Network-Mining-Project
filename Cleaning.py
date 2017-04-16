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

def vect2email(dictionary, vect):
    index = [i for i, x in enumerate(vect) if x == 1]
    inv_dictionary = {v: k for k, v in dictionary.items()}
    email_list = []
    for i in index:
        email_list.append(inv_dictionary[i])
    return(email_list)

#dt = parser.parse("Aug 28 1999 12:00AM")

"""
training_info_sid_min.csv C'est un fichier qui est un extrait du fichier training_info_sid.csv
On l'a fait pour minimiser les temps du execution
"""
f = open('./Datasets/new_training_info_min.csv', 'r')
t = open('./Datasets/new_test_info.csv', 'r')

reader_train = csv.reader(f, delimiter=',', quotechar='"')
reader_test = csv.reader(t, delimiter=',', quotechar='"')
steamer = DocTransformer()


"""
On mettre le text brut du fichier CSV (colonne 2) dans une list (body_list)
"""
x_id_list = []
x_date_list = []

y_id_list = []
y_date_list = []


"""
Initialisation des listes des champs pour email
"""
#train = x_
x_body_list = []
x_destinataires_list = []
x_expediteurs_list = []

#test = y_
y_body_list = []
y_destinataires_list = []
y_expediteurs_list = []


C = 0 #PARAMETER:  TAKE C = 0 IF THERE ISN'T INDEX COLUMN IN THE CSV // ELSE: C = 1 

#TRAIN
for row in reader_train:
    x_id_list.append(row[0+C])
    x_date_list.append(row[1+C])
    x_body_list.append(row[2+C])
    x_destinataires_list.append(row[3+C])
    x_expediteurs_list.append(row[4+C])

#TEST
for row in reader_test:
    y_id_list.append(row[0+C])
    y_date_list.append(row[1+C])
    y_body_list.append(row[2+C])
    y_expediteurs_list.append(row[3+C])



#(DATE TRAIN)
"""
Initialisation de la date:
"""
x_year_date_list = []
x_month_date_list = []
x_day_date_list = []
x_weekday_date_list = []
for i in range(0,len(x_date_list)):
    #DEBUG
    #print(str(id_list[i]), " ") 
    #print(date_list[i]) 
    
    #If there's not date
    if(x_date_list[i] == ""):
        continue
        
    dt = parse(x_date_list[i])
    x_year_date_list.append(dt.year)
    x_month_date_list.append(dt.month)
    x_day_date_list.append(dt.day)
    x_weekday_date_list.append(dt.isoweekday())
    

#(DATE TEST)
"""
Initialisation de la date:
"""

y_year_date_list = []
y_month_date_list = []
y_day_date_list = []
y_weekday_date_list = []
for i in range(0,len(y_date_list)):
    #DEBUG
    #print(str(y_id_list[i]), " ") 
    #print(y_date_list[i]) 
    
    #If there's not date
    if(y_date_list[i] == ""):
        print(i)
        continue
        
    dt = parse(y_date_list[i])
    y_year_date_list.append(dt.year)
    y_month_date_list.append(dt.month)
    y_day_date_list.append(dt.day)
    y_weekday_date_list.append(dt.isoweekday())

"""
Initialisation des emails TRAIN
"""
x_email_list = []    
for i in range(0,len(x_id_list)):
    x_email_list.append(Email(ID_mail=x_id_list[i], text=x_body_list[i], date=datetime.date(x_year_date_list[i],x_month_date_list[i],x_day_date_list[i]), destinataires=x_destinataires_list[i],expediteurs=x_expediteurs_list[i].split()))

"""
Initialisation des emails TEST
"""
y_email_list = []

for i in range(0,len(y_id_list)):
    y_email_list.append(Email(ID_mail=y_id_list[i], text=y_body_list[i], date=datetime.date(y_year_date_list[i],y_month_date_list[i],y_day_date_list[i]), destinataires=None,expediteurs=y_expediteurs_list[i].split()))    

"""
Nettoyage des emails TRAIN (le text nettoyé s'est mis sur email.tokenise comme un vecteur des mots)
"""
for email in x_email_list:
    email.text = steamer.clean(*email.text)
    email.tokenise = steamer.removeStopWords(steamer.tokenise(email.text))
    #email.print()

"""
Nettoyage des emails TEST (le text nettoyé s'est mis sur email.tokenise comme un vecteur des mots)
"""
for email in y_email_list:
    email.text = steamer.clean(*email.text)
    email.tokenise = steamer.removeStopWords(steamer.tokenise(email.text))
    #email.print()

    
"""
Initialisation pour TFIDF TRAIN:
"""

x_tfidf_maker_body = DocTransformer()
x_tfidf_maker_expediteurs = DocTransformer()
x_tfidf_maker_destinataires = DocTransformer()

x_documents = [email.text  for email in x_email_list]
x_expediteurs = [str(email.expediteurs) for email in x_email_list]
x_destinataires = [str(email.destinataires) for email in x_email_list]
x_dates = [[email.date[0].month, email.date[0].year, email.date[0].isoweekday(), email.date[0].day] for email in x_email_list]
#print(x_dates)

"""
Taken vocabulary
"""
x_tfidf_maker_body.getVectorKeywordIndex(x_documents)
x_tfidf_maker_expediteurs.getVectorKeywordIndex(x_expediteurs + x_destinataires, clean=False)
x_tfidf_maker_destinataires.getVectorKeywordIndex(x_expediteurs + x_destinataires, clean=False)
x_expediteurs_vector_keyword = x_tfidf_maker_expediteurs #Rename
#{'richardverma@univ': 0, 'burnsstrider@univ': 1, ... ,'danielschwerin@univ': 24}
x_destinataires_vector_keyword = x_tfidf_maker_destinataires #Rename
#print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
#print(x_destinataires_vector_keyword.vectorKeywordIndex)
#print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
"""
Making vectors
"""
x_tfidf_maker_body.matrixVector(x_documents)
x_tfidf_maker_expediteurs.matrixVector(x_expediteurs)
x_tfidf_maker_destinataires.matrixVector(x_destinataires)

x_matrix_tfidf_body = x_tfidf_maker_body.documentVectors
x_matrix_tfidf_expediteurs = x_tfidf_maker_expediteurs.documentVectors
x_matrix_tfidf_destinataires = x_tfidf_maker_destinataires.documentVectors


x_matrix_data = []
x_matrix_class = []
for i in range(len(x_matrix_tfidf_body)):
    x_matrix_data.append(np.concatenate((x_matrix_tfidf_body[i],x_matrix_tfidf_expediteurs[i],x_dates[i])))
    x_matrix_class.append(x_matrix_tfidf_destinataires[i])
#print(matrix_data[1])
#print("#@"*40)
#print(matrix_class[1])
#[    0.     0.     0. ...,  2012.     3.    12.]

"""
Initialisation pour TFIDF TEST:
"""

y_tfidf_maker_body = DocTransformer()
y_tfidf_maker_destinataires = DocTransformer()

y_documents = [email.text  for email in y_email_list]
y_expediteurs = [str(email.expediteurs) for email in y_email_list]
y_dates = [[email.date[0].month, email.date[0].year, email.date[0].isoweekday(), email.date[0].day] for email in y_email_list]
#print(dates)


"""
Same vocabulary than in train step (Making new vectors):
"""
x_tfidf_maker_body.matrixVector(y_documents)
x_tfidf_maker_expediteurs.matrixVector(y_expediteurs)

"""
Taking test data vectors
"""
y_matrix_tfidf_body = x_tfidf_maker_body.documentVectors
y_matrix_tfidf_expediteurs = x_tfidf_maker_expediteurs.documentVectors

y_matrix_data = []
for i in range(len(y_matrix_tfidf_body)):
    y_matrix_data.append(np.concatenate((y_matrix_tfidf_body[i],y_matrix_tfidf_expediteurs[i],y_dates[i])))
#print(y_matrix_data[1])
#[    0.     0.     0. ...,  2012.     3.    12.]
#print("#@"*40)



"""
#MACHINE LEARNING TRAININ STEP
"""
from sklearn import svm
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn import preprocessing

X = x_matrix_data
y = x_matrix_class

X = np.array(X)
y = np.array(y)
for h in range(len(y)):
    print([i for i, x in enumerate(y[h]) if x == 1])

binarizer = preprocessing.Binarizer()
y = binarizer.transform(y)

classif = OneVsRestClassifier(SVC(kernel='linear'))
classif.fit(X, y)

print("Classif Fit [OK]")

"""
#MACHINE LEARNING TEST STEP
"""

X_TEST = y_matrix_data
X_TEST = np.array(X_TEST)
    
email_dictionary = x_expediteurs_vector_keyword.vectorKeywordIndex
print(email_dictionary)

y_PRED = []
email_pred = []

"""
        ¡¡¡ ATENTION: !!!

        CHANGER LE 4 ON BAS POUR LEN(X_TEST) pour le depot final
"""
for i in range(4):
    pred = classif.predict(X_TEST[i].reshape(1,-1))
    pred = pred.tolist()[0]
    y_PRED.append(pred)
    #print(pred)
    email_pred.append(vect2email(email_dictionary, pred))
    print(str(y_id_list[i]) + ", " + str(email_pred[i]))
    


"""
pd = pandas.DataFrame(id_list, date_list, destinataires_list, body_clean_list)
pd.to_csv("out.csv")
"""                                         


















