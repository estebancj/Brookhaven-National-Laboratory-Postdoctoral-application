"""
Creator: Esteban Castillo Juarez
Date: 26/02/2018 

Program that eliminates all elements that
are not part of the ASCII encoding and also
URLs.

Note: the characters "@-?@" are used to separate the
distinct elements in the input and output files
"""


import codecs
import re
import unicodedata
import random

inputFile="test.txt"
outputFile="testClean.txt"

#Function that eliminates accents from Spanish words 
	
def remove_accents(s):
    try:
            return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
    except TypeError:
            return ""     
    except UnicodeDecodeError:
            return ""
    except:
            return ""
try:
    testList=[]
    with codecs.open(inputFile,"r","utf-8") as file:
        for line in file:
            elementList=line.split("@-?@")
            print elementList[0]
            TextWithoutURL=re.sub(r'''(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'".,<>?«»“”‘’]))''',
                               '',elementList[2], flags=re.MULTILINE)
            elements=TextWithoutURL.split(" ")
            wordList=[]
            for x in elements:
                word= re.sub('[^A-Za-z0-9 ]+', '',remove_accents(x.lower()))
                if len(word)>0:
                    wordList.append(word)
            testList.append(elementList[0]+"@-?@"+
                                  elementList[1]+"@-?@"+
                                  " ".join(wordList)+"@-?@"+
                                  elementList[3]+"@-?@"+
                                  elementList[4])        

    with codecs.open(outputFile,"w","utf-8") as file:
         for a in testList:
             file.write(a)
             
except IOError as (errno, strerror):
    print "Input/output error ({0}): {1}".format(errno, strerror)

except:
    print "Unexpected error:", sys.exc_info()[0]   
             
