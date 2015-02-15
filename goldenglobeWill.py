import json
import time
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
	stopset.add('cecile')
	stopset.add('demille')
	#added stopsets
	stopset.add('award')
	for i in range(0,len(words)):
		stopset.add(words[i])
	return stopset

def searchTweets(awards,nominees,inputFile):
	start_time = time.time()
	print "Searching for top tweets..."
	data = []
	with open('../' + inputFile) as f:
	    for line in f:
	        data.append(json.loads(line))
	award_stopsets = []
	for award in awards:
		stopset = removeIgnored(award)
		award_stopsets.append(stopset)

	# this code block creates our corpus of relevant tweets - an array of tweet objects
	award_bigrams = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
	award_unigrams =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

	counter = 0
	for tweet in data[0]: 
		tweetText = tweet["text"].lower()	
		tweetText = remove_punctuation(tweetText)
		awardText = remove_punctuation(award.lower())
		# awardTokens = nltk.word_tokenize(award)
		# for token in awardTokens:
		# 	if tweetText.find(token)==-1:#check if the award token is found
		# 		#if not found, change to true
		# 		awardTokenNotFound = True
		#print "Determining if tweet matches an award..."

		for i in range(0, len(awards)):
			awardTokenNotFound = False
			award = remove_punctuation(awards[i].lower())
			#print award
			#print "Determining match with award" + str(i+1)

			if award not in tweetText:
				awardTokenNotFound = True

			if awardTokenNotFound is False:
				print "Possible matching tweet found"
				tweetTokens = nltk.word_tokenize(tweetText)

				words = re.findall('\w+', tweetText) #seperate the words
				bigrams = zip(words, words[1:]) #create the bigrams

				#add to array of unigrams
				# tweetTokens = nltk.word_tokenize(tweetText)
				for tok in tweetTokens:#add appropriate unigrams
					if tok not in award_stopsets[i]:
						award_unigrams[i].append(tok)

				#add to array of bigams
				# words = re.findall('\w+', tweetText) #seperate the words
				# bigrams = zip(words, words[1:]) #create the bigrams
				for bi in bigrams:
					if bi[0] not in award_stopsets[i] and bi[1] not in award_stopsets[i]:
						award_bigrams[i].append(bi)

			#print "Finished with current tweet..."		

		counter+=1
		print "Tweets scanned: " + str(counter)

	print "Finished searching tweets, now determining winners..."

	winners =[]
	for i in range(0,len(awards)):
		if i is 25:
			#find the cecile winner on own
			fdistBigram = nltk.FreqDist(award_bigrams[25])
			topBi = fdistBigram.most_common(10)
			print "top bigrams for Cecile B. DeMille award"
			print topBi
			biPart1 = (topBi[0][0])[0]
			biPart2 = (topBi[0][0])[1]
			winner = biPart1 + " " + biPart2
			winners.append(winner)
		else:
			fdistUnigram = FreqDist(award_unigrams[i])
			topUni = fdistUnigram.most_common(10)
			fdistBigram = nltk.FreqDist(award_bigrams[i])
			topBi = fdistBigram.most_common(10)
			# print topUni
			# print topBi
			results = findWinner(topUni,topBi, nominees[i])
			winner = results[0]
			nominees[i]=results[1]
			winners.append(winner)

	# #find the cecile winner on own
	# fdistBigram = nltk.FreqDist(award_bigrams[25])
	# topBi = fdistBigram.most_common(10)
	# print "top bigrams for Cecile B. DeMille award"
	# print topBi
	# biPart1 = (topBi[0][0])[0]
	# biPart2 = (topBi[0][0])[1]
	# winner = biPart1 + " " + biPart2
	# winners.append(winner)

	elapsed_time = time.time() - start_time
	print "Search length: " + str(elapsed_time)
	#print winners
	return winners,nominees

def findWinner(topUnigrams, topBigrams, nominees):
	# print topUnigrams
	# print topBigrams
	singleWordNom = False
	for nom in nominees: #search nominees to see if any are single words
		checkNom = nltk.word_tokenize(nom)
		if len(checkNom)==1:
			singleWordNom= True
			print "Using unigrams instead..."
			break
	# for i in range(0,len(topUnigrams)):
	# 	for j in range (0,len(nominees)):
	# 		biPart1 = (topBigrams[i][0])[0]
	# 		biPart2 = (topBigrams[i][0])[1]
	# 		uni = topUnigrams[i][0]
	# 		nominee = nominees[j].lower()
	# 		if singleWordNom:#use unigram search if single words nominee
	# 			if nominee.find(uni)!=-1:
	# 				return nominees[j]
	# 				break
	# 		else:
	# 			if nominee.find(biPart1)!= -1 or nominee.find(biPart2)!=-1:
	# 				return nominees[j]
	# 				break
	if singleWordNom:
		for i in range(0,len(topUnigrams)):
			for j in range (0,len(nominees)):
				uni = topUnigrams[i][0]
				nominee = nominees[j].lower()
				if nominee.find(uni)!=-1:
					winner = nominees[j]
					nominees.remove(winner)
					return winner,nominees
					break
	else:
		for i in range(0,len(topBigrams)):
			for j in range (0,len(nominees)):
				biPart1 = (topBigrams[i][0])[0]
				biPart2 = (topBigrams[i][0])[1]
				nominee = nominees[j].lower()
				if nominee.find(biPart1)!= -1 or nominee.find(biPart2)!=-1:
					winner = nominees[j]
					nominees.remove(winner)
					return winner,nominees
					break
				

def findCecileWinner(topUnigrams, topBigrams):
	print topUnigrams
	print topBigrams
	for i in range(0,len(topBigrams)):
		biPart1 = (topBigrams[i][0])[0]
		biPart2 = (topBigrams[i][0])[1]
		if nominee.find(biPart1)!= -1 or nominee.find(biPart2)!=-1:
			return nominees[j]
			break
				



			

