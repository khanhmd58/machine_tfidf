#!/usr/bin/python
# -*- coding: utf8 -*-
from pyvi.pyvi import ViTokenizer, ViPosTagger
import re, itertools
import math
import pandas as pd

def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bowCount)
    return tfDict

def computeIDF(docList):
    #import math
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


f = open('test/diachi.txt', 'r')
docA= f.read()
f = open('test/ten.txt', 'r')
docB= f.read()
bowA = docA.split(" ")
bowB = docB.split(" ")
wordSet= set(bowA).union(set(bowB))

#I'll create dictionaries to keep my word counts.
wordDictA = dict.fromkeys(wordSet, 0)
wordDictB = dict.fromkeys(wordSet, 0)
print wordDictA

#now I'll count the words in my bags.
for word in bowA:
    wordDictA[word]+=1

for word in bowB:
    wordDictB[word]+=1


#Lastly I'll stick those into a matrix.

#pd.DataFrame([wordDictA, wordDictB])


tfBowA = computeTF(wordDictA, bowA)
tfBowB = computeTF(wordDictB, bowB)

idfs = computeIDF([wordDictA, wordDictB])

tfidfBowA =  computeTFIDF(tfBowA, idfs)
tfidfBowB = computeTFIDF(tfBowB, idfs)
print "/////////////"
for word,val in tfidfBowA.items():
	if tfidfBowA[word] == 0:
		del tfidfBowA[word]

for word,val in tfidfBowA.items():
	print word,val

print "/////////////"
for word,val in tfidfBowB.items():
	if tfidfBowB[word] == 0:
		del tfidfBowB[word]

for word,val in tfidfBowB.items():
	print word,val