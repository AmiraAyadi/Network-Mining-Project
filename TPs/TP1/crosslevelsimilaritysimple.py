import math

listofpairs=[]
freq = {}

f = open("SemEval-2014_Task-3/data/test/phrase2word.test.input.tsv")
for line in f.readlines():
  pairs = [(line.split("\t")[1],x) for x in line.split("\t")[0].split()]
  listofpairs.append(pairs)
  freq[pairs[0][0]] = 0
  for x in pairs:
    freq[x[1]] = 0
    freq[x] = 0

f = open("filtered.txt")
for line in f:
  for w in freq:
    if isinstance(w, tuple) and w[0] in line and w[1] in line:
      freq[w]+=1
    elif isinstance(w, str) and w in line:
      freq[w]+=1

for pairs in listofpairs:
  pmi = 0.0
  for pair in pairs:
    pmi += math.log((freq[pair])/float(freq[pair[0]]*freq[pair[1]])) if freq[pair[0]]*freq[pair[1]] > 0 and  freq[pair] > 0 else 0.0
  pmi /=float(len(pairs))
  print pmi



