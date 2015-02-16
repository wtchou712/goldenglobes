import Tkinter
from Tkinter import *
import tkMessageBox
top = Tkinter.Tk()

def info(phrase):
	#phrase= findinfo(phrase,year);
	#phrase= getinfo(phrase,year)
	phrase=phrase;
	tkMessageBox.showinfo( "INFO:", phrase);


y= IntVar()
y.set(2015)  # initializing the choice, i.e. Python


def ShowChoice():
    year= y.get()


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
MPD = Tkinter.Button(top, text ="Best Motion Picture - Drama",command= lambda: info("1"),width=40, height=2, wraplength=40)
MPC = Tkinter.Button(top, text ="Best Motion Picture - Musical or Comedy",command= lambda: info("2"),width=40, height=2, wraplength=40)
MPAD= Tkinter.Button(top, text ="Best Performance in a Motion Picture - Drama, Actor",command= lambda: info("3"),width=40, height=2, wraplength=40)
MPAcD = Tkinter.Button(top, text ="Best Performance in a Motion Picture - Drama, Actress",command= lambda: info("4"),width=40, height=2, wraplength=40)
MPAC = Tkinter.Button(top, text ="Best Performance in a Motion Picture - Musical or Comedy, Actor",command= lambda: info("5"),width=40, height=2, wraplength=40)
MPAcC = Tkinter.Button(top, text ="Best Performance in a Motion Picture - Musical or Comedy, Actress",command= lambda: info("6") ,width=40, height=2, wraplength=40)
MPSA = Tkinter.Button(top, text ="Best Supporting Performance in a Motion Picture - Actor",command= lambda: info("7") ,width=40, height=2, wraplength=40)
MPSAc = Tkinter.Button(top, text ="Best Supporting Performance in a Motion Picture - Actress",command= lambda: info("8"),width=40, height=2, wraplength=40)
MPDir = Tkinter.Button(top, text ="Best Director",command= lambda: info("9") ,width=40, height=2, wraplength=40)
MPScreen = Tkinter.Button(top, text ="Best Screenplay",command= lambda: info("10") ,width=40, height=2, wraplength=40)
MPScore = Tkinter.Button(top, text ="Best Original Score",command= lambda: info("11"),width=40, height=2, wraplength=40)
MPSong = Tkinter.Button(top, text ="Best Original Song",command= lambda: info("12") ,width=40, height=2, wraplength=40)
MPAnimate = Tkinter.Button(top, text ="Best Animated Feature Film",command= lambda: info("13") ,width=40, height=2, wraplength=40)
MPFor = Tkinter.Button(top, text ="Best Foreign Language Film",command= lambda: info("14") ,width=40, height=2, wraplength=40)
TVD = Tkinter.Button(top, text ="Best Series - Drama",command= lambda: info("15"),width=40, height=2, wraplength=40)
TVC = Tkinter.Button(top, text ="Best Series - Musical or Comedy",command= lambda: info("16") ,width=40, height=2, wraplength=40)
TVAD = Tkinter.Button(top, text ="Best Performance in a Television Series - Drama, Actor",command= lambda: info("17") ,width=40, height=2, wraplength=40)
TVAcD = Tkinter.Button(top, text ="Best Performance in a Television Series - Drama, Actress",command= lambda: info("18") ,width=40, height=2, wraplength=40)
TVAC = Tkinter.Button(top, text ="Best Performance in a Television Series - Musical or Comedy, Actor",command= lambda: info("19") ,width=40, height=2, wraplength=40)
TVAcC = Tkinter.Button(top, text ="Best Performance in a Television Series - Musical or Comedy, Actress",command= lambda: info("20") ,width=40, height=2, wraplength=40)
MiniA = Tkinter.Button(top, text ="Best Performance in a Miniseries or Television Film - Actor",command= lambda: info("21") ,width=40, height=2, wraplength=40)
MiniAc = Tkinter.Button(top, text ="Best Performance in a Miniseries or Television Film - Actress",command= lambda: info("22") ,width=40, height=2, wraplength=40)
MiniSupA= Tkinter.Button(top, text ="Best Supporting Performance in a Series, Miniseries, or Television Film - Actor",command= lambda: info("23"),width=40, height=2, wraplength=40)
MiniSupAc = Tkinter.Button(top, text ="Best Supporting Performance in a Series, Miniseries, or Television Film - Actress",command= lambda: info("24") ,width=40, height=2, wraplength=40)
BestMini = Tkinter.Button(top, text ="Best Miniseries or Television Film",command= lambda: info("25"),width=40, height=2, wraplength=40)
All = Tkinter.Button(top, text ="All Awards",command= lambda: info("26") ,width=40, height=2, wraplength=40)
BestD = Tkinter.Button(top, text ="Best Dressed",command= lambda: info("27") ,width=40, height=2, wraplength=40)
WorstD = Tkinter.Button(top, text ="Worst Dressed",command= lambda: info("28"),width=40, height=2, wraplength=40)
CBD = Tkinter.Button(top, text ="Cecil B. DeMille Award",command= lambda: info("29") ,width=40, height=2, wraplength=40)
Funny = Tkinter.Button(top, text ="Funniest at Awards",command= lambda: info("30"),width=40, height=2, wraplength=40)
w = Text(top, width=40, height=1,pady=0)
w2 = Text(top, width=40, height=1,pady=0)



w.insert(INSERT, "Select a year on the right.  Then click")
w2.insert(INSERT, "one of the bottons below for more info")

w.grid(row=0, column=0)
w2.grid(row=1, column=0)
MPD.grid(row=2,column=0)
MPC.grid(row=2,column=1)
MPAD.grid(row=3,column=0)
MPAcD.grid(row=3,column=1)
MPAC.grid(row=4,column=0)
MPAcC.grid(row=4,column=1)
MPSA.grid(row=5,column=0)
MPSAc.grid(row=5,column=1)
MPDir.grid(row=6,column=0)
MPScreen.grid(row=6,column=1)
MPScore.grid(row=7,column=0)
MPSong.grid(row=7,column=1)
MPAnimate.grid(row=8,column=0)
MPFor.grid(row=8,column=1)
TVD.grid(row=9,column=0)
TVC.grid(row=9,column=1)
TVAD.grid(row=10,column=0)
TVAcD.grid(row=10,column=1)
TVAC.grid(row=11,column=0)
TVAcC.grid(row=11,column=1)
MiniA.grid(row=12,column=0)
MiniAc.grid(row=12,column=1)
MiniSupA.grid(row=13,column=0)
MiniSupAc.grid(row=13,column=1)
BestMini.grid(row=14,column=0)
CBD.grid(row=14,column=1)
All.grid(row=15,column=0)
BestD.grid(row=15,column=1)
WorstD.grid(row=16,column=0)
Funny.grid(row=16,column=1)



top.mainloop()