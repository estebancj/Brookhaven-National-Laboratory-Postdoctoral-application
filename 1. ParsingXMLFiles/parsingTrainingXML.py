"""
Creator: Esteban Castillo Juarez
Date: 26/02/2018 

Program that parse a XML file to a plain txt file
using the Python ElementTree functionality.

Considering a training sentiment file, the
sentiment tags are obtained (positive, negative and
neutral) except for the None tags which are not used
in this experiments.

Note: the characters "@-?@" are used to separate the
distinct elements in the input and output files
"""

import xml.etree.ElementTree as ET
import codecs

tweetDic=[]

inputFile="trainingOriginalFile.xml"
ouput="training.txt"

tree = ET.ElementTree(file=inputFile)
for x in tree.iter(tag='tweet'):
   tempDict={}
   for y in x:
      tempDict[y.tag]=((y.text).replace('\n',' ')).replace('\n',' ')
      if y.tag=="sentiment":
        if (y[0][0].text) != "NONE":
          tempDict[y.tag]=y[0][0].text
          tweetDic.append(tempDict)


with codecs.open(ouput,"w","utf-8") as file:
    for x in tweetDic:
        file.write(x["tweetid"]+"@-?@"+
               x["user"]+"@-?@"+
               x["content"]+"@-?@"+
               x["date"]+"@-?@"+
               x["lang"]+"@-?@"+
               x["sentiment"]+"\n")
