from searchtweets import searchTweets
from searchtweets import findWinner
from searchtweets import remove_punctuation
from searchtweets import searchFunGoals
import json
import time
from collections import OrderedDict

directory13 = {'Ben Affleck': 'Argo', 'Kathryn Bigelow' : "Zero Dark Thirty", 'Ang Lee': 'Life of Pi', 'Steven Speilberg': 'Lincoln',
		  'Quentin Tarantino': 'Django Unchained', 'Jessica Chastain':'Zero Dark Thirty', 'Marion Cotillard': 'Rust and Bone',
		  'Helen Mirren':'Hitchcock', 'Naomi Watts': 'The Impossible', 'Rachel Weisz': 'The Deep Blue Sea', 'Daniel Day-Lewis': 'Lincoln',
		  'Richard Gere': 'Arbitage', 'John Hawkes': 'The Sessions', 'Joaquin Phoenix': 'The Master', 'Denzel Washington':'Flight',
		  'Jack Black': 'Bernie', 'Bradley Cooper': 'Silver Linings Playbook', 'Hugh Jackman': 'Les Miserables', 'Ewan McGregor': 'Salmong Fishing in the Yemen', 
		  'Bill Murray': 'Hyde Park on Hudson', 'Emily Blunt': 'Salmon Fishing in the Yemen', 'Judi Dench': 'The Best Exotic Marigold Hotel',
		  'Jennifer Lawrence':'Silver Linings Playbook', 'Maggie Smith':'Quartet', 'Meryl Streep': 'Hope Springs', 'Amy Adams': 'The Master',
		  'Sally Field':'Lincoln', 'Anne Hathaway':'Les Miserables', 'Helen Hunt':'The Sessions', 'Nicole Kidman':'The Paperboy', 'Alan Arkin':'Argo', 
		  'Leonardo DiCaprio':'Django Unchained', 'Philip Seymour Hoffman':'The Master', 'Tommy Lee Jones':'Lincoln','Christoph Waltz':'Django Unchained',
		  'Mark Boal':'Zero Dark Thirty', 'Tony Kushner':'Lincoln', "David O'Russell":'Silver Linings Playbook', 'Chris Terrio':'Argo',
		  'For You': 'music and lyrics by Monty Powell, Keith Urban in "Act of Valor"', 'Not Running Anymore': 'music and lyrics by Jon Bon Jobi in "Stand Up Guys"',
		  'Safe & Sound' : 'music and lyrics by Taylor Swift, John Paul White, Joy Williams, T Bone Burnett in "The Hunger Games"',
		  'Skyfall': 'music and lyrics by Adele and Paul Epworth in "Skyfall"', 'Suddenly':'music by Claude-Michel Stchonberg and lyrics by Herbert Kretzmer and Alain Boublil in "Les Miserables"',
		  'Mychael Danna': 'Life of Pi', 'Alexandre Desplat':'Argo', 'Dario Marianelli':'Anna Karenina', 'Tom Tykwer, Johnny Klimek and Reinhold Heil':'Cloud Atlas',
		  'John Williams':'Lincoln', 'Steve Buscemi':'Boardwalk Empire', 'Bryan Cranston':'Breaking Bad', 'Jeff Daniels':'The Newsroom',
		  'Jon Hamm':'Mad Men', 'Damian Lewis':'Homeland', 'Zooey Deschanel':'New Girl', 'Julia Louis-Dreyfus':'Veep', 'Lena Dunham':'Girls', 
		  'Tina Fey':'30 Rock', 'Amy Poehler':'Parks and Recreation', 'Alex Baldwin':'30 Rock', 'Don Cheadle':'House of Lies', 
		  'Louis C.K.':'Louie', 'Matt LeBlanc':'Episodes', 'Jim Parsons':'The Big Bang Theory', 'Nicole Kidman':'Hemingway & Gellhorn', 
		  'Jessica Lange':'American Horror Story:Asylum', 'Sienna Miller':'The Girl', 'Julianna Moores':'Game Change', 'Sigourney Weaver':'Political Animals', 
		  'Kevin Costner':'Hatfields & McCoys', 'Benedict Cumberbatch':'Sherlock(Masterpiece)', 'Woody Harrelson':'Game Change', 'Toby Jones':'The Girl', 
		  'Clive Owen':'Hemingway & Gellhorn', 'Hayden Panettiere':'Nashville', 'Archie Panjabi':'The Good Wife', 'Sarah Paulson':'Game Change',
		  'Maggie Smith':'Downtown Abbey:Season 2', 'Sofia Vergara':'Modern Family', 'Max Greenfield':'New Girl', 'Ed Harris':'Game Change', 'Danny Huston':'Magic City', 
		  'Eric Stonestreet':'Modern Family'}

MPDrama13 = ["Lincoln", "Django Unchained", "Life of Pi", "Argo", "Zero Dark Thirty"]
MPMusicComedy13 = ["The Best Exotic Marigold Hotel", "Les Miserables", "Moonrise Kingdom", "Salmon Fishing in the Yemen", "Silver Linings Playbook"]
MPDirector13 = ["Ben Affleck", "Kathryn Bigelow", "Ang Lee", "Steven Steilberg", "Quentin Tarantino"]
MPActressDrama13 = ["Jessica Chastain", "Marion Cotillard",'Sally Field', 'Helen Mirren', 'Naomi Watts', 'Rachel Weisz']
MPActorDrama13 = ['Daniel Day-Lewis', 'Richard Gere', 'John Hawkes', 'Joaquin Phoenix', 'Denzel Washington']
MPActorMusicComedy13 = ['Jack Black', 'Bradley Cooper', 'Hugh Jackman', 'Ewan McGregor', 'Bill Murray']
MPActressMusicComedy13 = ['Emily Blunt', 'Judi Dench', 'Jennifer Lawrence', 'Maggie Smith', 'Meryl Streep']
MPSupportingActress13 = ['Amy Adams', 'Sally Field', 'Anne Hathaway', 'Helen Hunt', 'Nicole Kidman']
MPSupportingActor13 = ['Alan Arkin', 'Leonardo DiCaprio', 'Philip Seymour Hoffman', 'Tommy Lee Jones', 'Christoph Waltz']
MPScreenplay13 = ['Django Unchained','Zero Dark Thirty','Lincoln','Silver Linings Playbook','Argo']
MPForeign13 = ['Amour','A Royal Affair', 'The Intouchables', 'Kon Tiki', 'Rust and Bone']
MPAnimated13 = ['Rise of the Guardians', 'Brave', 'Frankenweenie', 'Hotel Transylvania', 'Wreck-It Ralph']
MPSong13 = ['Act of Valor', 'Stand Up Guys', 'The Hunger Games', 'Skyfall', 'Les Miserables']
MPScore13 = ['Life of Pi','Argo','Anna Karenina', 'Cloud Atlas','Lincoln']


TVMusicComedy13 = ['The Big Bang Theory', 'Episodes' , 'Girls', 'Modern Family', 'Smash']
TVDrama13 = ['Breaking Bad', 'Boardwalk Empire', 'Downtown Abbey (masterpiece)', 'Homeland', 'The Newsroom']
TVActressDrama13 = ['Connie Britton', 'Glenn Close', 'Claire Danes', 'Michelle Dockery', 'Julianna Margulies']
TVActorDrama13 = ['Steve Buscemi', 'Bryan Cranston', 'Jeff Daniels', 'Jon Hamm', 'Damian Lewis']
TVActressComedy13 = ['Zooey Deschanel', 'Julia Louis-Dreyfous', 'Lena Dunham', 'Tina Fey', 'Amy Poehler']
TVActorComedy13 = ['Alec Baldwin', 'Don Cheadle', 'Louis C.K.', 'Matt LeBlanc', 'Jim Parsons']
TVMiniseries13 = ['Game Change', 'The Girl', 'Hatfields & McCoys', 'The Hour', 'Political Animals']
TVActressMiniseries13 = ['Nicole Kidman', 'Jessica Lange', 'Sienna Miller', 'Julianne Moore', 'Sigourney Weaver']
TVActorMiniSeries13 = ['Kevin Costner', 'Benedict Cumberbatch', 'Woody Harrelson', 'Toby Jones', 'Clive Owen']
TVSupportingActress13 = ['Hayden Panettiere', 'Archie Panjabi', 'Sarah Paulson' , 'Maggie Smith', 'Sofia Vergara']
TVSupportingActor13 = ['Max Greenfield', 'Ed Harris', 'Danny Huston', 'Mandy Patinkin', 'Eric Stonestreet']

allNominees13 = [MPDrama13, MPMusicComedy13, MPDirector13, MPActressDrama13, MPActorDrama13, MPActorMusicComedy13, MPActressMusicComedy13, MPSupportingActress13, MPSupportingActor13, MPScreenplay13, MPForeign13,
			   MPAnimated13, MPSong13, MPScore13, TVMusicComedy13, TVDrama13, TVActressDrama13, TVActorDrama13, TVActressComedy13, TVActorComedy13, TVMiniseries13, TVActressMiniseries13,
			   TVActorMiniSeries13, TVSupportingActress13, TVSupportingActor13]
presenters13 = [['Julia Roberts'],
				['Dustin Hoffman'],
				['Halle Berry'],
				['George Clooney'],
				['George Clooney'],
				['Jennifer Garner'],
				['Will Ferell','Kristen Wiig'],
				['Megan Fox','Jonah Hill'],
			    ['Bradley Cooper','Kate Hudson'],
			    ['Robert Pattinson', 'Amanda Seyfried'],
			    ['Arnold Schwarzenegger','Sylvester Stallone'],
			    ['Sacha Baron Cohen'],
			    ['Jennifer Lopez','Jason Statham'],
			    ['Jennifer Lopez','Jason Statham'],
			    ['Jimmy Fallon','Jay Leno'],
			    ['Salma Hayek','Paul Rudd'],
			    ['Nathan Fillion','Lea Michelle'],
			    ['Salma Hayek', 'Paul Rudd'],
			    ['Aziz Ansari', 'Jason Bateman'],
			    ['Lucy Liu', 'Debra Messing'],
			    ['Don Cheadle','Eva Longoria'],
			    ['Don Cheadle','Eva Longoria'],
			    ['Jessica Alba', 'Kiefer Sutherland'],
			    ['Dennis Quaid', 'Kerry Washington'],
			    ['Kristen Bell', 'John Krasinski'],
			    ['Robert Downey, Jr.']]
awardsList13 = ['Best Motion Picture - Drama', 
				'Best Motion Picture - Comedy or Musical', 
				'Best Director - Motion Picture', 
				'Best Performance by an Actress in a Motion Picture - Drama',
			  	'Best Performance by an Actor in a Motion Picture - Drama', 
			  	'Best Performance by an Actor in a Motion Picture - Comedy Or Musical', 
			  	'Best Performance by an Actress in a Motion Picture - Comedy Or Musical',
			  	'Best Performance by an Actress In A Supporting Role in a Motion Picture', 
			  	'Best Performance by an Actor In A Supporting Role in a Motion Picture', 
			  	'Best Screenplay - Motion Picture', 
			  	'Best Foreign Language Film', 
			  	'Best Animated Feature Film', 
			  	'Best Original Song - Motion Picture', 
			  	'Best Original Score - Motion Picture', 
			  	'Best Television Series - Comedy Or Musical', 
			  	'Best Television Series - Drama',
			  	'Best Performance by an Actress In A Television Series - Drama', 
			  	'Best Performance by an Actor In A Television Series - Drama', 
			  	'Best Performance by an Actress In A Television Series - Comedy Or Musical', 
			  	'Best Performance by an Actor In A Television Series - Comedy Or Musical',
			  	'Best Mini-Series Or Motion Picture Made for Television',
			  	'Best Performance by an Actress In A Mini-series or Motion Picture Made for Television', 
			  	'Best Performance by an Actor In A Mini-series or Motion Picture Made for Television', 
			  	'Best Performance by an Actress in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television', 
			  	'Best Performance by an Actor in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television',
			  	'Cecil B. DeMille Award']

directory15 = {'Richard Linklater': 'Boyhood', 'Wes Anderson' : 'The Grand Budapest Hotel', 'Ava DuVernay' : 'Selma', 'David Fincher' : 'Gone Girl',
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

MPDrama15 = ['Boyhood', 'Foxcatcher', 'The Imitation Game', 'Selma', 'The Theory of Everything']
MPMusicComedy15 = ['The Grand Budapest Hotel','Birdman','Into the Woods', 'Pride','St. Vincent']
MPDirector15 = ['Richard Linklater', 'Wes Anderson', 'Ava DuVernay', 'David Fincher', 'Alejandro Gonzalez Inarritu']
MPActressDrama15 = ['Julianne Moore', 'Jennifer Aniston',' Felicity Jones', 'Rosamund Pike', 'Reese Witherspoon']
MPActorDrama15 = ['Eddie Redmayne', 'Steve Carell', 'Benedict Cumberbatch', 'Jake Gyllenhaal', 'David Oyelowo']
MPActorMusicComedy15 = ['Michael Keaton', 'Ralph Fiennes', 'Bill Murray', 'Joaquin Phoenix', 'Christoph Waltz']
MPActressMusicComedy15 = ['Amy Adams', 'Emily Blunt', 'Helen Mirren', 'Julianne Moore', 'Quvenzhane Wallis']
MPSupportingActress15 = ['Patricia Arquette', 'Jessica Chastain', 'Keira Knightley', 'Emma Stone', 'Meryl Streep']
MPSupportingActor15 = ['J.K. Simmons', 'Robert Duvall', 'Ethan Hawke', 'Edward Norton', 'Mark Ruffalo']
MPScreenplay15 = ['Birdman', 'The Grand Budapest Hotel', 'Gone Girl', 'Boyhood', 'The Imitation Game']
MPForeign15 = ['Leviathan', 'Force Majeure', 'Gett: The Trial of Viviane Amsalem', 'Ida', 'Tangerines']
MPAnimated15 = ['How to Train Your Dragon 2', 'Big Hero 6', 'The Book of Life', 'The Boxtrolls', 'The Lego Movie']
MPSong15 = ['Selma','Big Eyes', 'Noah', 'Annie', 'the hunger games: mockingjay - part 1']
MPScore15 = ['The Theory of Everything', 'The Imitation Game', 'Gone Girl', 'Birdman', 'Interstellar']

TVMusicComedy15 = ['Transparent', 'Girls', 'Jane the Virgin', 'Orange Is the New Black', 'Silicon Valley']
TVDrama15 = ['The Affair', 'Game of Thrones', 'Downton Abbey', 'The Good Wife', 'House of Cards']
TVActressDrama15 = ['Ruth Wilson', 'Claire Danes', 'Viola Davis', 'Julianna Margulies', 'Robin Wright']
TVActorDrama15 = ['Kevin Spacey', 'Clive Owen', 'Liev Schreiber', 'James Spader', 'Dominic West']
TVActressComedy15 = ['Gina Rodriguez', 'Lena Dunham', 'Edie Falco', 'Julia Louis-Dreyfus', 'Taylor Schilling']
TVActorComedy15 = ['Jeffrey Tambor', 'Louis C. K.', 'Don Cheadle', 'Ricky Gervais', 'William H. Macy']
TVMiniseries15 = ['Fargo', 'The Missing', 'The Normal Heart', 'Olive Kitteridge', 'True Detective']
TVActressMiniseries15 = ['Maggie Gyllenhaal', 'Jessica Lange', 'Frances McDormand', "Frances O'Connor", 'Allison Tolman']
TVActorMiniSeries15 = ['Billy Bob Thornton', 'Martin Freeman', 'Wood Harrelson', 'Matthew McConaughey', 'Mark Ruffalo']
TVSupportingActress15 = ['Joanna Froggatt', 'Uzo Aduba', 'Kathy Bates', 'Allison Janney', 'Michelle Monaghan']
TVSupportingActor15 = ['Matt Bomer', 'Alan Cumming', 'Colin Hanks', 'Bill Murray', 'Jon Voight']

allNominees15 = [MPDrama15, MPMusicComedy15, MPDirector15, MPActressDrama15, MPActorDrama15, MPActorMusicComedy15, MPActressMusicComedy15, MPSupportingActress15, MPSupportingActor15, MPScreenplay15, MPForeign15,
			   MPAnimated15, MPSong15, MPScore15, TVMusicComedy15, TVDrama15, TVActressDrama15, TVActorDrama15, TVActressComedy15, TVActorComedy15, TVMiniseries15, TVActressMiniseries15,
			   TVActorMiniSeries15,TVSupportingActress15, TVSupportingActor15]
presenters15 = [['Meryl Streep'], 
			 	['Robert Downey, Jr.'], 
			 	['Harrison Ford'], 
			 	['Matthew McConaughey'], 
			 	['Gwyneth Paltrow'], 
			 	['Amy Adams'],
			 	['Ricky Gervais'], 
			 	['Jared Leto'], 
			  	['Jennifer Aniston', 'Benedict Cumberbatch'], 
			  	['Bill Hader', 'Kristen Wiig'], 
			  	["Colin Farrell", "Lupita Nyong'o"], 
			  	['Kevin Hart', 'Salma Hayek'], 
			  	['Prince'], 
			    ['Sienna Miller', 'Vince Vaughn'], 
			    ['Bryan Cranston', 'Kerry Washington'], 
			    ['Adam Levine','Paul Rudd'], 
			    ['Anna Faris','Chris Pratt'],
			    ['David Duchovny', 'Katherine Heigl'], 
			   	['Bryan Cranston','Kerry Washington'], 
			   	['Jane Fonda','Lily Tomlin'],
			   	['Jennifer Lopez','Jeremy Renner'],
			   	['Kate Beckinsale','Adrien Brody'],
			   	['Jennifer Lopez','Jeremy Renner'], 
			  	['Jamie Dornan','Dakota Johnson'],
			  	['Katie Holmes','Seth Meyers'],
			  	['Don Cheadle','Julianna Margulies']]
awardsList15 = ['Best Motion Picture - Drama', 
				'Best Motion Picture - Comedy or Musical', 
				'Best Director - Motion Picture', 
				'Best Performance by an Actress in a Motion Picture - Drama',
			  	'Best Performance by an Actor in a Motion Picture - Drama', 
			  	'Best Performance by an Actor in a Motion Picture - Comedy Or Musical', 
			  	'Best Performance by an Actress in a Motion Picture - Comedy Or Musical',
			  	'Best Performance by an Actress In A Supporting Role in a Motion Picture', 
			  	'Best Performance by an Actor In A Supporting Role in a Motion Picture', 
			  	'Best Screenplay - Motion Picture', 
			  	'Best Foreign Language Film', 
			  	'Best Animated Feature Film', 
			  	'Best Original Song - Motion Picture', 
			  	'Best Original Score - Motion Picture', 
			  	'Best Television Series - Comedy Or Musical', 
			  	'Best Television Series - Drama',
			  	'Best Performance by an Actress In A Television Series - Drama', 
			  	'Best Performance by an Actor In A Television Series - Drama', 
			  	'Best Performance by an Actress In A Television Series - Comedy Or Musical', 
			  	'Best Performance by an Actor In A Television Series - Comedy Or Musical',
			  	'Best Mini-Series Or Motion Picture Made for Television',
			  	'Best Performance by an Actress In A Mini-series or Motion Picture Made for Television', 
			  	'Best Performance by an Actor In A Mini-series or Motion Picture Made for Television', 
			  	'Best Performance by an Actress in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television', 
			  	'Best Performance by an Actor in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television',
			  	'Cecil B. DeMille Award']
searchList = ['Best Motion Picture - Drama', 
			  'Best Motion Picture - Musical or Comedy', 
			  'Best Director - Motion Picture', 
			  'Best Actress in a Motion Picture - Drama',
			  'Best Actor in a Motion Picture - Drama', 
			  'Best Actor in a Motion Picture - Comedy or Musical', 
			  'Best Actress in a Motion Picture - Comedy or Musical',
			  'Best Supporting Actress - Motion Picture', 
			  'Best Supporting Actor - Motion Picture', 
			  'Best Screenplay - Motion Picture', 
			  'Foreign Film', 
			  'Animated Film', 
			  'Best Original Song',
			  'Best Original Score', 
			  'Best TV Comedy or Musical', 
			  'Best TV Drama',
			  'Best Actress in a TV Drama', 
			  'Best Actor in a TV Drama', 
			  'Best Actress in a TV Comedy or Musical', 
			  'Best Actor in a TV Comedy',
			  'Best Miniseries or TV Movie',
			  'Best Actress in a Miniseries or TV Movie', 
			  'Best Actor in a Miniseries or TV Movie', 
			  'Best Supporting Actress in a TV Show, Miniseries or TV Movie', 
			  'Best Supporting Actor in a TV Show, Miniseries or TV Movie',
			  'Cecil B. DeMille Award']
funGoalSearchList = ['Best Dressed',
			  		 'Worst Dressed',
			  		 'worst speech',
			  	 	 'great speech',
			  		 'snub',
			  		 'not funn',
			  		 'hilarious',
			  		 'most handsome']

#function to find all the winnners for the award and output to a json file
def findAllAwards(year, allNominees, awardsList, presenterList, inputFile, outputName):
	#set the start time so we can time how long this takes
	print "Finding awards for " + str(year)
	start_time = time.time()
	results= searchTweets(searchList, allNominees, inputFile)
	elapsed_time = time.time() - start_time
	print "Search length: " + str(elapsed_time)
	winners = results[0]
	allNominees = results[1]

	for i in range(0,len(awardsList)):
		print awardsList[i] + " goes to " + winners[i]
	nomineeList = []
	for nominees in allNominees:
		nomineeList = nominees + nomineeList

	results = {}
	metadata = {}
	names = {}
	hosts = {}
	nominees = {}
	awards = {}
	presenters = {}
	data = {}
	structured = {}
	unstructured = {}
	mappings = {}
	hosts['method'] = "hardcoded"
	hosts['method_description'] = ''
	nominees['method'] = "hardcoded"
	nominees['method_description'] = ''
	awards['method'] = "hardcoded"
	awards['method_description'] = ''
	presenters['method'] = "hardcoded"
	presenters['method_description'] = ''
	metadata['year'] = year
	names['hosts'] = hosts
	names['nominees'] = nominees
	names['awards'] = awards
	names['presenters'] = presenters
	mappings['nominees'] = nominees
	mappings['presenters'] = presenters
	metadata['names'] = names
	metadata['mappings'] = mappings
	unstructured['hosts'] = ['Tina Fey', 'Amy Poehler']
	unstructured['winners'] = winners
	unstructured['awards'] = awardsList

	#get a list of presenters
	presenterUnstructured = []
	for presenter in presenterList:
		presenterUnstructured = presenterUnstructured + presenter
	unstructured['presenters'] = presenterUnstructured
	unstructured['nominees'] = nomineeList
	for i in range(0, len(winners)):
		award = {}
		if i is 25:#the Cecile B DeMille award does not have nominees
			award['nominees']=[]
		else:
			award['nominees'] = allNominees[i]
		award['winner'] = winners[i]
		award['presenters'] = presenterList[i]
		structured[awardsList[i]] = award

	data['unstructured']= unstructured
	data['structured'] = structured
	results['metadata'] = metadata
	results['data'] = data
	with open(outputName, 'w') as outfile:
	    json.dump(OrderedDict(results), outfile)

#finds all the answers to the fun goals
def funGoals(keywords, inputFile,outputName):
	start_time = time.time()
	results = searchFunGoals(keywords,inputFile)
	data = {}
	data['answers'] = results
	elapsed_time = time.time() - start_time
	print "Search length: " + str(elapsed_time)

	with open(outputName, 'w') as outfile: 
		json.dump(OrderedDict(data), outfile)

findAllAwards(2013, allNominees13,awardsList13, presenters13, 'gg2013.json','gg13answers.json')
findAllAwards(2015, allNominees15,awardsList15, presenters15, 'gg15mini.json','gg15answers.json')

funGoals(funGoalSearchList, 'gg2013.json', 'funGoals13.json')
funGoals(funGoalSearchList, 'gg15mini.json', 'funGoals15.json')
	



