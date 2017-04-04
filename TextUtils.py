from stemming.porter2 import stem
import re
from sklearn.feature_extraction.text import TfidfTransformer

class Ranking:
    vectorKeywordIndex = []
    documentVectors = []
    def __init__(self):
        self.stopwords= open('SmartStoplist.txt','r').read().split()
        
    #1/Tronquer les mots (stemming)
    def clean(self, string):
        string = string.replace(".","")
        string = string.replace("(","")
        string = string.replace(")","")
        string = re.sub(r"[0-9]","",string)
        string = string.replace("\s+"," ")
        string = string.lower()
        return string
    def tokenise(self, string):
        """ break string up into tokens and stem words """
        string = self.clean(string)
        words = string.split()
        return [stem(word) for word in words]
        #2/Stoplist

    def removeStopWords(self,list):
        """ Remove common words which have no search value """
        return [word for word in list if word not in self.stopwords ]