"""
Creator: Esteban Castillo Juarez
Date: 26/02/2018 

Program that transform each text (training) into a vector
representation taking the frequency of occurrence of the N
best ngrams

Note: the characters "@-?@" are used to separate the
distinct elements in the input and output files
"""


import codecs
import re
import sys
import operator
import nltk
from nltk.util import ngrams
from collections import Counter
from nltk import word_tokenize


NgramType=3
NgramNumber=150
inputFile="feature"+str(NgramType)+"Gram.txt"
inputFile2="trainingClean.txt"
outputFile="trainingVectors-"+str(NgramType)+"-"+str(NgramNumber)+".txt"

try: 
    nGramFeatureSet=[]
    counter=0
    with codecs.open(inputFile,"r","utf-8") as file:
        for line in file:
            counter=counter+1
            if counter <= NgramNumber:
                elementsList=line.split("@-?@")
                nGramFeatureSet.append(elementsList[0])
            else:
                break

    vectorList=[]
    sentimentTags=[]
    with codecs.open(inputFile2,"r","utf-8") as file:
        for line in file:
            nGramList=[]
            vector=[]
            elementsList=line.split("@-?@")
            print elementsList[0]
            sentimentTags.append(elementsList[5])
            words = nltk.word_tokenize(elementsList[2])
            nGrams=ngrams(words,NgramType)
            for nGram in nGrams:
                nGram=' '.join(e for e in nGram)
                nGramList.append(nGram)
            for nGram in nGramFeatureSet:
                vector.append(nGramList.count(nGram))    
            vectorList.append(vector)    
                                
    with codecs.open(outputFile,"w","utf-8") as file:
         for x,y in zip(vectorList,sentimentTags):
             file.write(','.join(map(str, x))+","+y)
            
except IOError as (errno, strerror):
    print "Input/output error ({0}): {1}".format(errno, strerror)

except:
    print "Unexpected error:", sys.exc_info()[0]    
             
