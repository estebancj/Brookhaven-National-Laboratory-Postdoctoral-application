"""
Creator: Esteban Castillo Juarez
Date: 26/02/2018 

Program that parse a XML file to a plain txt file
using the Python ElementTree functionality.

Considering a test sentiment file, there is not extracted
a sentiment tag.

Note: the characters "@-?@" are used to separate the
distinct elements in the input and output files
"""

import xml.etree.ElementTree as ET
import codecs

inputFile="testOriginalFile.xml"
ouput="test.txt"

tweetDic=[]

tree = ET.ElementTree(file=inputFile)
for x in tree.iter(tag='tweet'):
   tempDict={}
   for y in x:
      tempDict[y.tag]=((y.text).replace('\n',' ')).replace('\n',' ')
   tweetDic.append(tempDict)


with codecs.open(ouput,"w","utf-8") as file:
    for x in tweetDic:
        file.write(x["tweetid"]+"@-?@"+
               x["user"]+"@-?@"+
               x["content"]+"@-?@"+
               x["date"]+"@-?@"+
               x["lang"]+"\n")
