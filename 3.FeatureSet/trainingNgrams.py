"""
Creator: Esteban Castillo Juarez
Date: 26/02/2018 

Program that obtains a feature Set (Machine Learning)
based on extracting small word-windows called N-grams
(NLP)

For each N-gram the frequency of occurrence of that word
in all training texts is obtained (Descending order).


Note: the characters "@-?@" are used to separate the
distinct elements in the input and output files
"""

import codecs
import re
import sys
import operator
#NLP packages
import nltk
from nltk import word_tokenize
from nltk.util import ngrams

#N-gram window size
NgramType=3

inputFile="trainingClean.txt"
outputFile="feature"+str(NgramType)+"Gram.txt"

try:
    nGramFeatureSet={}
    with codecs.open(inputFile,"r","utf-8") as file:
        for line in file:
            elementList=line.split("@-?@")
            print elementList[0]
            words = nltk.word_tokenize(elementList[2])
            nGrams=ngrams(words,NgramType)
            for nGram in nGrams:
                nGram=' '.join(e for e in nGram)   
                if nGram in nGramFeatureSet:
                    nGramFeatureSet[nGram]=nGramFeatureSet[nGram]+1
                else:
                    nGramFeatureSet[nGram]=1     
    nGramFeatureSetSort = sorted(nGramFeatureSet.items(),
                                 key=operator.itemgetter(1),
                                 reverse=True)


    with codecs.open(outputFile,"w","utf-8") as file:
         for a in nGramFeatureSetSort:
             file.write(a[0]+"@-?@"+str(a[1])+"\n")
              
except IOError as (errno, strerror):
    print "Input/output error ({0}): {1}".format(errno, strerror)

except:
    print "Unexpected error:", sys.exc_info()[0]     
             
