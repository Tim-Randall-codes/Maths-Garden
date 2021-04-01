import tkinter as tk
import csv
from random import randint

win2 = tk.Tk()
win3 = tk.Tk()
var = tk.IntVar()
gtype = ''
ans = 0

#make the things that the game function only creates once the game function
#then the other things it has to do over and over can be different functions
#for example creating the random numbers
#comparing the user input to the answers
#updating the scores of correct and incorrect.
#determining if the user entered an integer or not

def gamer():
    pass

def addg():
    global gtype
    gtype = '+'
    game()

def subg():
    global gtype
    gtype = '-'
    game()

def multg():
    global gtype
    gtype = '*'
    game()

def divg():
    global gtype
    gtype = '/'
    game()

def allg():
    global gtype
    gtype = 'all'
    game()

def game():
    win3.deiconify()
    win3.geometry('800x600')
    win3.title('Go, go, GO!! ^^')
    global digs
    global answere
    global entryerror
    global rn
    global rn2
    global correct
    global incorrect
    global qdisplay
    global cdisplay
    global incdisplay
    global userinput
    global drn
    global drn2
    global rall
    global gtype
    global allon
    correct = 0
    incorrect = 0
    digs = (str(var.get()))
    if digs == '1' or digs == '0':
        rn = randint(0, 9)
        rn2 = randint(0, 9)
    elif digs == '2':
        rn = randint(10, 99)
        rn2 = randint(10, 99)
    else:
        rn = randint(100, 999)
        rn2 = randint(100, 999)
    drn = randint(10, 999)
    drn2 = randint(1, 12)
    rall = randint(0, 3)
    allon = False
    if gtype == 'all':
        allon = True
        rn = randint(1, 999)
        rn2 = randint(1, 999)
        if rall == 0:
            gtype = '+'
        elif rall == 1:
            gtype = '-'
        elif rall == 2:
            gtype = '*'
        elif rall == 3:
            gtype = '/'
    else:
        pass
    qdisplay = tk.Label(win3, text='')
    qdisplay.grid(column=0, row=2, sticky=tk.E)
    if gtype == '+' or gtype == '-' or gtype == '*':
        qdisplay['text'] = str(rn) + ' ' + str(gtype) + ' '  + str(rn2) + ' ='
    elif gtype == '/':
        qdisplay['text'] = str(drn) + ' ' + str(gtype) + ' '  + str(drn2) + ' ='
    explaing = tk.Label(win3, text='Put your answer in the box and answer')
    explaing.grid(column=0, row=0)
    explaing2 = tk.Label(win3, text='See how many you can do in two minutes')
    explaing2.grid(column=0, row=1)
    resultd = tk.Label(win3, text='')
    resultd.grid(column=1, row=1)
    answere = tk.Entry(win3, width=15)
    answere.grid(column=1, row=2)
    entryerror = tk.Label(win3, text='')
    entryerror.grid(column=1, row=3)
    answerb = tk.Button(win3, text='Answer', command=gamecon)
    answerb.grid(column=2, row=2)
    cdisplay = tk.Label(win3, text="Correct: "+str(correct))
    cdisplay.grid(column=3, row=0, sticky=tk.E)
    incdisplay = tk.Label(win3, text="Incorrect: "+str(incorrect))
    incdisplay.grid(column=3, row=1, sticky=tk.E)
    print(rn, rn2)
    print(drn, drn2)
    print(gtype)
    win2.withdraw()
    win3.mainloop()

    
def gamecon():
    global correct
    global incorrect
    letpass = True
    while True:
        try:
            ans = int(answere.get())
            letpass = True
            break
        except ValueError:
            entryerror['text'] = 'Enter whole numbers only'
            letpass = False
            break
    if letpass == True:
        entryerror['text'] = ''
        if gtype == '+':
            if rn + rn2 == ans:
                correct += 1
                cdisplay['text'] = "Correct: " + str(correct)
                rnreset()
            else:
                incorrect += 1
                incdisplay['text'] = "Incorrect: " + str(incorrect)
                rnreset()
        elif gtype == '-':
            if rn - rn2 == ans:
                correct += 1
                cdisplay['text'] = "Correct: " + str(correct)
                rnreset()
            else:
                incorrect += 1
                incdisplay['text'] = "Incorrect: " + str(incorrect)
                rnreset()
        elif gtype == '*':
            if rn * rn2 == ans:
                correct += 1
                cdisplay['text'] = "Correct: " + str(correct)
                rnreset()
            else:
                incorrect += 1
                incdisplay['text']= "Incorrect: " + str(incorrect)
                rnreset()
        elif gtype == '/':
            if drn / drn2 == ans:
                correct += 1
                cdisplay['text']= "Correct: " + str(correct)
                rnreset()
            else:
                incorrect += 1
                incdisplay['text'] = "Incorrect: " + str(incorrect)
                rnreset()
        print(rn, rn2)
        print(drn, drn2)
        print(gtype)
    else:
        pass

def rnreset():
    global rn
    global rn2
    global drn
    global drn2
    global qdisplay
    global rall
    global gtype
    global allon
    rall = randint(0, 3)
    if digs == '1' or digs == '0':
        rn = randint(0, 9)
        rn2 = randint(0, 9)
    elif digs == '2':
        rn = randint(10, 99)
        rn2 = randint(10, 99)
    else:
        rn = randint(100, 999)
        rn2 = randint(100, 999)
    drn = randint(10, 999)
    drn2 = randint(1, 12)
    if allon == True:
        rn = randint(1, 999)
        rn2 = randint(1, 999)
        if rall == 0:
            gtype = '+'
        elif rall == 1:
            gtype = '-'
        elif rall == 2:
            gtype = '*'
        elif rall == 3:
            gtype = '/'
    else:
        pass
    if gtype == '+' or gtype == '-' or gtype == '*':
        qdisplay['text'] = str(rn) + ' ' + str(gtype) + ' '  + str(rn2) + ' ='
    elif gtype == '/':
        qdisplay['text'] = str(drn) + ' ' + str(gtype) + ' ' + str(drn2) + ' ='
    
def menu():
    global win1
    win1.destroy()
    win2.deiconify()
    win2.geometry('800x600')
    win2.title('Maths Garden')
    addl = tk.Label(win2, text="Addition game: See how many addition problems \
you can do in two minutes")
    addl.grid(column=0, row=0, sticky=tk.W)
    subl = tk.Label(win2, text="Subtraction game: See how many subtraction \
problems you can do in two minutes")
    subl.grid(column=0, row=1, sticky=tk.W)
    multl = tk.Label(win2, text="Multiplication game: See how many multiplication\
 problems you can do in two minutes")
    multl.grid(column=0, row=2, sticky=tk.W)
    divl = tk.Label(win2, text="Division game: See how many division problems \
you can do in two minutes")
    divl.grid(column=0, row=3, sticky=tk.W)
    allgamel = tk.Label(win2, text="All game: hard mode consists of addition, subtraction\
 multiplication, division problems")
    allgamel.grid(column=0, row=4, sticky=tk.W)
    addb = tk.Button(win2, text="Play", command=addg)
    addb.grid(column=1, row=0)
    subb = tk.Button(win2, text="Play", command=subg)
    subb.grid(column=1, row=1)
    multb = tk.Button(win2, text="Play", command=multg)
    multb.grid(column=1, row=2)
    divb = tk.Button(win2, text="Play", command=divg)
    divb.grid(column=1, row=3)
    allb = tk.Button(win2, text="Play", command=allg)
    allb.grid(column=1, row=4)

    dl = tk.Label(win2, text="Select number of digits (if no selection one\
 will be used as the default.")
    dl.grid(column=0, row=5, sticky=tk.W)
    d1 = tk.Radiobutton(win2, text="One digit", variable=var, value=1)
    d1.grid(column=0, row=6)
    d2 = tk.Radiobutton(win2, text="Two digits", variable=var, value=2)
    d2.grid(column=0, row=7)
    d3 = tk.Radiobutton(win2, text="Three digits", variable=var, value=3)
    d3.grid(column=0, row=8)
    win3.withdraw()
    win2.mainloop()

def window1():
    global win1
    win1 = tk.Tk()
    win1.geometry('800x600')
    win1.title('Maths Garden')
    heading = tk.Label(win1, text="Maths Garden")
    heading.grid(column=0, row=0, sticky=tk.N)
    explain1 = tk.Label(win1, text='It is important to know maths')
    explain1.grid(column=0, row=1, sticky=tk.N)
    continueb = tk.Button(win1, text="Continue", command=menu)
    continueb.grid(column=0, row=2, sticky=tk.N)
    win3.withdraw()
    win2.withdraw()
    win1.mainloop()

window1()
