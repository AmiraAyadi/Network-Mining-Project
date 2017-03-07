import nltk.collocations
import collections
f = open("filtered.txt")
documents = " ".join([line for line in f.readlines()])
f.close()
bgm = nltk.collocations.BigramAssocMeasures()
finder = nltk.collocations.BigramCollocationFinder.from_words(documents.split())
ignored_words = nltk.corpus.stopwords.words('english')
#finder.apply_word_filter(lambda w: len(w) < 3 or w.lower() in ignored_words)
pmi = finder.score_ngrams(bgm.pmi)
dicpmi = {}
for x in pmi:
  dicpmi[x[0]]=x[1]
f = open("SemEval-2014_Task-3/data/test/phrase2word.test.input.tsv")
for line in f.readlines():
  pairs = [(line.split("\t")[1],x) for x in line.split("\t")[0].split()]
  val = [dicpmi[x] for x in pairs if x in dicpmi]
  val.extend([dicpmi[(x[1],x[0])] for x in pairs if (x[1],x[0]) in dicpmi])
  print sum(val)/float(len(val)) if len(val)>0 else 0.0

