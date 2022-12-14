import os
from datetime import date
from tkinter import *
from darktitlebar import *

today = date.today()  # getting date
d4 = today.strftime("%Y")  # setting d4 only as current year


def monthfolcreate():  # creating month folders
    newpath = fr'{a}\January'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    newpath = fr'{a}\February'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    newpath = fr'{a}\March'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    newpath = fr'{a}\April '
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    newpath = fr'{a}\May'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    newpath = fr'{a}\June'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    newpath = fr'{a}\July'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    newpath = fr'{a}\August'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    newpath = fr'{a}\September'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    newpath = fr'{a}\October'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    newpath = fr'{a}\November'
    if not os.path.exists(newpath):
        os.makedirs(newpath)

    newpath = fr'{a}\December'
    if not os.path.exists(newpath):
        os.makedirs(newpath)


def monthcreate():  # creating all date folders
    jan = 0
    feb = 0
    mar = 0
    apr = 0
    may = 0
    jun = 0
    jul = 0
    aug = 0
    sep = 0
    oct = 0
    nov = 0
    dec = 0

    for i in range(31):
        jan = jan + 1
        newpath = fr'{a}\January\{jan}-1-{d4}'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    for i in range(28):
        feb = feb + 1
        newpath = fr'{a}\February\{feb}-2-{d4}'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    for i in range(31):
        mar = mar + 1
        newpath = fr'{a}\March\{mar}-3-{d4}'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    for i in range(30):
        apr = apr + 1
        newpath = fr'{a}\April\{apr}-4-{d4}'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    for i in range(31):
        may = may + 1
        newpath = fr'{a}\May\{may}-5-{d4}'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    for i in range(30):
        jun = jun + 1
        newpath = fr'{a}\June\{jun}-6-{d4}'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    for i in range(31):
        jul = jul + 1
        newpath = fr'{a}\July\{jul}-7-{d4}'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    for i in range(31):
        aug = aug + 1
        newpath = fr'{a}\August\{aug}-8-{d4}'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    for i in range(30):
        sep = sep + 1
        newpath = fr'{a}\September\{sep}-9-{d4}'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    for i in range(31):
        oct = oct + 1
        newpath = fr'{a}\October\{oct}-10-{d4}'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    for i in range(30):
        nov = nov + 1
        newpath = fr'{a}\November\{nov}-11-{d4}'
        if not os.path.exists(newpath):
            os.makedirs(newpath)

    for i in range(31):
        dec = dec + 1
        newpath = fr'{a}\December\{dec}-12-{d4}'
        if not os.path.exists(newpath):
            os.makedirs(newpath)


def submit():  # submit button command
    global a
    a = e.get()
    if os.path.exists(path=a):
        w.config(text="Folder already exists cant make one!.")
        window.after(2000, window.update())
        exit()
    monthcreate()
    window.after(1000, window.update())
    monthfolcreate()
    w.config(text="Folders Created.")
    window.after(2000, window.update())
    exit()


def enter(self):  # Return key command
    global a
    a = e.get()
    if os.path.exists(path=a):
        w.config(text="Folder already exists cant make one!.")
        window.after(2000, window.update())
        exit()
    monthcreate()
    window.after(1000, window.update())
    monthfolcreate()
    w.config(text="Folders Created.")
    window.after(2000, window.update())
    exit()


def change_i():  # button img change
    if submitbtn.image == buttonimg:
        # start_recording()

        submitbtn.config(image=buttonimg2)
        submitbtn.image = buttonimg2
        window.after(5, window.update())
        submitbtn.config(image=buttonimg)
        submitbtn.image = buttonimg
    else:
        # stop_recording()

        submitbtn.config(image=buttonimg)
        submitbtn.image = buttonimg


def funcs(): # combining both change_i and submit func to work together
    change_i()
    submit()

# creating window
window = Tk()
window.eval('tk::PlaceWindow . center')
window.resizable(False, False)
window.geometry('300x200')
window.title('Folder creator')
window.config(bg='#111111')
p1 = PhotoImage(file='icon.png')
window.iconphoto(False, p1)
window.bind('<Return>', enter)
dark_title_bar(window)

# text on screen
w1 = Label(window, text='Insert folder name or directory:')
w1.place(x=30, y=50)
w1.config(bg='#111111', font=('VAG Rounded', 13), fg='white')

# 2nd text on screen
w = Label(window, text='')
w.place(y=500, x=4030)
w.pack(side=BOTTOM)
w.config(fg='white', font=('VAG Rounded', 13), bg='#111111')

# submit button
submitbtn = Button(window, text="", command=funcs)
buttonimg = PhotoImage(file="button.png")
submitbtn.image = buttonimg
buttonimg2 = PhotoImage(file='button2.png')
submitbtn.place(relx=0.5, rely=0.5, anchor=CENTER, x=115)
submitbtn.config(bg='#111111', bd=0, fg='white', font=('VAG Rounded', 13), image=buttonimg, activebackground='#111111')

# entry box
e = Entry()
e.place(relx=0.5, rely=0.5, anchor=CENTER, x=-33)
e.config(font=('Arial', 20), bg='#151515', insertbackground='white', fg='white', bd=0, width=15)
e.focus_force()

window.mainloop()
