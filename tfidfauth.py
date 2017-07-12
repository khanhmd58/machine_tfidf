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

# code main

# test open all file chi dc file .txt cac file .txt~ k luu dc
files = []
tfidf = []
wordDict = []
newA = []
tf =[]
path = 'training/negative'

obj2=open(path,"r")
str1 = obj2.read()
files = str1.split("\n\n")
obj2.close()
for val in files:
    print "//////"
    print val
    print "/////"


for value in range(len(files)):
	decode = files[value].decode('utf-8')
	tmp = ViTokenizer.tokenize(decode)
	split = tmp.split(" ")
	newA.append(split)

# mang 2 chieu luu tach tu 
union = set.union(*(set(value) for value in newA))
for val in range(len(files)):
	wordDict.append(dict.fromkeys(union, 0))

for num in range(len(newA)):
	for word in newA[num]:
		wordDict[num][word]+=1

#tf
for val in range(len(wordDict)):
	tfBow = computeTF(wordDict[val],newA[val])
	tf.append(tfBow)

#idf
idfs = computeIDF(wordDict)

#tfidf
for val in tf: 
	tfidfBow =  computeTFIDF(val, idfs)
	tfidf.append(tfidfBow)


'''for value in tfidf:
    for word,val in value.items():
        print word.encode('utf8'),val
    print "==================================================================================="
'''

print "==================================================================================="

print pd.DataFrame(tfidf);

x = dict.fromkeys(tfidf[0].keys(),0)

vt_Neg = []

for num in range(len(tfidf)):
    for word in tfidf[num]:
        x[word]+=tfidf[num][word]

for word,val in x.items():
    vt_Neg.append(x[word])
   
