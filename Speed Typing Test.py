#importing all libraries
from tkinter import *
from timeit import default_timer as T
import random as R

#Creating window using GUI
window=Tk()
window.title("Typing Test")

#Definig the size of window
window.geometry("800x250")
x=0

#Defining function for the test
def game():
    global x
    #loop for destroying the window after test ON
    if x==0:
        window.destroy()
        x+=1
    
    #function for results of the test
    def check_result():
        if entry.get() == words[word]:
            '''Start time is when window is opened
               End time is when window is destroyed'''
            end=T()
            print("Speed of Typing is: ",end)
        else:
            print("Wrong output!")
        
    words=['Code Clause',"Coding","Python","System","Software","Programming","IARE","Internship"]

    #Giving random words for testing.....
    word=R.randint(0,(len(words)-1))

    #Start Timer using Timeit function
    start=T()
    windows=Tk()
    windows.geometry("800x250")

    #Labeling in window using label method from tkinter
    x2=Label(windows, text=words[word], font="calibre 24")

    #Labeling place
    x2.place(x=300, y=10)
    x3=Label(windows, text="Start Texting", font="calibre 24")
    x3.place(x=250, y=80)
    entry=Entry(windows)
    entry.place(x=450, y=100)

    #Buttons to submit output and check results
    bDone=Button(windows, text="Done", command=check_result, width=12, bg='green')
    bDone.place(x=300, y=150)
    bTry=Button(windows, text="Try Again", command=game, width=12, bg='orange')
    bTry.place(x=400, y=150)
x1=Label(window, text="Let's Start Playing------", font="calibre 24")
x1.place(x=200, y=100)

bStart=Button(window, text="Go..", command=game, width=15, bg='green')
bStart.place(x=300, y=200)

#calling window
window.mainloop()