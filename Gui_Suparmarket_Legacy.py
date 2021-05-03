from tkinter import *

mGui = Tk()
mGui.title("SUPERMARKET GO...")

def backhome():
    sec.destroy()
    mGui

def printing():
    data1 = data1_fetch.get()
    data2 = data2_fetch.get()

    if data1 == "Anil Himam" and data2 == "Password":
        mGui.destroy()
        global sec
        sec = Tk()

        submit = Button(sec, text = "Submit", command = backhome)
        submit.pack()

    else:
        print("This dosent work")
    

data1_fetch = StringVar()
data2_fetch = StringVar()

heading = Label(mGui, text = "Welcome to supermarket Go ...", fg = "blue")
heading.grid(row = 0, columnspan = 2)

label_user = Label(mGui, text = "Username:")
label_user.grid(row = 1, column = 0, sticky = E)
entry_user = Entry(mGui, textvariable = data1_fetch)
entry_user.grid(row = 1, column = 1)

label_pass = Label(mGui, text = "Password:")
label_pass.grid(row = 2, column = 0, sticky = E)
entry_pass = Entry(mGui, textvariable = data2_fetch)
entry_pass.grid(row = 2, column = 1)

submit = Button(mGui, text = "Submit", command = printing)
submit.grid(row = 3, columnspan = 2)

