import numpy as np
from stemming.porter2 import stem
import re
from sklearn.feature_extraction.text import TfidfTransformer

def cosineVector(vector1, vector2):
        """ related documents j and q are in the concept space by comparing the vectors :cosine  = ( V1 * V2 ) / ||V1|| x ||V2|| """
        if (np.linalg.norm(vector1) != 0) and (np.linalg.norm(vector2) != 0):
            return float(np.dot(vector1,vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2)))
        else:
            return 0


class DocTransformer:
    vectorKeywordIndex = []
    documentVectors = []
    def __init__(self):
        self.stopwords= open('./doc/SmartStoplist.txt','r').read().split()
        
    def printVectorKeywordIndex(self):
        print(self.vectorKeywordIndex)
    
    
    #1/Tronquer les mots (stemming)
    def clean(self, string):
        string = string.replace(".","")
        string = string.replace("(","")
        string = string.replace(")","")
        string = string.replace("-"," ")
        string = string.replace(":"," ")
        string = string.replace(";"," ")
        string = string.replace(","," ")
        string = string.replace("/"," ")
        string = string.replace(r"_"," ")
        string = string.replace(r"['"," ")
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

    def removeStopWords(self, list):
        """ Remove common words which have no search value """
        return [word for word in list if word not in self.stopwords ]
    
    def getVectorKeywordIndex(self, documentList):
        """ create the keyword associated to the position of the elements within the document vectors """
        #Mapped documents into a single word string
        vocabularyString = " ".join(documentList)

        vocabularyList = self.tokenise(vocabularyString)
        #Remove common words which have no search value
        vocabularyList = self.removeStopWords(vocabularyList)
        #Supprime les mots multiples
        uniqueVocabularyList = list(set(vocabularyList))

        vectorIndex={}
        offset=0
        #Associate a position with the keywords which maps to the dimension on the vector used to represent this word
        for word in uniqueVocabularyList:
                vectorIndex[word]=offset
                offset+=1
        self.vectorKeywordIndex =vectorIndex
        return vectorIndex  #(keyword:position)
    #4/tf-idf et creer les vecteurs
    #Va renvoyer un vecteur avec le score de chaque terme
    
    def makeVector(self, wordString):
        #Initialise vector with 0's
        vector = [0] * len(self.vectorKeywordIndex)
        wordList = self.tokenise(wordString)
        wordList = self.removeStopWords(wordList)
        N = len(wordString)+1 #+1 POUR EVITER DIVISION ENTRE 0
        for word in wordList:
                """
                Sometimes word is not in vectorKeywordIndex, so we jump it
                """
                try:
                    vector[self.vectorKeywordIndex[word]] += 1/N; #Use simple Term Count Model
                except KeyError:
                    continue
        return vector
    
    def matrixVector(self, documents):
        """ Create the vector space for the passed document strings """
        matrix = [self.makeVector(document) for document in documents]
        transformer = TfidfTransformer(smooth_idf=True)
        tfidf = transformer.fit_transform(matrix)       
        self.documentVectors = tfidf.toarray().tolist()
        #print("Matrice des vecteurs de chaque paragraphe du document crée")