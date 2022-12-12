import os
from datetime import date
from tkinter import *
import traceback
import time

with open("log.txt", "w") as log:  # logging an error if it happens
    try:
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
                window.after(2000,window.update())
                exit()
            monthcreate()
            window.after(1000, window.update())
            monthfolcreate()
            w.config(text="Folders Created.")
            window.after(2000, window.update())
            exit()


        # creating window
        window = Tk()
        window.eval('tk::PlaceWindow . center')
        window.resizable(False, False)
        window.geometry('300x200')
        window.title('Folder creator')
        window.config(bg='#111111')

        # text on screen
        w1 = Label(window, text='Insert folder name or directory:')
        w1.place(x=30, y=50)
        w1.config(bg='#111111')
        w1.config(fg='white')
        w1.config(font=('Arial', 13))

        # 2nd text on screen
        w = Label(window, text='')
        w.place(y=500, x=4030)
        w.pack(side=BOTTOM)
        w.config(bg='#111111')
        w.config(fg='white')
        w.config(font=('Arial', 13))

        # submit button
        submit = Button(window, text="Start", command=submit)
        submit.place(y=130, x=120)
        submit.config(bg='#111111')
        submit.config(fg='white')
        submit.config(font=('Arial', 13))

        # entry box
        e = Entry()
        e.place(relx=0.5, rely=0.5, anchor=CENTER)
        e.config(font=('Arial', 20))
        e.config(bg='#111111')
        e.config(fg='white')

        window.mainloop()

    except Exception:
        traceback.print_exc(file=log)
