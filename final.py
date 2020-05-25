import re, math
from collections import Counter

docs = 0
i=1
j = int(input ("Give me number of files :\n")) #zitw arithmo arxeiwn
file = list(range(10))
doc = list(range(10))
for i in range (1,j+1) :
        file[i] = input(" Give me a file:\n ")
        doc[i] = file[i]
        file[i] = open(file[i], 'r').read()

def vectorize(file):  # xwrizw tis lekseis
    words = re.split(r'\W+', file)
    #print (Counter(words))
    return Counter(words)

def yp(doc1, doc2):  # typos similarity
    x1 = sum([doc1[x] * doc2[x] for x in set(doc1.keys()) & set(doc2.keys())])
    x2 = math.sqrt(sum([doc1[x] ** 2 for x in doc1.keys()])) * math.sqrt(sum([doc2[x] ** 2 for x in doc2.keys()]))
    return (x1) / x2

similarity = list (range(10))     
y=0
i2=1
ap = 1
static=0

while (i2 < j ):  #ypologismos similarity gia ta documents
  i = i2
  static = i2
  i2 = i2 + 1
  while (i<j):
    similarity[ap] = yp(vectorize(file[static]), vectorize(file[i+1]))
    doc[ap]= doc[static] ,doc [ i +1]
    print ('similarity:',ap, similarity[ap])  #ektipwnw ta similarity me seira
    i= i + 1
    ap = ap +1

k = int(input("Give me the Κ number:\n"))     #zitw ton arithmo twn pio similar documents

for i in range (1,j):
      if similarity[i] < similarity[i+1]:
              x = doc[i+1]
              doc[i+1]=doc[i]
              doc[i]=x
for i in range (1,k):
 print('The most similar documents are:', doc[i])   #ektipwnw ta top-k most similar documents
       



