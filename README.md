# goldenglobes
Golden Globes 2015

Welcome to Team 7's Golden Globe Searcher

Team Members: 
William Chou,
Matt Schley,
Jeremy Chase,
Andrew Jiang,

JSON files: 	
gg13answers.json,
gg15answers.json,
funGoals13.json,
funGoals15.json,

Packages and resources used:
NLTK (all packages),
Tkinter (for GUI)

How to run: 

Simple run 'main.py'
The program will begin searching for the award winners as well as fun goals
Once the program is finished searching a graphical user interface will appear allowing you to select which winners or
fun goals to view by year

***** NOTE *****

There is already 2 answer files from our search in the folder called "gg13answers.json" and "gg15answers.json". The 
program will always run the search at startup, but if you would like to skip the search and just see how the gui 
works, comment out line 6 in "main.py"

How our award search works: 

First, we take a tweet and see if it matches any of the awards that we are searching (i.e. "Best Director - Motion 
Picture"). If it does match an award, we normalize and tokenize the tweet to create bigrams and unigrams. We check if
each unigram/bigram is not in the list of ignored words (stopset) and if it is not, then we add it to the array of 
unigrams or bigrams for that specific award. For each tweet, we search all 25 awards at once. In this way, we are 
only going through the corpus once, rather than once for each award. Once the program is finished searching the 
entire corpus, we take each award's array of unigrams and bigrams and get the top 10 frequently occuring unigrams and
bigrams. Based on the list of nominees of that award, we determine whether to use the top 10 bigrams or the top 10 
unigrams. If any nominee in the list of nominees for that award is a single word (such as "Argo") then we will use 
unigrams, if not, we use the bigrams. From the top 10 unigrams/bigrams, we start from #1 and check if the bigram 
occurs in any of the nominees of that award. If it does, we stop the search and return that nominee as the winner. 
This is repeated for each award.

How our fun goal search works: 

This works similarly to the award search, but instead of normalized unigrams, we store the proper noun unigrams using
the 'NNP' tag. Then we get the top 10 bigrams and unigrams for each fun goal search term. For each proper noun 
unigram, we check to see if it matches any of the bigrams. If it does, we will store that bigram in the array of 
results for that fun goal search term. We continue searchin with the current unigram so we can remove any duplicate 
bigrams or similar bigrams in the top 10 bigrams. This is repeated for all fun goal search terms.

Approximate time for award search: 

2013 - 20s

2015 - 180s

Approximate time for fun goal search:

2013 - 60s

2015 - 380s
