import csv,sys
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfVectorizer

csv.field_size_limit(sys.maxsize)

#Read the training data from csv file
f = open('training_info_tp3.csv', 'r')

reader = csv.reader(f, delimiter=',', quotechar='"')
#X is used to represent the training data 
X=[]
#Y is used to save the training labels
y=[]
for row in reader:
  X.append(row[1]) 
  y.append(row[3])

#A tfidf representation fo text documents is used
tfidf_v = TfidfVectorizer(max_df=0.95, min_df=2, max_features=100000, stop_words='english')
tfidf = tfidf_v.fit_transform(X)

#A very simple classifier
clf = SVC()
clf.fit(tfidf, y)


#Read the test data
f = open('test_info_tp3.csv', 'r')
reader = csv.reader(f, delimiter=',', quotechar='"')
Xtest=[]
for row in reader:
  Xtest.append(row[1]) 

#The same tfidf representation is used
tfidf_test = tfidf_v.transform(Xtest)

#Labels are predicted to the tfidf data
pred_test=clf.predict(tfidf_test)


