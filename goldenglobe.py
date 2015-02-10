import json
import nltk 
import re, string
regex = re.compile('[%s]' % re.escape(string.punctuation))
from pprint import pprint
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.probability import *
from nltk import bigrams
from nltk.tokenize import RegexpTokenizer
from nltk.collocations import *
from collections import Counter

def remove_punct(string):
	string=regex.sub(' ', string)
	return string

def createstopset(phrase):
	words = phrase.split(' ')
	stopset = set(stopwords.words('english'))
	stopset.add('best')
	stopset.add('golden')
	stopset.add('globes')
	stopset.add('goldenglobes')
	stopset.add('goldenglobe')
	stopset.add('rt')
	stopset.add('actor')
	stopset.add('actress')
	for x in range(0,len(words)):
		stopset.add(words[x])
	return stopset

def findinfo(phrase):
	print "================================================="
	print "\n"
	data = []
	with open('gg2013.json') as f:
	    for line in f:
	        data.append(json.loads(line))

	# this code block creates our corpus of relevant tweets - an array of tweet objects
	corpus = []
	for tweet in data[0]: 
		text = tweet["text"].lower()	
		text = remove_punct(text)
		#tokens = tokenize(text)
		if phrase in text:
			corpus.append(text)
		#if "best supporting actor television" in text:
		#	corpus.append(text)

		#	print "\n"
		# corpus.append(text)
		# print tokens

	# this code block turns tweets into unigrams and bigrams and then stores them in token_array and bigram_array2
	token_array = []
	bigram_array = []
	bigram_array2 = []
	for x in range(0,len(corpus)):
		#print corpus[x]
		sentence = corpus[x]
		tokens = nltk.word_tokenize(sentence)
		bigrams = nltk.bigrams(sentence)
		token_array.append(tokens)
		#pairs = [ ", ".join(pair) for pair in nltk.bigrams(tokens)]	
		#print bigrams
		#bigram_array.append(pairs)
		words = re.findall('\w+', sentence)
		temp = zip(words,words[1:]) # originally had Counter() wrapped around zip(...)
		bigram_array2.append(temp)








	#stopset = set(stopwords.words('english')) # this is the creation of our stopset -- words we don't want to include
	stopset = createstopset(phrase)
	'''stopset.add('best')
	stopset.add('golden')
	stopset.add('globes')
	stopset.add('goldenglobes')
	stopset.add('goldenglobe')
	stopset.add('rt')
	stopset.add('actor')
	stopset.add('actress')







	stopset.add('motion')
	stopset.add('picture')
	stopset.add('comedy')
	stopset.add('musical')'''

	final_array = [] # this array will store all unigrams 
	no_common_words_array = []
	#print len(token_array)
	for x in range(0,len(token_array)):
		#print corpus[x]
		token_list = token_array[x]
		for y in range(0,len(token_list)):
			one_token = token_list[y]
			temp_array = []
			if one_token not in stopset:
				####print one_token	
				final_array.append(one_token)
				#print one_token
				#temp_array.append(one_token)
				#final_array.append(temp_array[0])
				#no_common_words = (token_list)
				#no_common_words_array.append(no_common_words)

	all_bigrams_array = [] # this array will store all bigrams
	for x in range(0,len(bigram_array2)):
		#print corpus[x]
		bigram_collection = bigram_array2[x]
		#print bigram_collection
		#print "\n"
		for y in range(0,len(bigram_collection)):
			one_bigram = bigram_collection[y]
			#print one_token
			temp_array = []
			# ADD CODE FOR STOPSET USING IF STATEMENT BELOW... need to check a and b in tuple (a,b) for stopset match
			if one_bigram[0] not in stopset:
				if one_bigram[1] not in stopset:
				####print one_token	
					all_bigrams_array.append(one_bigram)

	#print "UNIGRAM FREQUENCY OUTPUT"
	#print all_bigrams_array  # this is an array containing all bigrams... 
	fdist = FreqDist(final_array)
	top5uni = fdist.most_common(20)
	#print fdist.most_common(20)
	#print "================================================="
	#print "\n"
	#print "BIGRAM FREQUENCY OUTPUT"
	# This is the frequency counter for bigrams... all_bigrams_array is a list of all bigrams from queried tweets 
	fdist1 = nltk.FreqDist(all_bigrams_array)
	top5bi = fdist1.most_common(20)
	#print fdist1.most_common(20)
	#print "================================================="

	return top5uni,top5bi
