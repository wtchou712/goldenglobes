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

def remove_duplicates(values):
    output = []
    seen = set()
    for value in values:
        # If value has not been encountered yet,
        # ... add it to both list and set.
        if value not in seen:
            output.append(value)
            seen.add(value)
    return output

ignoredWords = ['best', 'golden', 'globes', 'goldenglobes', 'goldenglobe', 'rt', 'actor', 'actress', 'co' , 'http', 'cecil', 'demille', 'perezhilton', 'wins',
				'wtf', 'oscar', 'congratulations', 'director', 'category', 'right', '@', 'nbc', 'gives', 'academy', 'award', 'amp', 'eonline', 'list', 'photos',
				'face', 'normal','wow','see','fashion','red','carpet','tonight','styles','stylist', 'got','categories','guy','damn','funny','biggest',
				'bad','globe','luck','win','stylists','comedy','party','batman','billybob','ge','common','etglobes','need']

#set the stopset based on the list of ignored words
def removeIgnored(phrase):
	words = phrase.lower().split(' ')
	stopset = set(stopwords.words('english'))
	for word in ignoredWords:
		stopset.add(word)
	for i in range(0,len(words)):
		stopset.add(words[i])
	return stopset

#searches the tweets and finds winners
def searchTweets(awards,nominees,inputFile):
	print "Searching for top tweets for award winners..."
	data = []
	with open('../' + inputFile) as f:
	    for line in f:
	        data.append(json.loads(line))

	#create the stopset of ignored words for each award
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

		#checks if the tweet matches an award. if so, add unigrams and bigrams to array 
		for i in range(0, len(awards)):
			award = remove_punctuation(awards[i].lower())
			awardTokenNotFound = False
			if award not in tweetText:
				awardTokenNotFound = True
			if awardTokenNotFound is False:
				tweetTokens = nltk.word_tokenize(tweetText)#create the unigrams
				words = re.findall('\w+', tweetText) #seperate the words
				bigrams = zip(words, words[1:]) #create the bigrams

				#add to array of unigrams if not an ignored word
				for tok in tweetTokens:
					if tok not in award_stopsets[i]:
						award_unigrams[i].append(tok)

				#add to array of bigams if not an ignored word
				for bi in bigrams:
					if bi[0] not in award_stopsets[i] and bi[1] not in award_stopsets[i]:
						award_bigrams[i].append(bi)	
		counter+=1
		if counter%10000==0:#prints progress
			print "Tweets scanned: " + str(counter)

	winners =[]
	for i in range(0,len(awards)):
		if i is 25:
			#find the cecile winner on own, since we dont have a predetermined list of nominees
			#we will just go by the highest count
			fdistBigram = nltk.FreqDist(award_bigrams[i])
			topBi = fdistBigram.most_common(10)
			biPart1 = (topBi[0][0])[0]
			biPart2 = (topBi[0][0])[1]
			winner = biPart1 + " " + biPart2
			winners.append(winner)
		else:
			#find the other awards
			fdistUnigram = FreqDist(award_unigrams[i])
			topUni = fdistUnigram.most_common(10)
			fdistBigram = nltk.FreqDist(award_bigrams[i])
			topBi = fdistBigram.most_common(10)
			results = findWinner(topUni,topBi, nominees[i])
			winner = results[0]
			nominees[i]=results[1]
			winners.append(winner)
	return winners,nominees

#matches a winner based on the list of nominees
def findWinner(topUnigrams, topBigrams, nominees):
	singleWordNom = False
	for nom in nominees: #search nominees to see if any are single words
		checkNom = nltk.word_tokenize(nom)
		if len(checkNom)==1:
			singleWordNom= True
			break

	if singleWordNom:#if any of the nominees are single words, use unigrams to match
		for i in range(0,len(topUnigrams)):
			for j in range (0,len(nominees)):
				uni = topUnigrams[i][0]
				nominee = nominees[j].lower()
				if nominee.find(uni)!=-1:
					winner = nominees[j]
					nominees.remove(winner)
					return winner,nominees
					break
	else:#if none of the nominees are single words, use bigrams to match
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
	
#similar to searchTweets, searches for fun goal terms			
def searchFunGoals(keywords,inputFile):
	print "Searching for top tweets for fun goals..."
	data = []
	with open('../' + inputFile) as f:
	    for line in f:
	        data.append(json.loads(line))
	keyword_stopsets = []
	for kw in keywords:
		stopset = removeIgnored(kw)
		keyword_stopsets.append(stopset)

	# this code block creates our corpus of relevant tweets - an array of tweet objects
	keyword_bigrams = [[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
					 [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]
	keyword_unigrams =[[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],
					 [],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[],[]]

	counter = 0
	for tweet in data[0]: 
		tweetText = tweet["text"].lower()	
		tweetText = remove_punctuation(tweetText)
		dataSet = False
		for i in range(0, len(keywords)):
			keyword = remove_punctuation(keywords[i].lower())
			keywordTokenNotFound = False
			if keyword not in tweetText:
				keywordTokenNotFound = True
			if keywordTokenNotFound is False:
				#tokenize the tweet text and filter by pos so we can get proper nouns later
				lTokens = nltk.word_tokenize(tweet['text'])
				lTokens = nltk.pos_tag(lTokens)
				words = re.findall('\w+', tweetText) #seperate the words
				bigrams = zip(words, words[1:])#create bigrams from unigrams
				for bi in bigrams:#add the bigrams
					if bi[0].lower() not in keyword_stopsets[i] and bi[1].lower() not in keyword_stopsets[i]:
						keyword_bigrams[i].append(bi)

				for token in lTokens:#only add the proper noun unigrams
					if token[1] == 'NNP':
						if token[0].lower() not in keyword_stopsets[i]:
							keyword_unigrams[i].append(token[0])
		counter+=1
		if counter%10000==0:#prints progress 
			print "Tweets scanned: " + str(counter)

	results =[]
	#this loop goes through each fun goal search term
	#checks if a proper noun unigram matches a bigram for that search term
	#if so, add to the results
	for i in range(0,len(keywords)):
		fdistUnigram = FreqDist(keyword_unigrams[i])
		topUni = fdistUnigram.most_common(10)
		fdistBigram = nltk.FreqDist(keyword_bigrams[i])
		topBi = fdistBigram.most_common(10)	
		matches = []
		for i in range(0, len(topUni)): 
			foundMatch = False
			j=0
			while j < len(topBi): 
				uni = topUni[i][0].lower()
				rating = topUni[i][1]
				biPart1 = (topBi[j][0])[0]
				biPart2 = (topBi[j][0])[1]
				if uni in biPart1 or uni in biPart2:
					#if this is not the first match, remove the bigram, 
					#since it is a duplicate or similar to a bigram that has already been added to matches
					if foundMatch == True:
						topBi.remove(topBi[j])
					else:#if this is the first bigram that has matched, add it
						if rating > 1:
							ans = biPart1 + " " + biPart2
							matches.append(ans)
							foundMatch = True 
				j+=1
		matches = remove_duplicates(matches)
		results.append(matches)
	return results





			

