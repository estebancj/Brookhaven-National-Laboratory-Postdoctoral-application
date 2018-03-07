"""
Creator: Esteban Castillo Juarez
Date: 26/02/2018 

Program that predicts a sentiment (positive,
negative or neutral) based in the supervised learning
theory.

First, a model is created from training samples. Later
for each test vector a sentiment is predicted using
the classification model.
"""

import codecs
import re
import sys
import pickle
import numpy as np
from sklearn import svm
from sklearn.metrics import precision_score
from sklearn.metrics import accuracy_score

NgramType=3
NgramNumber=150

inputFile="trainingVectors-"+str(NgramType)+"-"+str(NgramNumber)+".txt"
inputFile2="testVectors-"+str(NgramType)+"-"+str(NgramNumber)+".txt"
inputFile3="goldStandar.qrel"
outputFile="Model-"+str(NgramType)+"-"+str(NgramNumber)+".txt"

#try:
temp=[]
temp2=[]
trainingVectors=[]
testVectors=[]
sentimentTag=[]
goldstandarTag=[]
testResults=[]

with codecs.open(inputFile,"r","utf-8") as file:
        for line in file:
          elements=line.split(",")
          vector=elements[0:len(elements)-1]
          trainingVectors.append([int(i) for i in vector])
          sentimentTag.append((elements[len(elements)-1]).rstrip())

with codecs.open(inputFile2,"r","utf-8") as file:
        for line in file:
          vector=line.split(",")
          vector[len(vector)-1]=vector[len(vector)-1].rstrip()
          temp.append([[int(i) for i in vector]])

with codecs.open(inputFile3,"r","utf-8") as file:
        for line in file:
          elements=line.split("	")
          elements[1]=elements[1].rstrip()
          if elements[1]!="NONE":
              temp2.append(elements[1])

#Eliminate the NONE elements from the dataset
for x,y in zip(temp,temp2):
    if y!="NONE":
        testVectors.append(x)
        goldstandarTag.append(y)
               
# SVC with polynomial (degree 3) kernel
C = 1.0
clf= poly_svc = svm.SVC(kernel='poly', degree=3, C=C)
#training phase (model construction)
clf.fit(trainingVectors, sentimentTag)
#Model serialization
pickle.dump(clf, open(outputFile, "wb"))
#in case of loading the object use: dump = pickle.load(outputFile)
    
#Testing phase
for vector in testVectors:
    testResults.append(clf.predict(vector)[0])
    
print "Model Accuracy: "+str(accuracy_score(goldstandarTag,testResults))
print "Model micro presicion: "+str(precision_score(goldstandarTag,testResults, average='micro'))
print "Model macro presicion: "+str(precision_score(goldstandarTag,testResults, average='macro'))
print "Model weighted presicion: "+str(precision_score(goldstandarTag,testResults, average='weighted'))
