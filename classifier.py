# Michael Wattendorf
# 4 February 2016
# Hackerrank Question Classifier Challenge
#############################################
# training data is a json file of the form:
# topic, question, excerpt:
# GOAL, predict topic given question & excerpt
import json
from pprint import pprint
import nltk
from nltk import word_tokenize
from nltk.corpus import stopwords
from sys import stdin

data = []
with open('training.json') as data_file:    
	for line in data_file:
		data.append(json.loads(line))

# First, want to make a list of ALL WORDS in the training dataset
# the nltk package has several tokenizers, one that makes sense
# to apply here is the word_tokenizer, which parses the sentance
# into words. 
all_words_list = {}
for f in data[1:]:
	newWords1 = nltk.word_tokenize(f['excerpt'])
	for word in newWords1:
		# Removing stopwords, which will be uninformative and dilute our model
		if word not in all_words_list and word not in stopwords.words("english"):
			all_words_list[word] = 1
	newWords2 = nltk.word_tokenize(f['question'])
	for word in newWords2:
		if word not in all_words_list and word not in stopwords.words("english"):
			all_words_list[word] = 1

# If we limit to the top 2000 words, we can use these as features
# this will help eliminate the long tail of words that only
# appear once
all_words = nltk.FreqDist(w.lower() for w in all_words_list.keys())
word_features = list(all_words)[:2000] # 

# we then need to build a feature extractor which takes
# the tokenized text of a question and turns it into a feature set
def extract_features(question,excerpt): 
    document_words = set(question) | set(excerpt)
    features = {}
    for word in word_features:
        features[u"{0}".format(word)] = (word in document_words)
    return features

# we can now build our training data by using the feature extractor
# and the labels assigned to each question in the training set
X_train = []
Y_train = []
train = []
for f in data[1:]:
	feat = extract_features(nltk.word_tokenize(f['excerpt']),nltk.word_tokenize(f['question']))
	topic = str(f['topic'])
	train.append([feat,topic])

# tested two popular classifiers, the Naive Bayes and Decision Tree
# classifiers, as implemented by the nltk package
classifierNB = nltk.classify.NaiveBayesClassifier.train(train)
#classifierDT = nltk.DecisionTreeClassifier.train(train)

# to select a classifier, I tested each on the input00.txt file 
# and compared the results to the output00.txt file
#outputNB = []

#outputDT = []
#with open('input00.txt') as data_file:
#	N = int(data_file.readline())
#	for i in range(N):
#		nextSample = json.loads(data_file.readline())
#		ept = nltk.word_tokenize(nextSample['excerpt'])
#		qsn = nltk.word_tokenize(nextSample['question'])
#		outputNB.append(classifierNB.classify(extract_features(qsn,ept)))
		#outputDT.append(classifierDT.classify(extract_features(qsn,ept)))

#f = open('outNB_2.txt','w')
#for o in outputNB:
#	f.write(o+"\n")
#f.close()

N = int(stdin.readline())
for line in stdin:
	nextSample = json.loads(line)
	ept = nltk.word_tokenize(nextSample['excerpt'])
	qsn = nltk.word_tokenize(nextSample['question'])
	print(nltk.classify(extract_features(qsn,ept)))


