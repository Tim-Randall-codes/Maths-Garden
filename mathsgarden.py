import tkinter as tk
from random import randint
import time
from pygame import mixer
from PIL import Image, ImageTk

mixer.init()
mixer.music.load("Ambient come back.mp3")

win2 = tk.Tk()
win3 = tk.Tk()
win4 = tk.Tk()
var = tk.IntVar()
gtype = ''
ans = 0

# make some flowers and plants graphics and put them in the program
# have a song play in the program
# format where the things are on the page better.

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

def after_game():
    print('after game')
    win4.deiconify()
    win4.geometry('800x600+100+100')
    win4.title('Moment of Turth! ^^')

    global correct
    global incorrect
    result_one = tk.Label(win4, text="Results:")
    result_one.grid(column=0, row=0)
    result_two = tk.Label(win4, text="You got "+str(correct)+" correct and "\
                          +str(incorrect)+" incorrect.")
    result_two.grid(column=0, row=1)
    backtomenub = tk.Button(win4, text="Back to menu", command=menu)
    backtomenub.grid(column=0, row=2)
    plant_4 = tk.PhotoImage(master=win4, file="pic5.png")
    plant_4_l = tk.Label(win4, image=plant_4)
    plant_4_l.place(x=500, y=300)
    win3.withdraw()
    win4.mainloop()

def timer():
    global time_display
    t=120
    for times in range(t):
        t-=1
        if t >= 70:
            time_display['text'] = '1:'+str(t-60)
        elif t >= 60:
            time_display['text'] = '1:0'+str(t-60)
        elif t >=10:
            time_display['text'] = '0:' +str(t)
        else:
            time_display['text'] = '0:0' +str(t)
        win3.update()
        time.sleep(1)
    after_game()
    print('this happens afterwards')       

def game():
    win3.deiconify()
    win3.geometry('800x600+100+100')
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
    global time_display
    global answere
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
    time_display = tk.Label(win3, text='')
    time_display.grid(column=0, row=4)
    answerb = tk.Button(win3, text='Answer', command=gamecon)
    answerb.grid(column=2, row=2)
    cdisplay = tk.Label(win3, text="Correct: "+str(correct))
    cdisplay.grid(column=3, row=0, sticky=tk.E)
    incdisplay = tk.Label(win3, text="Incorrect: "+str(incorrect))
    incdisplay.grid(column=3, row=1, sticky=tk.E)
    plant_2 = tk.PhotoImage(master=win3, file="pic3.png")
    plant_2_l = tk.Label(win3, image=plant_2)
    plant_2_l.place(x=500, y=200)
    plant_3 = tk.PhotoImage(master=win3, file="pic4.png")
    plant_3_l =tk.Label(win3, image=plant_3)
    plant_3_l.place(x=250, y=180)
    win2.withdraw()
    timer()
    print(rn, rn2)
    print(drn, drn2)
    print(gtype)
    win3.mainloop()
    
def gamecon():
    global correct
    global incorrect
    global answere
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
    answere.delete(0, tk.END)

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
    win2.deiconify()
    win2.geometry('800x600+100+100')
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
    plant_1 = tk.PhotoImage(master=win2, file="pic2.png")
    plant_1_l = tk.Label(win2, image=plant_1)
    plant_1_l.grid(row=9, column=9)
    win4.withdraw()
    win1.withdraw()
    win3.withdraw()
    win2.mainloop()

def window1():
    global win1
    win1 = tk.Tk()
    win1.geometry('800x600+100+100')
    win1.title('Maths Garden')
    logo = tk.PhotoImage(master = win1, file="IMG_0201.png")
    heading = tk.Label(win1, image=logo)
    heading.place(x=200, y=200)
    explain1 = tk.Label(win1, text='It is important to know arithmatic, even \
if you have a calculator. \nBeing able to do this in your head can help you \
quickly solve problems.')
    explain1.place(x=200, y=300)
    continueb = tk.Button(win1, text="Continue", command=menu)
    continueb.place(x=380, y=400)
    win3.withdraw()
    win2.withdraw()
    win4.withdraw()
    win1.mainloop()

window1()
