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
	stopset.add('wins')
	stopset.add('wtf')
	stopset.add('oscar')
	stopset.add('congratulations')
	stopset.add('director')
	stopset.add('category')
	stopset.add('right')
	stopset.add('@')
	stopset.add('nbc')
	stopset.add('gives')
	stopset.add('academy')
	stopset.add('award')
	stopset.add('amp')
	stopset.add('eonline')
	stopset.add('list')
	stopset.add('photos')
	stopset.add('face')
	stopset.add('normal')
	stopset.add('wow')
	stopset.add('see')
	stopset.add('fashion')
	stopset.add('red')
	stopset.add('carpet')
	stopset.add('tonight')
	stopset.add('styles')
	stopset.add('stylist')
	stopset.add('yay')
	stopset.add('got')
	stopset.add('categories')
	stopset.add('biggest')
	stopset.add('guy')
	stopset.add('damn')
	stopset.add('funny')
	stopset.add('biggest')
	stopset.add('bad')
	#stopset.add('')
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
			#if i <= 25:
			awardTokenNotFound = False
			# award = remove_punctuation(awards[i].lower())

			if award not in tweetText:
				awardTokenNotFound = True
			if awardTokenNotFound is False:
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
			# else:
			# 	awardTokenNotFound = False
			# 	if award not in tweetText:
			# 		awardTokenNotFound = True
			# 	if awardTokenNotFound is False:
			# 		lTokens = nltk.word_tokenize(tweet['text'])
			# 		lTokens = nltk.pos_tag(lTokens)

			# 		# lTagDict = findtags('NNP', lTokens)
			# 		# if lTagDict.has_key("NNP"):
			# 		# 	words = lTagDict["NNP"]
			# 		# 	bigrams = zip(words,words[1:])
			# 		words = re.findall('\w+', tweetText) #seperate the words
			# 		bigrams = zip(words, words[1:])
			# 		for bi in bigrams:
			# 			if bi[0].lower() not in award_stopsets[i] and bi[1].lower() not in award_stopsets[i]:
			# 				award_bigrams[i].append(bi)

			# 		# for tag in sorted(lTagDict):
			# 		#     print tag, lTagDict[tag]

			# 		for token in lTokens:
			# 			if token[1] == 'NNP':
			# 				if token[0].lower() not in award_stopsets[i]:
			# 					award_unigrams[i].append(token[0])
					
		counter+=1
		if counter%1000==0:
			print "Tweets scanned: " + str(counter)


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
		# elif i >= 26: 
		# 	# #find the winners for the fun goals
		# 	# fdistBigram = nltk.FreqDist(award_bigrams[i])
		# 	# topBi = fdistBigram.most_common(10)
		# 	# print "top bigrams for " + awards[i]
		# 	# print topBi
		# 	# biPart1 = (topBi[0][0])[0]
		# 	# biPart2 = (topBi[0][0])[1]
		# 	# winner = biPart1 + " " + biPart2
		# 	fdistUnigram = FreqDist(award_unigrams[i])
		# 	topUni = fdistUnigram.most_common(10)
		# 	fdistBigram = nltk.FreqDist(award_bigrams[i])
		# 	topBi = fdistBigram.most_common(10)
		# 	print '================================================'
		# 	print "top unigrams for " + awards[i]
		# 	print topUni
		# 	print '================================================'
		# 	print "top bigrams for " + awards[i]
		# 	print topBi
		# 	#winners.append(winner)
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
				
def searchFunGoals(keywords,inputFile):
	start_time = time.time()
	print "Searching for top tweets..."
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
				lTokens = nltk.word_tokenize(tweet['text'])
				lTokens = nltk.pos_tag(lTokens)

				# lTagDict = findtags('NNP', lTokens)
				# if lTagDict.has_key("NNP"):
				# 	words = lTagDict["NNP"]
				# 	bigrams = zip(words,words[1:])
				words = re.findall('\w+', tweetText) #seperate the words
				bigrams = zip(words, words[1:])
				for bi in bigrams:
					if bi[0].lower() not in keyword_stopsets[i] and bi[1].lower() not in keyword_stopsets[i]:
						keyword_bigrams[i].append(bi)

				# for tag in sorted(lTagDict):
				#     print tag, lTagDict[tag]

				for token in lTokens:
					if token[1] == 'NNP':
						if token[0].lower() not in keyword_stopsets[i]:
							keyword_unigrams[i].append(token[0])
					
		counter+=1
		if counter%1000==0:
			print "Tweets scanned: " + str(counter)

	results =[]
	for i in range(0,len(keywords)):
		fdistUnigram = FreqDist(keyword_unigrams[i])
		topUni = fdistUnigram.most_common(10)
		fdistBigram = nltk.FreqDist(keyword_bigrams[i])
		topBi = fdistBigram.most_common(10)
		print '================================================'
		print "top unigrams for " + keywords[i]
		print topUni
		print '================================================'
		print "top bigrams for " + keywords[i]
		print topBi
		
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
					if foundMatch == True:
						topBi.remove(topBi[j])
					else:
						if rating > 1:
							ans = biPart1 + " " + biPart2
							matches.append(ans)
							foundMatch = True 
				j+=1
		matches = remove_duplicates(matches)
		results.append(matches)


	elapsed_time = time.time() - start_time
	print "Search length: " + str(elapsed_time)
	#print winners
	return results





			

