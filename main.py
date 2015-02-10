from goldenglobe import findinfo

directory = {'Ben Affleck': 'Argo', 'Kathryn Bigelow' : "Zero Dark Thirty", 'Ang Lee': 'Life of Pi', 'Steven Speilberg': 'Lincoln',
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

MPDrama = ["Lincoln", "Django Unchained", "Life of Pi", "Argo", "Zero Dark Thirty"]
MPMusicComedy = ["The Best Exotic Marigold Hotel", "Les Miserables", "Moonrise Kingdom", "Salmon Fishing in the Yemen", "Silver Linings Playbook"]
MPDirector = ["Ben Affleck", "Kathryn Bigelow", "Ang Lee", "Steven Steilberg", "Quentin Tarantino"]
MPActressDrama = ["Jessica Chastain", "Marion Cotillard", 'Helen Mirren', 'Naomi Watts', 'Rachel Weisz']
MPActorDrama = ['Daniel Day-Lewis', 'Richard Gere', 'John Hawkes', 'Joaquin Phoenix', 'Denzel Washington']
MPActorMusicComedy = ['Jack Black', 'Bradley Cooper', 'Hugh Jackman', 'Ewan McGregor', 'Bill Murray']
MPActressMusicComedy = ['Emily Blunt', 'Judi Dench', 'Jennifer Lawrence', 'Maggie Smith', 'Meryl Streep']
MPSupportingActress = ['Amy Adams', 'Sally Field', 'Anne Hathaway', 'Helen Hunt', 'Nicole Kidman']
MPSupportingActor = ['Alan Arkin', 'Leonardo DiCaprio', 'Philip Seymour Hoffman', 'Tommy Lee Jones', 'Christoph Waltz']
MPScreenplay = ['Mark Boal', 'Tony Kushner', "David O'Russell", 'Quentin Tarantino', 'Chris Terrio']
MPForeign = ['Amour','A Royal Affair', 'The Intouchables', 'Kon-Tiki', 'Rust and Bone']
MPAnimated = ['Rise of the Guardians', 'Brave', 'Frankenweenie', 'Hotel Transylvania', 'Wreck-It Ralph']
MPSong = ['For You', 'Not Running Anymore', 'Safe & Sound', 'Skyfall', 'Suddenly']
MPScore = ['Mychael Danna', 'Alexandre Desplat', 'Dario Marianelli', 'Tom Tykwer, Johnny Klimek, Reinhold Heil', 'John Williams']

TVMusicComedy = ['The Big Bang Theory', 'Episodes' , 'Girls', 'Modern Family', 'Smash']
TVDrama = ['Breaking Bad', 'Boardwalk Empire', 'Downtown Abbey', 'Homeland', 'The Newsroom']
TVActressDrama = ['Connie Britton', 'Glenn Close', 'Claire Danes', 'Michelle Dockery', 'Julianna Margulies']
TVActorDrama = ['Steve Buscemi', 'Bryan Cranston', 'Jeff Daniels', 'Jon Hamm', 'Damian Lewis']
TVActressComedy = ['Zooey Deschanel', 'Julia Louis-Dreyfous', 'Lena Dunham', 'Tina Fey', 'Amy Poehler']
TVActorComedy = ['Alec Baldwin', 'Don Cheadle', 'Louis C.K.', 'Matt LeBlanc', 'Jim Parsons']
TVMiniseries = ['Game Change', 'The Girl', 'Hatfields & McCoys', 'The Hour', 'Political Animals']
TVActressMiniseries = ['Nicole Kidman', 'Jessica Lange', 'Sienna Miller', 'Julianne Moore', 'Sigourney Weaver']
TVActorMiniSeries = ['Kevin Costner', 'Benedict Cumberbatch', 'Woody Harrelson', 'Toby Jones', 'Clive Owen']
TVSupportingActress = ['Hayden Panettiere', 'Archie Panjabi', 'Sarah Paulson' , 'Maggie Smith', 'Sofia Vergara']
TVSupportingActor = ['Max Greenfield', 'Ed Harris', 'Danny Huston', 'Mandy Patinkin', 'Eric Stonestreet']


print "1: Best Motion Picture - Drama"
print "2: X"
print "3: X"
print "4: X"
print "5: X"
print "6: X"
print "7: X"
print "8: X"
print "9: X"
print "10: X"
print "11: X"
print "12: X"
print "13: X"
print "14: X"
print "15: X"
print "16: X"
print "17: X"
print "18: X"
print "19: X"
print "20: X"
print "21: X"
print "22: X"
print "23: X"
print "24: X"
print "25: X"
print "26: X"

var = raw_input("Choose the number of award you want to see: ")
print "you entered", var

if (var == "1"):
	print "u made it here"
	top20=findinfo("best supporting actress")
	unis=top20[0]
	bis=top20[1]
	uniarray=[]
	biarray=[]
	for x in range(0,5):
		uniarray.append(unis[x][0])
	for x in range(0,5):
		temp = bis[x][0]
		biarray.append(temp)
	print "================================================"
	#for x in range (0,len(uniarray)):
	#	print uniarray[x]
	print "================================================"
	#for x in range (0,len(biarray)):
	#	print biarray[x]
	for y in range(0,len(MPSupportingActress)):
		for x in range (0,5):
			temp = biarray[x]
			first=temp[0]
			second=temp[1]
			nominee = MPSupportingActress[y]
			nominee = nominee.lower()
			#print nominee
			#print first
			#print second
			#print uniarray[x]
			#print MPDrama[y]
			print "+++++++++++++++++++++++++++++++++++++"
			if first or second in nominee:
				if uniarray[x] in nominee:
					print MPSupportingActress[y]
				break
					#y=len(MPDrama)
	