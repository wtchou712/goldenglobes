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

def remove_punctuation(string):
	string=regex.sub(' ', string)
	return string

def removeIgnored(phrase):
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
	stopset.add('co')
	stopset.add('http')
	#added stopsets
	stopset.add('award')
	for i in range(0,len(words)):
		stopset.add(words[i])
	return stopset

def findTopTweets(award):
	print "     Searching for top tweets..."
	data = []
	with open('gg15mini.json') as f:
	    for line in f:
	        data.append(json.loads(line))

	stopset = removeIgnored(award)

	# this code block creates our corpus of relevant tweets - an array of tweet objects
	award_bigrams = []
	award_unigrams = []
	presenter_bigram = []
	for tweet in data[0]: 
		tweetText = tweet["text"].lower()	
		tweetText = remove_punctuation(tweetText)
		awardTokenNotFound = False
		awardText = remove_punctuation(award.lower())
		# awardTokens = nltk.word_tokenize(award)
		# for token in awardTokens:
		# 	if tweetText.find(token)==-1:#check if the award token is found
		# 		#if not found, change to true
		# 		awardTokenNotFound = True
		if award not in tweetText:
			awardTokenNotFound = True

		if awardTokenNotFound is False:
			#add to array of unigrams
			tweetTokens = nltk.word_tokenize(tweetText)
			for tok in tweetTokens:#add appropriate unigrams
				if tok not in stopset:
					award_unigrams.append(tok)

			#add to array of bigams
			words = re.findall('\w+', tweetText) #seperate the words
			bigrams = zip(words, words[1:]) #create the bigrams
			for bi in bigrams:
				if bi[0] not in stopset and bi[1] not in stopset:
					award_bigrams.append(bi)
					# if presenterTokenNotFound is False:
					# 	presenter_bigram.append(bi)

	fdistUnigram = FreqDist(award_unigrams)
	topUni = fdistUnigram.most_common(30)
	fdistBigram = nltk.FreqDist(award_bigrams)
	topBi = fdistBigram.most_common(30)
	# fdistPresenter = nltk.FreqDist(presenter_bigram)
	# topPresenterBi = fdistPresenter.most_common(10)
	print topUni
	print topBi
	# print topPresenterBi
	return topUni,topBi

def findWinner(topUnigrams, topBigrams, nominees):
	singleWordNom = False
	for nom in nominees: #search nominees to see if any are single words
		checkNom = nltk.word_tokenize(nom)
		if len(checkNom)!=0:
			singleWordNom= True
			break
	for i in range(0,len(topUnigrams)):
		for j in range (0,len(nominees)):
			biPart1 = (topBigrams[i][0])[0]
			biPart2 = (topBigrams[i][0])[1]
			uni = topUnigrams[i][0]
			nominee = nominees[j].lower()
			if singleWordNom:#use unigram search if single words nominee
				if nominee.find(uni)!=-1:
					return nominees[j]
					break
			else:
				if nominee.find(biPart1)!= -1 or nominee.find(biPart2)!=-1:
					return nominees[j]
					break
def findHost(topBigrams):
	for i in range(0,len(topBigrams)):
		biPart1 = (topBigrams[i][0])[0]
		biPart2 = (topBigrams[i][0])[1]
		return biPart1 + " " + biPart2


def findPresenter(winner):
	#winner = remove_punctuation(winner.lower())
	print "Searching for the presenter..."
	print "     Searching for top tweets..."
	data = []
	with open('gg15mini.json') as f:
	    for line in f:
	        data.append(json.loads(line))

	stopset = removeIgnored(winner.lower())
	stopset.add('motion')
	stopset.add('picture')
	#print stopset

	# this code block creates our corpus of relevant tweets - an array of tweet objects
	presenter_bigrams = []
	presenter_unigrams = []
	winnerTokens = nltk.word_tokenize(winner.lower())
	print winnerTokens
	for tweet in data[0]: 
		tweetText = tweet["text"].lower()	
		tweetText = remove_punctuation(tweetText)
		presenterTokenNotFound = False
		for token in winnerTokens:
			if tweetText.find(token)==-1 or tweetText.find('present')==-1:
				#if not found, change to true
				presenterTokenNotFound = True
		# if tweetText.find(winner)==-1 or tweetText.find(winner)==-1:
		# 	presenterTokenNotFound = True

		if presenterTokenNotFound is False:
			print "Possible tweet match found"
			#add to array of unigrams
			tweetTokens = nltk.word_tokenize(tweetText)
			for tok in tweetTokens:#add appropriate unigrams
				if tok not in stopset:
					presenter_unigrams.append(tok)

			#add to array of bigams
			words = re.findall('\w+', tweetText) #seperate the words
			bigrams = zip(words, words[1:]) #create the bigrams
			for bi in bigrams:
				if bi[0] not in stopset and bi[1] not in stopset:
					presenter_bigrams.append(bi)

	fdistUnigram = FreqDist(presenter_unigrams)
	topUni = fdistUnigram.most_common(30)
	fdistPresenter = nltk.FreqDist(presenter_bigrams)
	topBi = fdistPresenter.most_common(10)
	print topUni
	print topBi
	return topUni,topBi
			

