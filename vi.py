#!/usr/bin/python
# -*- coding: utf8 -*-
from pyvi.pyvi import ViTokenizer, ViPosTagger
import re, itertools
import pandas as pd
import math



def computeTF(wordDict, bow):
    tfDict = {}
    bowCount = len(bow)
    for word, count in wordDict.items():
        tfDict[word] = count / float(bowCount)
    return tfDict

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


f = open('test/dia chi.txt', 'r')
str1 = f.read()
z = str1.decode('utf-8')

q = open('test/ten.txt', 'r')
str2 = q.read()
print type(str2)
t = str2.decode('utf-8')
print len(t)
x = ViTokenizer.tokenize(z)
x2 = ViTokenizer.tokenize(t)
#x = ViPosTagger.postagging(ViTokenizer.tokenize(u"Trường đại học Bách Khoa Hà Nội"))

y = x.split(" ")
y2 = x2.split(" ")
aList = []
bList = []

for index in range(len(y)):
    tmp = y[index]
    aList.append(tmp)

for index in range(len(aList)):
    print aList[index]

for index in range(len(y2)):
    tmp = y2[index]
    bList.append(tmp)

for index in range(len(bList)):
    print bList[index]

print "///////////////////////////"
wordSet = set(aList).union(set(bList))

#docA = "the cat sat on my face"
#docB = "the dog sat on my bed"
#bowA = docA.split(" ")
#bowB = docB.split(" ")
wordSet1 = set(aList).union(set(bList))

wordDictA = dict.fromkeys(wordSet1,0)
wordDictB = dict.fromkeys(wordSet1,0)

for word in aList:
	wordDictA[word]+=1

for word in bList:
	wordDictB[word]+=1

print wordDictA

print pd.DataFrame([wordDictA,wordDictB])

#print z

tfBowA = computeTF(wordDictA,aList)
tfBowB = computeTF(wordDictB,bList)

print "////////////"
print pd.DataFrame([tfBowA,tfBowB])
print "////////////12312"
idfs = computeIDF([wordDictA, wordDictB])

for word,value in idfs.items():
    print word,value

tfidfBowA =  computeTFIDF(tfBowA, idfs)
tfidfBowB = computeTFIDF(tfBowB, idfs)

print "/////////////"
print "bitcoint"

for word,val in tfidfBowA.items():
	print word,val

print "/////////////"
print "bongda"
'''for word,val in tfidfBowB.items():
	if tfidfBowB[word] == 0:
		del tfidfBowB[word]

for word,val in tfidfBowB.items():
	print word,val'''
print pd.DataFrame([tfidfBowA,tfidfBowB])
