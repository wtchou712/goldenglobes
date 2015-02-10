import json
import nltk
from pprint import pprint
json_data=open('/Users/Jeremy/Downloads/gg2013.json')

data = json.load(json_data)

tokenarray=[]
'''pprint(data)'''
counter=0
for tweet in data:
	tokens = nltk.word_tokenize(tweet['text'].lower())
	'''pprint(tokens)'''
	'''remove unwanted tokens'''
	'''add tokens to array'''
	tokenarray.append(tokens)

print "DONE"
json_data.close()
while counter < len(tokenarray):
	pprint(tokenarray[counter])
	counter= counter+1