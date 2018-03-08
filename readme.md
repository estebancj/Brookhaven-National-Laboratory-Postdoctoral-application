## Sentiment analysis example for the Brookhaven National Laboratory Postdoctoral application

The purpose of this example is to demonstrate my ability to collect, work with, clean, and classify a 
set of text documents applied to a sentiment analysis problem in which the idea is to find the polarity
of text documents based on the lexical-syntactical structure of documents. 

This is one of my first attempts to obtain the sentiment attached to peer-review comments related to 
text documents in a data repository like Dspace (where digital document collections and communities are managed).

Example features:

* All the programs (files *.py) were implemented in Python 2.7
* The dataset used are part of a Spanish collection of tweets from TASS 2018 http://www.sepln.org/workshops/tass/
* The  Python packages required to run the programs are the following:

	* Numpy (classification) http://www.numpy.org/
	* scikit-learn (classification) http://scikit-learn.org/stable/
	* NLTK (NLP techniques) https://www.nltk.org/
	* CLips pattern (NLP techniques) https://www.clips.uantwerpen.be/pattern

There are five folders that show the different steps used to clean, pre-process, represent and classify a set of 
text documents from some known samples:

	1. ParsingXMLFiles
	2. CleaningTxtFiles
	3. FeatureSet
	4. VectorRepresentation
	5. TrainingTesting
 
## Dspace ontology work

Additionally to the Python examples, an ontology (OntologyExample.owl file) created in protégé https://protege.stanford.edu/ is 
presented as an example of an ideal semantic modeling for a repository in which I’m involved as a postdoctoral researcher.

It is important to notice that the ontology concepts and definitions are in Spanish, considering that the main 
purpose of this taxonomy is to model the relationships of text documents and authors in a Mexican university scope 
(Universidad de las Américas Puebla http://www.udlap.mx/inicio.aspx and http://www.udlap.mx/repositorio/) where 
there is a variety of documents such as thesis, articles, books, research data collections, etc.
