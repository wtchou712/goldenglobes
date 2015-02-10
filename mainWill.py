from goldenglobeWill import findTopTweets
from goldenglobeWill import findWinner
from goldenglobeWill import remove_punctuation
from goldenglobeWill import findHost
import json

# directory = {'Ben Affleck': 'Argo', 'Kathryn Bigelow' : "Zero Dark Thirty", 'Ang Lee': 'Life of Pi', 'Steven Speilberg': 'Lincoln',
# 		  'Quentin Tarantino': 'Django Unchained', 'Jessica Chastain':'Zero Dark Thirty', 'Marion Cotillard': 'Rust and Bone',
# 		  'Helen Mirren':'Hitchcock', 'Naomi Watts': 'The Impossible', 'Rachel Weisz': 'The Deep Blue Sea', 'Daniel Day-Lewis': 'Lincoln',
# 		  'Richard Gere': 'Arbitage', 'John Hawkes': 'The Sessions', 'Joaquin Phoenix': 'The Master', 'Denzel Washington':'Flight',
# 		  'Jack Black': 'Bernie', 'Bradley Cooper': 'Silver Linings Playbook', 'Hugh Jackman': 'Les Miserables', 'Ewan McGregor': 'Salmong Fishing in the Yemen', 
# 		  'Bill Murray': 'Hyde Park on Hudson', 'Emily Blunt': 'Salmon Fishing in the Yemen', 'Judi Dench': 'The Best Exotic Marigold Hotel',
# 		  'Jennifer Lawrence':'Silver Linings Playbook', 'Maggie Smith':'Quartet', 'Meryl Streep': 'Hope Springs', 'Amy Adams': 'The Master',
# 		  'Sally Field':'Lincoln', 'Anne Hathaway':'Les Miserables', 'Helen Hunt':'The Sessions', 'Nicole Kidman':'The Paperboy', 'Alan Arkin':'Argo', 
# 		  'Leonardo DiCaprio':'Django Unchained', 'Philip Seymour Hoffman':'The Master', 'Tommy Lee Jones':'Lincoln','Christoph Waltz':'Django Unchained',
# 		  'Mark Boal':'Zero Dark Thirty', 'Tony Kushner':'Lincoln', "David O'Russell":'Silver Linings Playbook', 'Chris Terrio':'Argo',
# 		  'For You': 'music and lyrics by Monty Powell, Keith Urban in "Act of Valor"', 'Not Running Anymore': 'music and lyrics by Jon Bon Jobi in "Stand Up Guys"',
# 		  'Safe & Sound' : 'music and lyrics by Taylor Swift, John Paul White, Joy Williams, T Bone Burnett in "The Hunger Games"',
# 		  'Skyfall': 'music and lyrics by Adele and Paul Epworth in "Skyfall"', 'Suddenly':'music by Claude-Michel Stchonberg and lyrics by Herbert Kretzmer and Alain Boublil in "Les Miserables"',
# 		  'Mychael Danna': 'Life of Pi', 'Alexandre Desplat':'Argo', 'Dario Marianelli':'Anna Karenina', 'Tom Tykwer, Johnny Klimek and Reinhold Heil':'Cloud Atlas',
# 		  'John Williams':'Lincoln', 'Steve Buscemi':'Boardwalk Empire', 'Bryan Cranston':'Breaking Bad', 'Jeff Daniels':'The Newsroom',
# 		  'Jon Hamm':'Mad Men', 'Damian Lewis':'Homeland', 'Zooey Deschanel':'New Girl', 'Julia Louis-Dreyfus':'Veep', 'Lena Dunham':'Girls', 
# 		  'Tina Fey':'30 Rock', 'Amy Poehler':'Parks and Recreation', 'Alex Baldwin':'30 Rock', 'Don Cheadle':'House of Lies', 
# 		  'Louis C.K.':'Louie', 'Matt LeBlanc':'Episodes', 'Jim Parsons':'The Big Bang Theory', 'Nicole Kidman':'Hemingway & Gellhorn', 
# 		  'Jessica Lange':'American Horror Story:Asylum', 'Sienna Miller':'The Girl', 'Julianna Moores':'Game Change', 'Sigourney Weaver':'Political Animals', 
# 		  'Kevin Costner':'Hatfields & McCoys', 'Benedict Cumberbatch':'Sherlock(Masterpiece)', 'Woody Harrelson':'Game Change', 'Toby Jones':'The Girl', 
# 		  'Clive Owen':'Hemingway & Gellhorn', 'Hayden Panettiere':'Nashville', 'Archie Panjabi':'The Good Wife', 'Sarah Paulson':'Game Change',
# 		  'Maggie Smith':'Downtown Abbey:Season 2', 'Sofia Vergara':'Modern Family', 'Max Greenfield':'New Girl', 'Ed Harris':'Game Change', 'Danny Huston':'Magic City', 
# 		  'Eric Stonestreet':'Modern Family'}

# MPDrama = ["Lincoln", "Django Unchained", "Life of Pi", "Argo", "Zero Dark Thirty"]
# MPMusicComedy = ["The Best Exotic Marigold Hotel", "Les Miserables", "Moonrise Kingdom", "Salmon Fishing in the Yemen", "Silver Linings Playbook"]
# MPDirector = ["Ben Affleck", "Kathryn Bigelow", "Ang Lee", "Steven Steilberg", "Quentin Tarantino"]
# MPActressDrama = ["Jessica Chastain", "Marion Cotillard", 'Helen Mirren', 'Naomi Watts', 'Rachel Weisz']
# MPActorDrama = ['Daniel Day-Lewis', 'Richard Gere', 'John Hawkes', 'Joaquin Phoenix', 'Denzel Washington']
# MPActorMusicComedy = ['Jack Black', 'Bradley Cooper', 'Hugh Jackman', 'Ewan McGregor', 'Bill Murray']
# MPActressMusicComedy = ['Emily Blunt', 'Judi Dench', 'Jennifer Lawrence', 'Maggie Smith', 'Meryl Streep']
# MPSupportingActress = ['Amy Adams', 'Sally Field', 'Anne Hathaway', 'Helen Hunt', 'Nicole Kidman']
# MPSupportingActor = ['Alan Arkin', 'Leonardo DiCaprio', 'Philip Seymour Hoffman', 'Tommy Lee Jones', 'Christoph Waltz']
# MPScreenplay = ['Mark Boal', 'Tony Kushner', "David O'Russell", 'Quentin Tarantino', 'Chris Terrio']
# MPForeign = ['Amour','A Royal Affair', 'The Intouchables', 'Kon-Tiki', 'Rust and Bone']
# MPAnimated = ['Rise of the Guardians', 'Brave', 'Frankenweenie', 'Hotel Transylvania', 'Wreck-It Ralph']
# MPSong = ['For You', 'Not Running Anymore', 'Safe & Sound', 'Skyfall', 'Suddenly']
# MPScore = ['Mychael Danna', 'Alexandre Desplat', 'Dario Marianelli', 'Tom Tykwer, Johnny Klimek, Reinhold Heil', 'John Williams']

# TVMusicComedy = ['The Big Bang Theory', 'Episodes' , 'Girls', 'Modern Family', 'Smash']
# TVDrama = ['Breaking Bad', 'Boardwalk Empire', 'Downtown Abbey', 'Homeland', 'The Newsroom']
# TVActressDrama = ['Connie Britton', 'Glenn Close', 'Claire Danes', 'Michelle Dockery', 'Julianna Margulies']
# TVActorDrama = ['Steve Buscemi', 'Bryan Cranston', 'Jeff Daniels', 'Jon Hamm', 'Damian Lewis']
# TVActressComedy = ['Zooey Deschanel', 'Julia Louis-Dreyfous', 'Lena Dunham', 'Tina Fey', 'Amy Poehler']
# TVActorComedy = ['Alec Baldwin', 'Don Cheadle', 'Louis C.K.', 'Matt LeBlanc', 'Jim Parsons']
# TVMiniseries = ['Game Change', 'The Girl', 'Hatfields & McCoys', 'The Hour', 'Political Animals']
# TVActressMiniseries = ['Nicole Kidman', 'Jessica Lange', 'Sienna Miller', 'Julianne Moore', 'Sigourney Weaver']
# TVActorMiniSeries = ['Kevin Costner', 'Benedict Cumberbatch', 'Woody Harrelson', 'Toby Jones', 'Clive Owen']
# TVSupportingActress = ['Hayden Panettiere', 'Archie Panjabi', 'Sarah Paulson' , 'Maggie Smith', 'Sofia Vergara']
# TVSupportingActor = ['Max Greenfield', 'Ed Harris', 'Danny Huston', 'Mandy Patinkin', 'Eric Stonestreet']

# allNominees = [MPDrama, MPMusicComedy, MPDirector, MPActressDrama, MPActorDrama, MPActorMusicComedy, MPActressMusicComedy, MPSupportingActress, MPSupportingActor, MPScreenplay, MPForeign,
# 			   MPAnimated, MPSong, MPScore, TVMusicComedy, TVDrama, TVActressDrama, TVActorDrama, TVActressComedy, TVActorComedy, TVMiniseries, TVActressMiniseries,
# 			   TVActorMiniSeries,TVSupportingActress, TVSupportingActor]
# awardsList = ['Best Motion Picture - Drama', 'Best Motion Picture - Musical or Comedy', 'Best Director - Motion Picture', 'Best Actress in a Motion Picture - Drama',
# 			  'Best Actor in a Motion Picture - Drama', 'Best Actor in a Motion Picture - Musical or Comedy', 'Best Actress in a Motion Picture - Musical or Comedy',
# 			  'Best Supporting Actress - Motion Picture', 'Best Supporting Actor - Motion Picture', 'Best Screenplay - Motion Picture', 'Foreign Film - Motion Picture', 
# 			  'Best Animated Film - Motion Picture', 'Best Original Song - Motion Picture', 'Best Original Score - Motion Picture', 'Best TV Comedy or Musical', 'Best TV Drama',
# 			  'Best Actress in a TV Drama', 'Best Actor in a TV Drama', 'Best Actress in a TV Comedy or Musical', 'Best Actor in a TV Comedy', 'Best Miniseries or TV Movie',
# 			  'Best Actress in a Miniseries or TV Movie', 'Best Actor in a Miniseries or TV Movie', 'Best Supporting Actress in a TV Show, Miniseries or TV Movie', 
# 			  'Best Supporting Actor in a TV Show, Miniseries or TV Movie']

directory = {'Richard Linklater': 'Boyhood', 'Wes Anderson' : 'The Grand Budapest Hotel', 'Ava DuVernay' : 'Selma', 'David Fincher' : 'Gone Girl',
'Alejandro Gonzalez Inarritu' : 'Birdman','Eddie Redmayne' : 'The Theory of Everything', 'Steve Carell' : 'Foxcatcher', 'Benedict Cumberbatch' : 'The Imitation Game', 
'Jake Gyllenhaal' : 'Nightcrawler', 'David Oyelowo' : 'Selma','Julianne Moore' : 'Still Alice', 'Jennifer Aniston' : 'Cake',' Felicity Jones' : 'The Theory of Everything', 
'Rosamund Pike' : 'Gone Girl', 'Reese Witherspoon': 'Wild','Michael Keaton' : 'Birdman', 'Ralph Fiennes' : 'The Grand Budapest Hotel', 'Bill Murray' : 'St. Vincent', 
'Joaquin Phoenix' : 'Inherent Vice', 'Christoph Waltz' : 'Big Eyes','Amy Adams' : 'Big Eyes', 'Emily Blunt' : 'Into the Woods', 'Helen Mirren' : 'The Hundred-Foot Journey', 
'Julianne Moore' : 'Maps to the Stars', 'Quvenzhane Wallis' : 'Annie', 'Patricia Arquette' : 'Boyhood', 'Jessica Chastain' : 'A Most Violent Year', 
'Keira Knightley' : 'The Imitation Game', 'Emma Stone' : 'Birdman', 'Meryl Streep' : 'Into the Woods','J.K. Simmons' : 'Whiplash', 'Robert Duvall' : 'The Judge', 
'Ethan Hawke' : 'Boyhood', 'Edward Norton' : 'Birdman', 'Mark Ruffalo': 'Foxcatcher' ,'Alejandro Gonzalez Inarritu, Nicolas Giacobone, Armando Bo, Alexander Dinelaris, Jr.': 'Birdman',
'Wes Anderson' : 'The Grand Budapest Hotel', 'Gillian Flynn' : 'Gone Girl', 'Richard Linklater': 'Boyhood', 'Graham Moore':'The Imitation Game',
'Johann Johannsson': 'The Theory of Everything', 'Alexandre Desplat': 'The Imitation Game', 'Trent Reznore, Atticus Ross': 'Gone Girl', 'Antonio Sanchez' : 'Birdman', 
'Hans Zimmer' : 'Interstellar', 'Glory': 'Selma', 'Big Eyes': 'Big Eyes', 'Mercy Is': 'Noah', 'Opportunity' : 'Annie', 'Yellow Flicker Beat': 'The Hunger Games: Mockingjay - Part 1',
'Ruth Wilson': 'The Affair', 'Claire Danes':'Homeland', 'Viola Davis': 'How to Get Away With Murder', 'Julianna Margulies': 'The Good Wife', 'Robin Wright': 'House of Cards',
'Kevin Spacey': 'House of Cards', 'Clive Owen' : 'Liev Schreiber' , 'Liev Schreiber': 'Ray Donovan', 'James Spader': 'The Blacklist', 'Dominic West': 'The Affair',
'Gina Rodriguez': 'Jane the Virgin', 'Lena Dunham': 'Girls', 'Edie Falco' : 'Nurse Jackie', 'Julia Louis-Dreyfus' : 'Veep', 'Taylor Schilling': 'Orange is the New Black',
'Jeffrey Tambor': 'Transparent', 'Louis C. K.': 'Louie', 'Don Cheadle': 'House of Lies', 'Ricky Gervais': 'Derek', 'William H. Macy': 'Shameless','Maggie Gyllenhaal' : 'The Honourable Woman',
'Jessica Lange': 'American Horror Story: Freak Show', 'Frances McDormand' : 'Olive Kitteridge', "Frances O'Connor" : 'The Missing', 'Allison Tolman': 'Fargo', 
'Billy Bob Thornton':'Fargo', 'Martin Freeman' : 'Fargo', 'Wood Harrelson' : 'True Detective', 'Matthew McConaughey' : 'True Detective', 'Mark Ruffalo': 'The Normal Heart',
'Joanna Froggatt': 'Downton Abbey', 'Uzo Aduba': 'Orange Is the New Black', 'Kathy Bates': 'American Horror Story: Freak Show', 'Allison Janney': 'Mom', 
'Michelle Monaghan': 'True Detective','Matt Bomer': 'The Normal Heart', 'Alan Cumming': 'The Good Wife', 'Colin Hanks' : 'Fargo', 'Bill Murray' : 'Olive Kitteridge', 'Jon Voight': 'Ray Donovan'}

MPDrama = ['Boyhood', 'Foxcatcher', 'The Imitation Game', 'Selma', 'The Theory of Everything']
MPMusicComedy = ['The Grand Budapest Hotel','Birdman','Into the Woods', 'Pride','St. Vincent']
MPDirector = ['Richard Linklater', 'Wes Anderson', 'Ava DuVernay', 'David Fincher', 'Alejandro Gonzalez Inarritu']
MPActressDrama = ['Julianne Moore', 'Jennifer Aniston',' Felicity Jones', 'Rosamund Pike', 'Reese Witherspoon']
MPActorDrama = ['Eddie Redmayne', 'Steve Carell', 'Benedict Cumberbatch', 'Jake Gyllenhaal', 'David Oyelowo']
MPActorMusicComedy = ['Michael Keaton', 'Ralph Fiennes', 'Bill Murray', 'Joaquin Phoenix', 'Christoph Waltz']
MPActressMusicComedy = ['Amy Adams', 'Emily Blunt', 'Helen Mirren', 'Julianne Moore', 'Quvenzhane Wallis']
MPSupportingActress = ['Patricia Arquette', 'Jessica Chastain', 'Keira Knightley', 'Emma Stone', 'Meryl Streep']
MPSupportingActor = ['J.K. Simmons', 'Robert Duvall', 'Ethan Hawke', 'Edward Norton', 'Mark Ruffalo']
MPScreenplay = ['Alejandro Gonzalez Inarritu, Nicolas Giacobone, Armando Bo, Alexander Dinelaris, Jr.', 'Wes Anderson', 'Gillian Flynn', 'Richard Linklater', 'Graham Moore']
MPForeign = ['Leviathan', 'Force Majeure', 'Gett: The Trial of Viviane Amsalem', 'Ida', 'Tangerines']
MPAnimated = ['How to Train Your Dragon 2', 'Big Hero 6', 'The Book of Life', 'The Boxtrolls', 'The Lego Movie']
MPSong = ['Glory', 'Big Eyes', 'Mercy Is', 'Opportunity', 'Yellow Flicker Beat']
MPScore = ['Johann Johannsson', 'Alexandre Desplat', 'Trent Reznore, Atticus Ross', 'Antonio Sanchez', 'Hans Zimmer']

TVMusicComedy = ['Transparent', 'Girls', 'Jane the Virgin', 'Orange Is the New Black', 'Silicon Valley']
TVDrama = ['The Affair', 'Game of Thrones', 'Downton Abbey', 'The Good Wife', 'House of Cards']
TVActressDrama = ['Ruth Wilson', 'Claire Danes', 'Viola Davis', 'Julianna Margulies', 'Robin Wright']
TVActorDrama = ['Kevin Spacey', 'Clive Owen', 'Liev Schreiber', 'James Spader', 'Dominic West']
TVActressComedy = ['Gina Rodriguez', 'Lena Dunham', 'Edie Falco', 'Julia Louis-Dreyfus', 'Taylor Schilling']
TVActorComedy = ['Jeffrey Tambor', 'Louis C. K.', 'Don Cheadle', 'Ricky Gervais', 'William H. Macy']
TVMiniseries = ['Fargo', 'The Missing', 'The Normal Heart', 'Olive Kitteridge', 'True Detective']
TVActressMiniseries = ['Maggie Gyllenhaal', 'Jessica Lange', 'Frances McDormand', "Frances O'Connor", 'Allison Tolman']
TVActorMiniSeries = ['Billy Bob Thornton', 'Martin Freeman', 'Wood Harrelson', 'Matthew McConaughey', 'Mark Ruffalo']
TVSupportingActress = ['Joanna Froggatt', 'Uzo Aduba', 'Kathy Bates', 'Allison Janney', 'Michelle Monaghan']
TVSupportingActor = ['Matt Bomer', 'Alan Cumming', 'Colin Hanks', 'Bill Murray', 'Jon Voight']

allNominees = [MPDrama, MPMusicComedy, MPDirector, MPActressDrama, MPActorDrama, MPActorMusicComedy, MPActressMusicComedy, MPSupportingActress, MPSupportingActor, MPScreenplay, MPForeign,
			   MPAnimated, MPSong, MPScore, TVMusicComedy, TVDrama, TVActressDrama, TVActorDrama, TVActressComedy, TVActorComedy, TVMiniseries, TVActressMiniseries,
			   TVActorMiniSeries,TVSupportingActress, TVSupportingActor]
presenters = [['Meryl Streep'], ['Robert Downey, Jr.'], ['Harrison Ford'], ['Matthew McConaughey'], ['Gwyneth Paltrow'], ['Amy Adams'],['Ricky Gervais'], ['Jared Leto'], 
			  ['Jennifer Aniston', 'Benedict Cumberbatch'], ['Bill Hader', 'Kristen Wiig'], ["Colin Farrell", "Lupita Nyong'o"], ['Kevin Hart', 'Salma Hayek'], ['Prince'], 
			  ['Sienna Miller', 'Vince Vaughn'], ['Bryan Cranston', 'Kerry Washington'], ['Adam Levine','Paul Rudd'], ['Anna Faris','Chris Pratt'], ['David Duchovny', 'Katherine Heigl'], 
			  ['Bryan Cranston','Kerry Washington'], ['Jane Fonda','Lily Tomlin'],['Jennifer Lopez','Jeremy Renner'],['Kate Beckinsale','Adrien Brody'],['Jennifer Lopez','Jeremy Renner'], 
			  ['Jamie Dornan','Dakota Johnson'],['Katie Holmes','Seth Meyers']]
awardsList = ['Best Motion Picture - Drama', 'Best Motion Picture - Musical or Comedy', 'Best Director - Motion Picture', 'Best Actress in a Motion Picture - Drama',
			  'Best Actor in a Motion Picture - Drama', 'Best Actor in a Motion Picture - Comedy or Musical', 'Best Actress in a Motion Picture - Comedy or Musical',
			  'Best Supporting Actress - Motion Picture', 'Best Supporting Actor - Motion Picture', 'Best Screenplay - Motion Picture', 'Best Foreign Language Film', 
			  'Best Animated Feature Film', 'Best Original Song - Motion Picture', 'Best Original Score - Motion Picture', 'Best TV Comedy or Musical', 'Best TV Drama',
			  'Best Actress in a TV Drama', 'Best Actor in a TV Drama', 'Best Actress in a TV Comedy or Musical', 'Best Actor in a TV Comedy or Musical', 'Best Miniseries or TV Movie',
			  'Best Actress in a Miniseries or TV Movie', 'Best Actor in a Miniseries or TV Movie', 'Best Supporting Actress in a TV Show, Miniseries or TV Movie', 
			  'Best Supporting Actor in a TV Show, Miniseries or TV Movie']
searchList = ['Best Motion Picture - Drama', 'Best Motion Picture - Musical or Comedy', 'Best Director - Motion Picture', 'Best Actress in a Motion Picture - Drama',
			  'Best Actor in a Motion Picture - Drama', 'Best Actor in a Motion Picture - Comedy or Musical', 'Best Actress in a Motion Picture - Comedy or Musical',
			  'Best Supporting Actress - Motion Picture', 'Best Supporting Actor - Motion Picture', 'Best Screenplay - Motion Picture', 'Foreign Film', 
			  'Animated Film', 'Best Original Song', 'Best Original Score', 'Best TV Comedy or Musical', 'Best TV Drama',
			  'Best Actress in a TV Drama', 'Best Actor in a TV Drama', 'Best Actress in a TV Comedy or Musical', 'Best Actor in a TV Comedy or Musical', 'Best Miniseries or TV Movie',
			  'Best Actress in a Miniseries or TV Movie', 'Best Actor in a Miniseries or TV Movie', 'Best Supporting Actress in a TV Show, Miniseries or TV Movie', 
			  'Best Supporting Actor in a TV Show, Miniseries or TV Movie']

winners= findTopTweets(searchList, allNominees)
#winners = findTopTweets(['Best Original Score'], [MPScore])
for i in range(0,len(winners)):
	print awardsList[i] + " goes to " + winners[i]

nomineeList = []
for nominees in allNominees:
	nomineeList = nominees + nomineeList


results = {}
metadata = {}
hosts = {}
nominees = {}
awards = {}
data = {}
structured = {}
unstructured = {}

metadata['year'] = 2013
hosts['method'] = "hardcoded"
hosts['method_description'] = ''
nominees['method'] = "hardcoded"
nominees['method_description'] = ''
awards['method'] = "hardcoded"
awards['method_description'] = ''
unstructured['hosts'] = ['Tina Fey', 'Amy Poehler']
unstructured['winners'] = winners
unstructured['awards'] = awardsList
unstructured['presenters'] = []
unstructured['nominees'] = nomineeList

for i in range(0, len(awardsList)):
	award = {}
	award['nominees'] = allNominees[i]
	award['winner'] = winners[i]
	award['presenters'] = presenters[i]
	structured['award' + str(i+1)] = award
data['unstructured']= unstructured
data['structured'] = structured
results['metadata'] = metadata
results['data'] = data
with open('data.json', 'w') as outfile:
    json.dump(data, outfile)

# def searchAward(awardChoice):
# 	# print "you entered", awardChoice
# 	print "Searching for " + awardsList[awardChoice-1]

# 	if awardChoice is 12: #animated film
# 		results=findTopTweets(remove_punctuation(("Animated Film").lower()))
# 		winner = findWinner(results[0], results[1], allNominees[awardChoice-1])
# 	elif awardChoice is 11: #foreign film
# 		results=findTopTweets(remove_punctuation(('Foreign Film').lower()))
# 		winner = findWinner(results[0], results[1], allNominees[awardChoice-1])
# 	elif awardChoice is 20:
# 		resultsA=findTopTweets(remove_punctuation(('Best Actor in a TV Comedy').lower()))
# 		winnerA = findWinner(resultsA[0], resultsA[1], allNominees[awardChoice-1])
# 		resultsB=findTopTweets(remove_punctuation(('Best Actor in a TV Musical').lower()))
# 		winnerB = findWinner(resultsB[0], resultsB[1], allNominees[awardChoice-1])
# 		if winnerA is None:
# 			winner = winnerB
# 		else: 
# 			winner = winnerA
# 	else:
# 		results=findTopTweets(remove_punctuation((awardsList[awardChoice-1]).lower()))
# 		winner = findWinner(results[0], results[1], allNominees[awardChoice-1])
	
# 	#presenter = findPresenter(winner)	

# 	#print allNominees[awardChoice-1]
# 	print "========================================================"
# 	if winner in directory:
# 		print "The award for " + awardsList[awardChoice-1] + " goes to " + winner + " in " + directory[winner]
# 	else: 
# 		print "The award for " + awardsList[awardChoice-1] + " goes to " + str(winner)




# for i in range(0, len(awardsList)):
# 	print str(i+1) + ": " + awardsList[i]
# print str(26) + ": " + 'All Awards' 

# awardChoice = int(raw_input("Choose the number of award you want to see: ")) 

# if awardChoice is not 26:
# 	searchAward(awardChoice)
# else:
# 	print "Searching all..."
# 	for index in range(1,26):
# 		searchAward(index)



	



