import os
from datetime import date
from tkinter import *
from darktitlebar import *
import atexit

today = date.today()  # getting date
d4 = today.strftime("%Y")  # setting d4 only as current year

def exittask():
    os.remove("__pycache__/darktitlebar.cpython-311.pyc")
    os.rmdir("__pycache__")

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
        os.remove("__pycache__/darktitlebar.cpython-311.pyc")
        os.rmdir("__pycache__")
        exit()
    monthcreate()
    window.after(1000, window.update())
    monthfolcreate()
    w.config(text="Folders Created.")
    window.after(2000, window.update())
    os.remove("__pycache__/darktitlebar.cpython-311.pyc")
    os.rmdir("__pycache__")
    open = a
    open = os.path.realpath(open)
    os.startfile(open)
    exit()


def enter(self):  # Return key command
    global a
    a = e.get()
    if os.path.exists(path=a):
        w.config(text="Folder already exists cant make one!.")
        window.after(2000, window.update())
        os.remove("__pycache__/darktitlebar.cpython-311.pyc")
        os.rmdir("__pycache__")
        exit()
    monthcreate()
    window.after(1000, window.update())
    monthfolcreate()
    w.config(text="Folders Created.")
    window.after(2000, window.update())
    os.remove("__pycache__/darktitlebar.cpython-311.pyc")
    os.rmdir("__pycache__")
    open = a
    open = os.path.realpath(open)
    os.startfile(open)
    exit()


def change_i():  # button img change
    if submitbtn.image == buttonimg:


        submitbtn.config(image=buttonimg2)
        submitbtn.image = buttonimg2
        window.after(5, window.update())
        submitbtn.config(image=buttonimg)
        submitbtn.image = buttonimg

    elif submitbtn.image == buttonimg3:


        submitbtn.config(image=buttonimg)
        submitbtn.image = buttonimg
        window.after(10, window.update())
        submitbtn.config(image=buttonimg3)
        submitbtn.image = buttonimg3
def change_theme():  # theme change
    if buttn.image == buttnimg3:


        buttn.config(bg='#111111', image=buttnimg4, activebackground='#111111')
        window.config(bg="#111111")
        submitbtn.image = buttonimg
        e.config(bg="#151515", fg="white", insertbackground='white')
        submitbtn.config(bg="#111111", image=buttonimg, activebackground="#111111")
        w.config(bg="#111111", fg="white")
        w1.config(bg="#111111", fg="white")
        buttn.image = buttnimg4
        dark_title_bar(window)
        window.geometry(str(window.winfo_width() + 1) + "x" + str(window.winfo_height() + 1))
        window.geometry(str(window.winfo_width() - 1) + "x" + str(window.winfo_height() - 1))
    else:


        buttn.config(bg='white', image=buttnimg3, activebackground='white')
        window.config(bg="white")
        submitbtn.image = buttonimg3
        e.config(bg="#fafafa", fg="#111111", insertbackground='#111111')
        submitbtn.config(bg="white", image=buttonimg3, activebackground="white")
        w.config(bg="white", fg="#111111")
        w1.config(bg="white", fg="#111111")
        buttn.image = buttnimg3
        light_title_bar(window)
        window.geometry(str(window.winfo_width() + 1) + "x" + str(window.winfo_height() + 1))
        window.geometry(str(window.winfo_width() - 1) + "x" + str(window.winfo_height() - 1))

def funcs(): # combining both change_i and submit func to work together
    change_i()
    submit()

# creating window
window = Tk()
window.eval('tk::PlaceWindow . center')
window.resizable(False, False)
window.geometry('300x200')
window.title('Folder creator')
window.config(bg='white')
p1 = PhotoImage(file='icon.png')
window.iconphoto(False, p1)
window.bind('<Return>', enter)
light_title_bar(window)
window.geometry(str(window.winfo_width() + 1) + "x" + str(window.winfo_height() + 1))
window.geometry(str(window.winfo_width() - 1) + "x" + str(window.winfo_height() - 1))

# text on screen
w1 = Label(window, text='Insert folder name or directory:')
w1.place(x=30, y=50)
w1.config(bg='white', font=('VAG Rounded', 13), fg='#111111')

# 2nd text on screen
w = Label(window, text='')
w.place(y=500, x=4030)
w.pack(side=BOTTOM)
w.config(fg='#111111', font=('VAG Rounded', 13), bg='white')

# submit button
submitbtn = Button(window, text="", command=funcs)
buttonimg = PhotoImage(file="button.png")
buttonimg2 = PhotoImage(file='button2.png')
buttonimg3 = PhotoImage(file='button5.png')
submitbtn.image = buttonimg3
submitbtn.place(relx=0.5, rely=0.5, anchor=CENTER, x=85)
submitbtn.config(bg='white', bd=0, fg='white', font=('VAG Rounded', 13), image=buttonimg3, activebackground='white')


# theme change button
buttn = Button(window, text="", command=change_theme)
buttnimg3 = PhotoImage(file="button3.png")
buttn.image = buttnimg3
buttnimg4 = PhotoImage(file='button4.png')
buttn.place(relx=0.5, rely=0.5, anchor=CENTER, x=133)
buttn.config(bg='white', bd=0, fg='white', font=('VAG Rounded', 13), image=buttnimg3, activebackground='white')

# entry box
e = Entry()
e.place(y=83, x=5)
e.config(font=('Arial', 20), bg='#fafafa', insertbackground='#111111', fg='#111111', bd=0, width=13)
e.focus_force()

window.mainloop()


atexit.register(exittask)