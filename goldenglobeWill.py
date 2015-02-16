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

def findtags(tag_prefix, tagged_text):
    """
    Find tokens matching the specified tag_prefix
    """
    cfd = nltk.ConditionalFreqDist((tag, word) for (word, tag) in tagged_text
                                  if tag.startswith(tag_prefix))
    return dict((tag, cfd[tag].keys()[:5]) for tag in cfd.conditions())

def removeIgnored(phrase):
	words = phrase.lower().split(' ')
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
	stopset.add('cecil')
	stopset.add('demille')
	stopset.add('perezhilton')
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
	award_bigrams = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
					 [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
	award_unigrams =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
					 [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

	counter = 0
	for tweet in data[0]: 
		tweetText = tweet["text"].lower()	
		tweetText = remove_punctuation(tweetText)

		for i in range(0, len(awards)):
			award = remove_punctuation(awards[i].lower())
			if i <= 25:
				awardTokenNotFound = False
				# award = remove_punctuation(awards[i].lower())

				if award not in tweetText:
					awardTokenNotFound = True
				if awardTokenNotFound is False:
					print "Possible matching tweet found"
					tweetTokens = nltk.word_tokenize(tweetText)
					words = re.findall('\w+', tweetText) #seperate the words
					bigrams = zip(words, words[1:]) #create the bigrams


					#add to array of unigrams
					for tok in tweetTokens:#add appropriate unigrams
						if tok not in award_stopsets[i]:
							award_unigrams[i].append(tok)

					#add to array of bigams
					for bi in bigrams:
						if bi[0] not in award_stopsets[i] and bi[1] not in award_stopsets[i]:
							award_bigrams[i].append(bi)
			else:
				awardTokenNotFound = False
				if award not in tweetText:
					awardTokenNotFound = True
				if awardTokenNotFound is False:
					lTokens = nltk.word_tokenize(tweet['text'])
					lTokens = nltk.pos_tag(lTokens)

					lTagDict = findtags('NNP', lTokens)
					if lTagDict.has_key("NNP"):
						words = lTagDict["NNP"]
						bigrams = zip(words,words[1:])
						for bi in bigrams:
							if bi[0].lower() not in award_stopsets[i] and bi[1].lower() not in award_stopsets[i]:
								award_bigrams[i].append(bi)

					# for tag in sorted(lTagDict):
					#     print tag, lTagDict[tag]

					for token in lTokens:
						if token[1] == 'NNP':
							if token[0].lower() not in award_stopsets[i]:
								award_unigrams[i].append(token[0])
					
		counter+=1
		print "Tweets scanned: " + str(counter)

	print "Finished searching tweets, now determining winners..."

	winners =[]
	for i in range(0,len(awards)):
		if i is 25:
			#find the cecile winner on own
			fdistBigram = nltk.FreqDist(award_bigrams[i])
			topBi = fdistBigram.most_common(10)
			# print "top bigrams for Cecil B. DeMille award"
			# print topBi
			biPart1 = (topBi[0][0])[0]
			biPart2 = (topBi[0][0])[1]
			winner = biPart1 + " " + biPart2
			winners.append(winner)
		elif i >= 26: 
			# #find the winners for the fun goals
			# fdistBigram = nltk.FreqDist(award_bigrams[i])
			# topBi = fdistBigram.most_common(10)
			# print "top bigrams for " + awards[i]
			# print topBi
			# biPart1 = (topBi[0][0])[0]
			# biPart2 = (topBi[0][0])[1]
			# winner = biPart1 + " " + biPart2
			fdistUnigram = FreqDist(award_unigrams[i])
			topUni = fdistUnigram.most_common(10)
			fdistBigram = nltk.FreqDist(award_bigrams[i])
			topBi = fdistBigram.most_common(10)
			print '================================================'
			print "top unigrams for " + awards[i]
			print topUni
			print '================================================'
			print "top bigrams for " + awards[i]
			print topBi
			#winners.append(winner)
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
			#print "Using unigrams instead..."
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
				




			

