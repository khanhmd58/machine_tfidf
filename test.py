#!/usr/bin/python
# -*- coding: utf8 -*-
from pyvi.pyvi import ViTokenizer, ViPosTagger
import re, itertools
import math,os
import pandas as pd

#define function tf
def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bowCount)
    return tfDict

#define function idf
def computeIDF(docList):
    import math
    idfDict = {}
    N = len(docList)
    #counts the number of documents that contain a word w
    idfDict = dict.fromkeys(docList[0].keys(),0)
    for doc in docList:
        for word, val in doc.items():
            if val > 0:
                idfDict[word] +=1
                
    #divide N by denominator above, take the log of that
    for word, val in idfDict.items():
        idfDict[word]= math.log(N / float(val)) 

    return idfDict

def computeTFIDF(tfBow, idfs):
    tfidf = {}
    for word, val in tfBow.items():
        tfidf[word] = val * idfs[word]
    return tfidf

aList = [6,7,8,9,10,11,12]
bList = [1,2,3,4,5,6,7,8]
cList = [10,11,12,13,'a','b','d']
dList = [aList,bList,cList]
wordDict = []
z=[]
wordSet = set(cList).union(set(bList),set(aList))
print wordSet

q =  []
#f = open(q[0], 'r')
#str1 = f.read()
#print str1

for filename in os.listdir("test/"):
    q.append(filename)

for value in q:
    f = open(value, 'r')
    str1 = f.read()
    z.append(str1)



# test open all file chi dc file .txt cac file .txt~ k luu dc

print "//////////"

print "//////////"
#input la file out put la string

print z
print len(z)
print z[0]
print type(z[0])
k = z[0].decode('utf-8')
x = ViTokenizer.tokenize(k)
print x
newA = []
for value in range(len(z)):
	x = z[value].decode('utf-8')
	tmp = ViTokenizer.tokenize(x)
	k = tmp.split(" ")
	newA.append(k)

print newA

# mang 2 chieu luu tach tu 
y = set.union(*(set(x) for x in newA))
print y
for val in range(len(z)):
	wordDict.append(dict.fromkeys(y, 0))

print wordDict
print "==================================================================================="
for num in range(len(newA)):
	for word in newA[num]:
		wordDict[num][word]+=1		
print "==================================================================================="
print wordDict
print pd.DataFrame(wordDict)
print "==================================================================================="


#tf
tf =[]
for val in range(len(wordDict)):
	tfBow = computeTF(wordDict[val],newA[val])
	tf.append(tfBow)
print "aaaaaaaaaaaaaaaaaaaaTFFFFFF"
print tf
print pd.DataFrame(tf)

#idf
idfs = computeIDF(wordDict)
print "==================================================================================="
for word,value in idfs.items():
	print word,value

#tfidf
tfidf = []

for val in tf: 
	tfidfBow =  computeTFIDF(val, idfs)
	tfidf.append(tfidfBow)

for value in tfidf:
	for word,val in value.items():
		if value[word] == 0:
			del value[word]

print "==================================================================================="
print pd.DataFrame(tfidf)