import Tkinter
from Tkinter import *
import tkMessageBox
import json

import findwinners
top = Tkinter.Tk()

awardsList =   ['Best Motion Picture - Drama', 
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


json13=open('gg13answers.json')
data13 = json.load(json13)

json15=open('gg15answers.json')
data15 = json.load(json15)

fun13=open('funGoals13.json')
f2013 = json.load(fun13)

fun15=open('funGoals15.json')
f2015 = json.load(fun15)

y= IntVar()
y.set(2015)  # initializing the choice, i.e. Python


def ShowChoice():
    year= y.get()

#called when one of the award buttons is clicked
#retreives the answer from the json file and prints out a message
def awards(index):
    if y.get() == 2015:
        winner = data15['data']['structured'][awardsList[index-1]]['winner']
        nominees = data15['data']['structured'][awardsList[index-1]]['nominees']
        presenter = data15['data']['structured'][awardsList[index-1]]['presenters']
    else:
        winner = data13['data']['structured'][awardsList[index-1]]['winner']
        nominees = data13['data']['structured'][awardsList[index-1]]['nominees']
        presenter = data13['data']['structured'][awardsList[index-1]]['presenters']
    presenters = ''
    for pres in presenter:
        presenters += "\n" + pres
    nomineeList=''
    for nom in nominees: 
        nomineeList += "\n" + nom
    message = "Winner: \n" + winner + "\n===============\nPresented by: " + presenters + "\n===============\nNominees for the award: " + nomineeList
    tkMessageBox.showinfo( "INFO:", message);

#called when a fungoal button is clicked
#retrieves the answer from the json file and prints out a message 
def fungoals(index):
    print ""
    if y.get() ==2015:
        results = f2013['answers'][index-1]

    else:
        results = f2015['answers'][index-1]
    #print out the results
    if len(results)==0:
        message = "Could not find any significant chatter on twitter!"
    else: 
        message = "People are talking about: "
        for person in results: 
            message += "\n" + person 
    tkMessageBox.showinfo( "INFO:", message);


Radiobutton(top,
            text='2015', 
            variable=y, 
            command=ShowChoice,
            value=2015).grid(row=0, column=1)
Radiobutton(top,
            text='2013', 
            variable=y, 
            command=ShowChoice,
            value=2013).grid(row=1, column=1)

# Code to add widgets will go here...
MPD = Tkinter.Button(top, text ="Best Motion Picture - Drama",command= lambda: awards(1),width=55, height=2, wraplength=55)
MPC = Tkinter.Button(top, text ='Best Motion Picture - Comedy or Musical',command= lambda: awards(2),width=55, height=2, wraplength=55)
MPAD= Tkinter.Button(top, text ='Best Director - Motion Picture',command= lambda: awards(3),width=55, height=2, wraplength=55)
MPAcD = Tkinter.Button(top, text ='Best Performance by an Actress in a Motion Picture - Drama',command= lambda: awards(4),width=55, height=2, wraplength=55)
MPAC = Tkinter.Button(top, text ='Best Performance by an Actor in a Motion Picture - Drama',command= lambda: awards(5),width=55, height=2, wraplength=55)
MPAcC = Tkinter.Button(top, text ='Best Performance by an Actor in a Motion Picture - Comedy Or Musical',command= lambda: awards(6) ,width=55, height=2, wraplength=55)
MPSA = Tkinter.Button(top, text ='Best Performance by an Actress in a Motion Picture - Comedy Or Musical',command= lambda: awards(7) ,width=55, height=2, wraplength=55)
MPSAc = Tkinter.Button(top, text ='Best Performance by an Actress In A Supporting Role in a Motion Picture',command= lambda: awards(8),width=55, height=2, wraplength=55)
MPDir = Tkinter.Button(top, text ='Best Performance by an Actor In A Supporting Role in a Motion Picture',command= lambda: awards(9) ,width=55, height=2, wraplength=55)
MPScreen = Tkinter.Button(top, text ='Best Screenplay - Motion Picture',command= lambda: awards(10) ,width=55, height=2, wraplength=55)
MPScore = Tkinter.Button(top, text ='Best Foreign Language Film',command= lambda: awards(11),width=55, height=2, wraplength=55)
MPSong = Tkinter.Button(top, text ='Best Animated Feature Film',command= lambda: awards(12) ,width=55, height=2, wraplength=55)
MPAnimate = Tkinter.Button(top, text ='Best Original Song - Motion Picture',command= lambda: awards(13) ,width=55, height=2, wraplength=55)
MPFor = Tkinter.Button(top, text ='Best Original Score - Motion Picture',command= lambda: awards(14) ,width=55, height=2, wraplength=55)
TVD = Tkinter.Button(top, text ='Best Television Series - Comedy Or Musical',command= lambda: awards(15),width=55, height=2, wraplength=55)
TVC = Tkinter.Button(top, text ='Best Television Series - Drama',command= lambda: awards(16) ,width=55, height=2, wraplength=55)
TVAD = Tkinter.Button(top, text ='Best Performance by an Actress In A Television Series - Drama',command= lambda: awards(17) ,width=55, height=2, wraplength=55)
TVAcD = Tkinter.Button(top, text ='Best Performance by an Actor In A Television Series - Drama',command= lambda: awards(18) ,width=55, height=2, wraplength=55)
TVAC = Tkinter.Button(top, text ='Best Performance by an Actress In A Television Series - Comedy Or Musical',command= lambda: awards(19) ,width=55, height=2, wraplength=55)
TVAcC = Tkinter.Button(top, text ='Best Performance by an Actor In A Television Series - Comedy Or Musical',command= lambda: awards(20) ,width=55, height=2, wraplength=55)
MiniA = Tkinter.Button(top, text ='Best Mini-Series Or Motion Picture Made for Television',command= lambda: awards(21) ,width=55, height=2, wraplength=55)
MiniAc = Tkinter.Button(top, text ='Best Performance by an Actress In A Mini-series or Motion Picture Made for Television',command= lambda: awards(22) ,width=55, height=2, wraplength=55)
MiniSupA= Tkinter.Button(top, text ='Best Performance by an Actor In A Mini-series or Motion Picture Made for Television',command= lambda: awards(23),width=55, height=2, wraplength=55)
MiniSupAc = Tkinter.Button(top, text ='Best Performance by an Actress in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television',command= lambda: awards(24) ,width=55, height=2, wraplength=55)
BestMini = Tkinter.Button(top, text ='Best Performance by an Actor in a Supporting Role in a Series, Mini-Series or Motion Picture Made for Television',command= lambda: awards(25),width=55, height=2, wraplength=55)
CBD = Tkinter.Button(top, text ="Cecil B. DeMille Award",command= lambda: awards(26) ,width=55, height=2, wraplength=55)
BestD = Tkinter.Button(top, text ="Best Dressed",command= lambda: fungoals(1) ,width=55, height=2, wraplength=55)
WorstD = Tkinter.Button(top, text ="Worst Dressed",command= lambda: fungoals(2),width=55, height=2, wraplength=55)
WorstS = Tkinter.Button(top, text ="Worst Speech",command= lambda: fungoals(3),width=55, height=2, wraplength=55)
BestS = Tkinter.Button(top, text ="Best Speech",command= lambda: fungoals(4),width=55, height=2, wraplength=55)
Snub = Tkinter.Button(top, text ="Biggest Snub",command= lambda: fungoals(5),width=55, height=2, wraplength=55)
LFunny = Tkinter.Button(top, text ="Least Funny",command= lambda: fungoals(6),width=55, height=2, wraplength=55)
Funny = Tkinter.Button(top, text ="Funniest",command= lambda: fungoals(7),width=55, height=2, wraplength=55)
Handsome = Tkinter.Button(top, text ="Most Handsome",command= lambda: fungoals(8),width=55, height=2, wraplength=55)
w = Text(top, width=40, height=1,pady=0)    
w2 = Text(top, width=40, height=1,pady=0)


w.insert(INSERT, "Select a year on the right. Then click")
w2.insert(INSERT, "one of the buttons below for more info")

w.grid(row=0, column=0)
w2.grid(row=1, column=0)
MPD.grid(row=2,column=0)
MPC.grid(row=3,column=0)
MPAD.grid(row=4,column=0)
MPAcD.grid(row=5,column=0)
MPAC.grid(row=6,column=0)
MPAcC.grid(row=7,column=0)
MPSA.grid(row=8,column=0)
MPSAc.grid(row=9,column=0)
MPDir.grid(row=10,column=0)
MPScreen.grid(row=11,column=0)
MPScore.grid(row=12,column=0)
MPSong.grid(row=13,column=0)
MPAnimate.grid(row=2,column=1)
MPFor.grid(row=3,column=1)
TVD.grid(row=4,column=1)
TVC.grid(row=5,column=1)
TVAD.grid(row=6,column=1)
TVAcD.grid(row=7,column=1)
TVAC.grid(row=8,column=1)
TVAcC.grid(row=9,column=1)
MiniA.grid(row=10,column=1)
MiniAc.grid(row=11,column=1)
MiniSupA.grid(row=12,column=1)
MiniSupAc.grid(row=13,column=1)
BestMini.grid(row=2,column=2)
CBD.grid(row=3,column=2)
BestD.grid(row=4,column=2)
WorstD.grid(row=5,column=2)
WorstS.grid(row=6,column=2)
BestS.grid(row=7,column=2)
Snub.grid(row=8,column=2)
LFunny.grid(row=9,column=2)
Funny.grid(row=10,column=2)
Handsome.grid(row=11,column=2)

top.mainloop()