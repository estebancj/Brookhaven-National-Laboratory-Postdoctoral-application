"""
Creator: Esteban Castillo Juarez
Date: 26/02/2018 

Program that transform each text (training) into a vector
representation taking the frequency of occurrence of the N
best PoS tags ngrams

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
from pattern.es import parse

NgramType=3
NgramNumber=150
inputFile="feature"+str(NgramType)+"GramPoSTag.txt"
inputFile2="testClean.txt"
outputFile="testVectors-"+str(NgramType)+"-"+str(NgramNumber)+"PoSTag.txt"

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
    with codecs.open(inputFile2,"r","utf-8") as file:
        for line in file:
            nGramList=[]
            vector=[]
            elementsList=line.split("@-?@")
            print elementsList[0]
            elementsParser=parse(elementsList[2])
            PoSTagList=[]
            for PoSTag in elementsParser.split(" "):
                elements=PoSTag.split("/")
                PoSTagList.append(elements[1])
            nGrams=ngrams(PoSTagList,NgramType)
            for nGram in nGrams:
                nGram=' '.join(e for e in nGram)
                nGramList.append(nGram)
            for nGram in nGramFeatureSet:
                vector.append(nGramList.count(nGram))    
            vectorList.append(vector) 

                         
    with codecs.open(outputFile,"w","utf-8") as file:
         for x in vectorList:
             file.write(','.join(map(str, x))+"\n")
     
except IOError as (errno, strerror):
    print "Input/output error ({0}): {1}".format(errno, strerror)

except:
    print "Unexpected error:", sys.exc_info()[0]    
              
             
