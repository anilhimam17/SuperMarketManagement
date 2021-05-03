from tkinter import *

def second():
    global second_page
    second_page = Tk()

    Lab = Label(second_page, text = "This is the last page")
    Lab.pack()

    but = Button(second_page, text = "back", command = goto_first_page)
    but.pack()

def first():
    global first_page
    first_page = Tk()

    Lab = Label(first_page, text = "This is the last page")
    Lab.pack()

    secButton = Button(first_page, text = "Go to Second Page",
                       command = goto_second_page)
    secButton.pack()

def second_destroy():
    second_page.destroy()

def first_destroy():
    first_page.destroy()

def goto_second_page():
    first_page.destroy()
    second()

def goto_first_page():
    second_page.destroy()
    first()

first()





    
