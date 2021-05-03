from tkinter import *

def search():

    pid = ser_prod_id.get()
    pname = ser_prod_name.get()

    print(pid, pname)

    '''sqlformula = "select * from Product_Details where Product_ID = %s and Product_Name = %s".format(pid, pname)
    print(sqlformula)

    product_cursor.execute(sqlformula)

    if product_cursor:
        string = "Product ID: " + product_cursor[0][0] + "\nProduct Name: ", + product_cursor[0][1] 
        messagebox.showinfo("Product Found", string)

    else:
        messagebox.showinfo("Alert", "Product not Found")'''

def search_product():

    global ser_prod_id
    global ser_prod_name

    search_page = Tk()
    search_page.title("Search Products")
    search_page.geometry("500x500+200+200")
    search_page.config(bg="cyan")

    ser_prod_id = StringVar()
    ser_prod_name = StringVar()

    heading = Label(search_page, text="Search Records", fg="blue", bg="cyan", font="futura 50")
    heading.grid(row=0, column=0, columnspan=6, ipadx=5, ipady=5)

    blanklabel1 = Label(search_page, text="", bg="cyan")
    blanklabel1.grid(row=1, column=0, columnspan=5)

    id_label = Label(search_page, text = "Product ID:", fg = "blue", bg = "cyan", font = "futura 20")
    id_label.grid(row = 2, column = 1)
    ser_id_box = Entry(search_page, textvariable = ser_prod_id, borderwidth = 7)
    ser_id_box.grid(row = 2, column = 2)

    blanklabel2 = Label(search_page, text="", bg="cyan")
    blanklabel2.grid(row=3, column=0, columnspan=5)

    id_label = Label(search_page, text = "Product Name:", fg = "blue", bg = "cyan", font = "futura 20")
    id_label.grid(row = 4, column = 1)
    ser_id_box = Entry(search_page, textvariable = ser_prod_name, borderwidth = 7)
    ser_id_box.grid(row = 4, column = 2)

    blanklabel3 = Label(search_page, text="", bg="cyan")
    blanklabel3.grid(row=5, column=0, columnspan=5)

    submit_button = Button(search_page, text = "Submit", font = "futura 20", width = 20, fg = "blue", command = search)
    submit_button.grid(row = 6, column = 1, columnspan = 2)
