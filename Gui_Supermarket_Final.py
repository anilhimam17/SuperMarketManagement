import mysql.connector as sql
import matplotlib.pyplot as m
from tkinter import *
from tkinter import messagebox
from random import randint

passwords_database = sql.connect(host="localhost", user="root", passwd="anil$1234", database="supermarket_passwords")
product_database = sql.connect(host="localhost", user="root", passwd="anil$1234", database="supermarket_products")

password_cursor = passwords_database.cursor()
product_cursor = product_database.cursor()

    
# -------------------------------------------------------------------------------------------------------------------------


def ser_processing():

    id_get = int(ser_id_box.get())
    name_get = '"' + str(ser_name_box.get()) + '"'

    sqlformula = "select * from Product_Details where Product_ID = {} and Product_Name = {}".format(id_get, name_get)
    #print(sqlformula)

    product_cursor.execute(sqlformula)

    result = product_cursor.fetchall()
    #print(result)

    if result != []:
        messagebox.showinfo("Product Found", "\nProduct ID: {} \n\nProduct Name: {} \n\nProduct Description: {} \n\nQuantity: {} \n\nPrice: {}".format(result[0][0], result[0][1],
                                                                                                                                                       result[0][2], result[0][3], result[0][4]))
    elif result == []:
        messagebox.showinfo("Alert", "Product not found please enter the details again \n\nElse the product dosent exist please make a new entry")
        


def search_product():

    global ser_prod_page

    ser_prod_page = Tk()

    global ser_id_box
    global ser_name_box

    ser_prod_page.title("Deleting Products")
    ser_prod_page.geometry("460x460+450+200")
    ser_prod_page.configure(background="cyan")

    heading = Label(ser_prod_page, text="Searching Products", fg="blue", bg="cyan", font="futura 50", height=1)
    heading.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="NEWS")

    blanklabel1 = Label(ser_prod_page, text="", bg="cyan", height=2)
    blanklabel1.grid(row=1, column=0, columnspan=4)

    id_label = Label(ser_prod_page, text="Product ID:", fg="blue", bg="cyan", font="futura 20", height=1)
    id_label.grid(row=2, column=1)
    ser_id_box = Entry(ser_prod_page, borderwidth=10)
    ser_id_box.grid(row=2, column=2)

    blanklabel2 = Label(ser_prod_page, text="", bg="cyan", height=2)
    blanklabel2.grid(row=3, column=0, columnspan=4)

    name_label = Label(ser_prod_page, text="Product Name:", fg="blue", bg="cyan", font="futura 20", height=1)
    name_label.grid(row=4, column=1)
    ser_name_box = Entry(ser_prod_page, borderwidth=10)
    ser_name_box.grid(row=4, column=2)

    blanklabel3 = Label(ser_prod_page, text="", bg="cyan", height=2)
    blanklabel3.grid(row=5, column=0, columnspan=4)

    del_button = Button(ser_prod_page, text="Search Product", fg="blue", font="futura 20", width=20, height=2,
                        command=ser_processing)
    del_button.grid(row=6, column=1, columnspan=2)

    blanklabel4 = Label(ser_prod_page, text="", bg="cyan", height=1)
    blanklabel4.grid(row=7, column=0, columnspan=4)

    del_to_home_button = Button(ser_prod_page, text="Back To Homepage", fg="blue", font="futura 20", width=20, height=2, command = ser_prod_to_home)
    del_to_home_button.grid(row=8, column=1, columnspan=2)


# -------------------------------------------------------------------------------------------------------------------------


def show_record():

    global showrecord

    showrecord = Tk()
    showrecord.title("User Records")
    showrecord.geometry("1100x700+190+100")
    showrecord.config(bg="cyan")

    heading = Label(showrecord, text="User Records History", fg="blue", bg="cyan", font="futura 50")
    heading.grid(row=0, column=0, columnspan=6, ipadx=5, ipady=5)

    blanklabel1 = Label(showrecord, text="", bg="cyan")
    blanklabel1.grid(row=1, column=0, columnspan=5)

    name = Label(showrecord, text="User Name", fg="blue", bg="cyan", font="futura 25", height=2, width=20)
    name.grid(row=2, column=1)

    password = Label(showrecord, text="User Password", fg="blue", bg="cyan", font="futura 25", height=2, width=20)
    password.grid(row=2, column=2)

    email = Label(showrecord, text="User Email - ID", fg="blue", bg="cyan", font="futura 25", height=2, width=20)
    email.grid(row=2, column=3)

    blanklabel2 = Label(showrecord, text="", bg="cyan")
    blanklabel2.grid(row=3, column=0, columnspan=5)

    sqlformula = "select * from user_profiles"
    password_cursor.execute(sqlformula)

    profiles = password_cursor.fetchall()

    but_val = 4
    
    for i in range(len(profiles)):

        nm_user = Label(showrecord, text = profiles[i][0], fg = "blue", bg = "cyan", font = "futura 25", height = 2, width = 20)
        nm_user.grid(row = but_val, column = 1)

        password_user = Label(showrecord, text=profiles[i][1], fg="blue", bg="cyan", font="futura 25", height=2, width=20)
        password_user.grid(row=but_val, column=2)

        email_user = Label(showrecord, text=profiles[i][2], fg="blue", bg="cyan", font="futura 25", height=2, width=20)
        email_user.grid(row=but_val, column=3)

        blanklabel2 = Label(showrecord, text="", bg="cyan")
        blanklabel2.grid(row=but_val + 1, column=0, columnspan=5)

        but_val += 1


    buttonval = but_val + 2

    back_setpage = Button(showrecord, text="Back to Settings Page", font="futura 20", fg="blue", width=30, height=2, command=showrec_to_setpage)
    back_setpage.grid(row=buttonval, column = 2, ipadx=5, ipady=5, sticky="NEWS")


def settings():

    global settingpage

    settingpage = Tk()
    settingpage.title("Billing Page")
    settingpage.geometry("550x500+400+200")
    settingpage.config(bg="cyan")

    heading = Label(settingpage, text="Settings Page", fg="blue", font="futura 50", bg = "cyan", width=20, height = 1)
    heading.pack()

    blanklabel1 = Label(settingpage, text="", bg="cyan", height = 1)
    blanklabel1.pack()

    subheading = Label(settingpage, text="Here you can view the user \ndetails of the software", fg="blue", bg = "cyan", font="futura 35", width=50, height = 2)
    subheading.pack()

    blanklabel2 = Label(settingpage, text="", bg="cyan", height = 2)
    blanklabel2.pack()

    show_rec_button = Button(settingpage, text="Show Records", fg="blue", font="futura 20", width=20, height = 2, command = goto_showrecord)
    show_rec_button.pack()

    blanklabel3 = Label(settingpage, text="", bg="cyan", height = 2)
    blanklabel3.pack()

    set_to_home_button = Button(settingpage, text="Back To Homepage", fg="blue", font="futura 20", width=20, height = 2, command=setting_to_home)
    set_to_home_button.pack()


# -------------------------------------------------------------------------------------------------------------------------


def deleting():

    id_get = int(id_raw.get())

    sqlFormula = "delete from Product_Details where Product_ID like {}".format(id_get)

    product_cursor.execute(sqlFormula)

    product_database.commit()


def del_processing():

    id_get = int(id_raw.get())

    sqlFormula = "select Product_ID from Product_Details where Product_ID like {}".format(id_get)
    product_cursor.execute(sqlFormula)

    result = product_cursor.fetchall()

    if result:
        answer = messagebox.askquestion("Alert", "Do you really want to delete this product!")

        if answer == "yes":
            deleting()

        else:
            pass

    else:
        messagebox.showinfo("Alert", "The PRODUCT ID mentioned isnt assigned to\n any product in the database")


def delete_product():

    global del_prod_page

    del_prod_page = Tk()

    global id_raw
    global name_raw
    id_raw = StringVar()
    name_raw = StringVar()

    del_prod_page.title("Deleting Products")
    del_prod_page.geometry("460x460+450+200")
    del_prod_page.configure(background="cyan")

    heading = Label(del_prod_page, text="Deleting Products", fg="blue", bg="cyan", font="futura 50", height=1)
    heading.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="NEWS")

    blanklabel1 = Label(del_prod_page, text="", bg="cyan", height=2)
    blanklabel1.grid(row=1, column=0, columnspan=4)

    id_label = Label(del_prod_page, text="Product ID", fg="blue", bg="cyan", font="futura 20", height=1)
    id_label.grid(row=2, column=1)
    id_box = Entry(del_prod_page, borderwidth=10, textvariable=id_raw)
    id_box.grid(row=2, column=2)

    blanklabel2 = Label(del_prod_page, text="", bg="cyan", height=2)
    blanklabel2.grid(row=3, column=0, columnspan=4)

    name_label = Label(del_prod_page, text="Product Name", fg="blue", bg="cyan", font="futura 20", height=1)
    name_label.grid(row=4, column=1)
    name_box = Entry(del_prod_page, borderwidth=10, textvariable=name_raw)
    name_box.grid(row=4, column=2)

    blanklabel3 = Label(del_prod_page, text="", bg="cyan", height=2)
    blanklabel3.grid(row=5, column=0, columnspan=4)

    del_button = Button(del_prod_page, text="Delete Product", fg="blue", font="futura 20", width=20, height=2,
                        command=del_processing)
    del_button.grid(row=6, column=1, columnspan=2)

    blanklabel4 = Label(del_prod_page, text="", bg="cyan", height=1)
    blanklabel4.grid(row=7, column=0, columnspan=4)

    del_to_home_button = Button(del_prod_page, text="Back To Homepage", fg="blue", font="futura 20", width=20, height=2,
                                command=delete_product_to_home)
    del_to_home_button.grid(row=8, column=1, columnspan=2)


# -------------------------------------------------------------------------------------------------------------------------


def statistics():

    sqlFormula = "select * from Product_Details"
    product_cursor.execute(sqlFormula)

    result = list(product_cursor.fetchall())

    names = []
    values = []

    for i in result:
        names.append(i[1])
        values.append(int(i[3]))

    xval = []

    for i in range(len(names)):
        xval.append(i)

    m.title("Order Statistics")
    m.xlabel("Products")
    m.ylabel("Quantity")
    m.bar(xval, values, width=0.6, color="cyan", label="Products")
    m.legend(loc="upper right")
    m.xticks(xval, names)
    m.show()

    pass


# -------------------------------------------------------------------------------------------------------------------------


def notification():

    global notifypage

    notifypage = Tk()

    notifypage.title("Quantity Management")
    notifypage.geometry("1260x700+100+100")
    notifypage.configure(background="cyan")

    sqlFormula = "SELECT * FROM Product_Details WHERE Quantity < 50"

    product_cursor.execute(sqlFormula)
    result = product_cursor.fetchall()

    '''Here also we print data dyanamically using a for loop'''

    heading = Label(notifypage, text="Welcome to Product Quantity Notifcation", font="futura 30", fg="blue", bg="cyan",
                    height=2)
    heading.grid(row=0, column=0, columnspan=6, sticky="NEWS")

    blanklabel1 = Label(notifypage, text="       ", bg="cyan")
    blanklabel1.grid(row=1, column=0, columnspan=5)

    if len(result) == None:

        message = Label(notifypage, text="You have no products to be ordered immediately",
                        font="futura 25", fg="blue", bg="cyan")
        message.grid(row=2, column=0, columnspan=5)

    else:

        ids = Label(notifypage, text="Product ID", fg="blue", bg="cyan", font="futura 25", height=2, width=15)
        ids.grid(row=2, column=1)

        name = Label(notifypage, text="Product Name", fg="blue", bg="cyan", font="futura 25", height=2, width=15)
        name.grid(row=2, column=2)

        description = Label(notifypage, text="Product Desc", fg="blue", bg="cyan", font="futura 25", height=2, width=15)
        description.grid(row=2, column=3)

        quantity = Label(notifypage, text="Product Quantity", fg="blue", bg="cyan", font="futura 25", height=2,
                         width=15)
        quantity.grid(row=2, column=4)

        price = Label(notifypage, text="Product Price", fg="blue", bg="cyan", font="futura 25", height=2, width=15)
        price.grid(row=2, column=5)

        blanklabel2 = Label(notifypage, text="", bg="cyan")
        blanklabel2.grid(row=3, column=0, columnspan=5)

        pos = 4

        for i in result:
            product_id = Label(notifypage, text=i[0], fg="white", bg="cyan", font="futura 20")
            product_id.grid(row=pos, column=1)

            product_name = Label(notifypage, text=i[1], fg="white", bg="cyan", font="futura 20")
            product_name.grid(row=pos, column=2)

            product_desc = Label(notifypage, text=i[2], fg="blue", bg="cyan", font="futura 20")
            product_desc.grid(row=pos, column=3)

            product_quantity = Label(notifypage, text=i[3], fg="white", bg="cyan", font="futura 20")
            product_quantity.grid(row=pos, column=3)

            product_price = Label(notifypage, text=i[4], fg="white", bg="cyan", font="futura 20")
            product_price.grid(row=pos, column=4)

            blanklabel3 = Label(notifypage, text="", bg="cyan")
            blanklabel3.grid(row=pos + 1, column=0, columnspan=5)

            pos += 1

        buttonval = pos + 2

        back_home = Button(notifypage, text="Back to Home Page", font="futura 20", fg="blue", width=30, height=2,
                           command=notify_to_home)
        back_home.grid(row=buttonval, column=1, columnspan=2, ipadx=5, ipady=5, sticky="NEWS")


# -------------------------------------------------------------------------------------------------------------------------


def show_products():

    global productspage

    productspage = Tk()

    productspage.title("Product Window")
    productspage.geometry("1260x700+100+100")
    productspage.configure(background="cyan")

    sqlFormula = "SELECT * FROM Product_Details"

    product_cursor.execute(sqlFormula)
    products = product_cursor.fetchall()

    ''' Here we need to execute a for loop for a dynamic variable to place all the information in a tabular format'''

    heading = Label(productspage, text="Present Inventory", fg="blue", bg="cyan", font="futura 50")
    heading.grid(row=0, column=0, columnspan=6, ipadx=5, ipady=5)

    blanklabel1 = Label(productspage, text="", bg="cyan")
    blanklabel1.grid(row=1, column=0, columnspan=5)

    ids = Label(productspage, text="Product ID", fg="blue", bg="cyan", font="futura 25", height=2, width=15)
    ids.grid(row=2, column=1)

    name = Label(productspage, text="Product Name", fg="blue", bg="cyan", font="futura 25", height=2, width=15)
    name.grid(row=2, column=2)

    description = Label(productspage, text="Product Desc", fg="blue", bg="cyan", font="futura 25", height=2, width=15)
    description.grid(row=2, column=3)

    quantity = Label(productspage, text="Product Quantity", fg="blue", bg="cyan", font="futura 25", height=2, width=15)
    quantity.grid(row=2, column=4)

    price = Label(productspage, text="Product Price", fg="blue", bg="cyan", font="futura 25", height=2, width=15)
    price.grid(row=2, column=5)

    blanklabel2 = Label(productspage, text="", bg="cyan")
    blanklabel2.grid(row=3, column=0, columnspan=5)

    pos = 4

    for i in products:
        product_id = Label(productspage, text=i[0], fg="blue", bg="cyan", font="futura 20")
        product_id.grid(row=pos, column=1)

        product_name = Label(productspage, text=i[1], fg="blue", bg="cyan", font="futura 20")
        product_name.grid(row=pos, column=2)

        product_desc = Label(productspage, text=i[2], fg="blue", bg="cyan", font="futura 20")
        product_desc.grid(row=pos, column=3)

        product_quantity = Label(productspage, text=i[3], fg="blue", bg="cyan", font="futura 20")
        product_quantity.grid(row=pos, column=4)

        product_price = Label(productspage, text=i[4], fg="blue", bg="cyan", font="futura 20")
        product_price.grid(row=pos, column=5)

        blanklabel3 = Label(productspage, text="", bg="cyan")
        blanklabel3.grid(row=pos + 1, column=0, columnspan=5)

        pos += 1

    buttonval = pos + 2

    back_home = Button(productspage, text="Back to Home Page", font="futura 20", fg="blue", width=30, height=2,
                       command=showproducts_to_home)
    back_home.grid(row=buttonval, column=1, columnspan=2, ipadx=5, ipady=5, sticky="NEWS")


# -------------------------------------------------------------------------------------------------------------------------


def append_db():

    product_name = product_name_raw.get()
    product_desc = product_desc_raw.get()
    product_quantity = product_quantity_raw.get()
    product_price = product_price_raw.get()

    data = [id_val, product_name.strip(), product_desc.strip(), product_quantity.strip(), product_price.strip()]
    product_data = tuple(data)

    sqlFormula = "select Product_ID, Product_Name from Product_Details"
    product_cursor.execute(sqlFormula)

    results = product_cursor.fetchall()

    for i, j in results:

        if i == id_val or j == product_name:

            messagebox.showinfo("ALERT !",
                                "There already exists a product with the given details. Please enter a unique name for the product")
            break

        else:
            pass

    else:

        sqlFormula = "INSERT INTO Product_Details (Product_ID, Product_Name, Product_Description, Quantity, Price) VALUES (%s, %s, %s, %s, %s)"

        product_cursor.execute(sqlFormula, product_data)

        product_database.commit()


def add_new_products():

    global appendpage

    appendpage = Tk()

    appendpage.title("New Products")
    appendpage.geometry("600x720+350+100")
    appendpage.configure(background="cyan")

    heading = Label(appendpage, text="ADD NEW PRODUCTS", fg="blue", bg="cyan", font="futura 50", height=1)
    heading.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky="NEWS")

    blanklabel1 = Label(appendpage, text="", bg="cyan", height=2)
    blanklabel1.grid(row=1, column=0, columnspan=4)

    global product_name_raw
    global product_quantity_raw
    global product_price_raw
    global product_desc_raw

    product_name_raw = StringVar()
    product_quantity_raw = StringVar()
    product_price_raw = StringVar()
    product_desc_raw = StringVar()

    sqlFormula = "select Product_ID from Product_Details"

    product_cursor.execute(sqlFormula)
    ids = product_cursor.fetchall()

    global id_val

    for i in ids:

        id_val = randint(1000000000000, 9999999999999)

        if id_val != i:
            break

    product_id_label = Label(appendpage, text="Product ID:", fg="blue", bg="cyan", font="futura 20")
    product_id_label.grid(row=2, column=0, sticky=E)
    product_id_val_label = Label(appendpage, text=id_val, fg="blue", bg="cyan", font="futura 20")
    product_id_val_label.grid(row=2, column=1)

    blanklabel2 = Label(appendpage, text="", bg="cyan", height=2)
    blanklabel2.grid(row=3, column=1, columnspan=4)

    product_name_label = Label(appendpage, text="Product Name:", fg="blue", bg="cyan", font="futura 20")
    product_name_label.grid(row=4, column=0, sticky=E)
    product_name_box = Entry(appendpage, borderwidth=10, textvariable=product_name_raw)
    product_name_box.grid(row=4, column=1)

    blanklabel3 = Label(appendpage, text="", bg="cyan", height=2)
    blanklabel3.grid(row=5, column=1, columnspan=4)

    product_desc_label = Label(appendpage, text="Product Description:", fg="blue", bg="cyan", font="futura 20")
    product_desc_label.grid(row=6, column=0, sticky=E)
    product_desc_box = Entry(appendpage, borderwidth=10, textvariable=product_desc_raw)
    product_desc_box.grid(row=6, column=1)

    blanklabel4 = Label(appendpage, text="", bg="cyan", height=2)
    blanklabel4.grid(row=7, column=1, columnspan=4)

    product_quantity_label = Label(appendpage, text="Product Quantity:", fg="blue", bg="cyan", font="futura 20")
    product_quantity_label.grid(row=8, column=0, sticky=E)
    product_quantity_box = Entry(appendpage, borderwidth=10, textvariable=product_quantity_raw)
    product_quantity_box.grid(row=8, column=1)

    blanklabel5 = Label(appendpage, text="", bg="cyan", height=2)
    blanklabel5.grid(row=9, column=1, columnspan=4)

    product_price_label = Label(appendpage, text="Product Price:", fg="blue", bg="cyan", font="futura 20")
    product_price_label.grid(row=10, column=0, sticky=E)
    product_price_box = Entry(appendpage, borderwidth=10, textvariable=product_price_raw)
    product_price_box.grid(row=10, column=1)

    blanklabel6 = Label(appendpage, text="", bg="cyan", height=2)
    blanklabel6.grid(row=11, column=0, columnspan=4)

    add_product_button = Button(appendpage, text="ADD PRODUCT", font="futura 20", fg="blue", width=20, height=2,
                                command=append_db)
    add_product_button.grid(row=12, column=0, columnspan=2)

    blanklabel7 = Label(appendpage, text="       ", bg="cyan")
    blanklabel7.grid(row=13, column=0, padx=5, pady=5)

    back_home = Button(appendpage, text="Back to Home Page", font="futura 20", fg="blue", width=20, height=2,
                       command=appendpage_to_home)
    back_home.grid(row=14, column=0, columnspan=2)


# -------------------------------------------------------------------------------------------------------------------------


def quit_home():

    answer = messagebox.askquestion("Alert", "Do you really want to quit the application!")

    if answer == "yes":
        home_destroy()

    else:
        pass


def home():

    global homepage

    homepage = Tk()

    homepage.title("Home Window")
    homepage.geometry("750x800+350+50")
    homepage.configure(background="cyan")
    head = "Welcome Back: " + username

    heading = Label(homepage, text=head, font="futura 50", bg="cyan", fg="blue")
    heading.grid(row=0, column=0, columnspan=3, padx=5, pady=5, sticky=E)

    blanklabel1 = Label(homepage, text="       ", bg="cyan", height=2)
    blanklabel1.grid(row=1, column=0, padx=5, pady=5, sticky=E)

    append_button = Button(homepage, text="Add New Products", font="futura 25", fg="blue", width=20, height=2, command=goto_appendpage)
    append_button.grid(row=2, column=1, padx=5, pady=5, sticky=E)

    showButton = Button(homepage, text="Show Products", font="futura 25", fg="blue", width=20, height=2, command=goto_productspage)
    showButton.grid(row=2, column=2, padx=5, pady=5, sticky=E)

    blanklabel2 = Label(homepage, text="       ", bg="cyan", height=2)
    blanklabel2.grid(row=3, column=0, padx=5, pady=5, sticky=E)

    stats_button = Button(homepage, text="Product Sales", font="futura 25", fg="blue", width=20, height=2, command=statistics)
    stats_button.grid(row=4, column=1, padx=5, pady=5, sticky=E)

    notif_button = Button(homepage, text="Notification", font="futura 25", fg="blue", width=20, height=2, command=goto_notifypage)
    notif_button.grid(row=4, column=2, padx=5, pady=5, sticky=E)

    blanklabel3 = Label(homepage, text="       ", bg="cyan", height=2)
    blanklabel3.grid(row=5, column=0, padx=5, pady=5, sticky=E)

    set_button = Button(homepage, text="Setting", font="futura 25", fg="blue", width=20, height=2, command=goto_settingpage)
    set_button.grid(row=6, column=1, padx=5, pady=5, sticky=E)

    del_prod_button = Button(homepage, text="Delete Product", font="futura 25", fg="blue", width=20, height=2, command=goto_deleteproduct)
    del_prod_button.grid(row=6, column=2, padx=5, pady=5, sticky=E)

    blanklabel4 = Label(homepage, text="       ", bg="cyan", height=2)
    blanklabel4.grid(row=7, column=0, padx=5, pady=5, sticky=E)

    search_button = Button(homepage, text = "Search Product", font = "futura 25", fg = "blue", width = 20, height = 2, command = goto_ser_prod)
    search_button.grid(row = 8, column = 1, padx=5, pady=5, sticky=E)

    back_login = Button(homepage, text="Back to Login Page", font="futura 25", fg="blue", width=20, height=2, command=homepage_to_login)
    back_login.grid(row=8, column=2, padx=5, pady=5, sticky=E)

    blanklabel5 = Label(homepage, text="       ", bg="cyan", height=2)
    blanklabel5.grid(row=9, column=0, padx=5, pady=5, sticky=E)

    quit_app = Button(homepage, text="Quit Application", font="futura 25", fg="blue", width=20, height=2, command=quit_home)
    quit_app.grid(row=10, column=0, columnspan=2, padx=5, pady=5, sticky=E)


# -------------------------------------------------------------------------------------------------------------------------


def processing():

    global username

    username = user_fetch.get()
    password = pass_fetch.get()

    sqlFormula = "SELECT Username, Password FROM user_profiles"
    password_cursor.execute(sqlFormula)

    profiles = password_cursor.fetchall()

    data = [username.strip(), password.strip()]
    profile = tuple(data)

    for i in profiles:

        if i == profile:
            goto_homepage()
            break

        else:
            pass

    else:
        messagebox.showinfo("Invalid", "The entered credentials are invalid \n Please check them or Register")
        pass


# -------------------------------------------------------------------------------------------------------------------------


def quit_register():

    answer = messagebox.askquestion("Alert", "Do you really want to quit the application!")

    if answer == "yes":
        register_destroy()

    else:
        pass


def register_data():

    datafetch_username = data_username.get()
    datafetch_password = data_password.get()
    datafetch_email = data_email.get()

    data = [datafetch_username.strip(), datafetch_password.strip(), datafetch_email.strip()]
    profile = tuple(data)

    entryFormula = "INSERT INTO user_profiles (Username, Password, Email) VALUES (%s, %s, %s)"

    password_cursor.execute(entryFormula, profile)

    passwords_database.commit()

    register_destroy()
    register()


def register():

    global registerpage
    global data_username
    global data_password
    global data_email

    registerpage = Tk()

    registerpage.title("Register Page")
    registerpage.geometry("700x500+350+200")
    registerpage.configure(background="cyan")

    heading = Label(registerpage, text="Welcome to the Register Page", fg="blue", bg="cyan", font="futura 50")
    heading.grid(row=1, column=1, columnspan=2)

    blanklabel1 = Label(registerpage, text="", bg="cyan")
    blanklabel1.grid(row=2, columnspan=2)

    user_label = Label(registerpage, text="Username:", fg="blue", bg="cyan", font="futura 20")
    user_label.grid(row=3, column=1, sticky=E)

    data_username = StringVar()

    user_box = Entry(registerpage, borderwidth=10, textvariable=data_username)
    user_box.grid(row=3, column=2)

    blanklabel2 = Label(registerpage, text="", bg="cyan")
    blanklabel2.grid(row=4, columnspan=2)

    password_label = Label(registerpage, text="Password:", fg="blue", bg="cyan", font="futura 20")
    password_label.grid(row=5, column=1, sticky=E)

    data_password = StringVar()

    password_box = Entry(registerpage, textvariable=data_password, borderwidth=10)
    password_box.grid(row=5, column=2)

    blanklabel3 = Label(registerpage, text="", bg="cyan")
    blanklabel3.grid(row=6, columnspan=2)

    email_label = Label(registerpage, text="Email:", fg="blue", bg="cyan", font="futura 20")
    email_label.grid(row=7, column=1, sticky=E)

    data_email = StringVar()

    email_box = Entry(registerpage, textvariable=data_email, borderwidth=10)
    email_box.grid(row=7, column=2)

    blanklabel5 = Label(registerpage, text="", bg="cyan")
    blanklabel5.grid(row=8, columnspan=2)

    submit = Button(registerpage, text="Submit", font="futura 20", fg="blue", borderwidth=7, width=20,
                    command=register_data)
    submit.grid(row=9, column=1, columnspan=2, ipadx=5, ipady=5)

    blanklabel6 = Label(registerpage, text="", bg="cyan")
    blanklabel6.grid(row=10, column=0, columnspan=2)

    back_login = Button(registerpage, text="Back To Loginpage", font="futura 20", fg="blue", borderwidth=7, width=20,
                        command=register_to_login)
    back_login.grid(row=11, column=1, columnspan=2, ipadx=5, ipady=5)

    blanklabel7 = Label(registerpage, text="", bg="cyan")
    blanklabel7.grid(row=12, column=0, columnspan=2)

    quit_app = Button(registerpage, text="Quit Application", font="futura 20", fg="blue", borderwidth=7, width=20,
                      command=quit_register)
    quit_app.grid(row=13, column=1, columnspan=2, ipadx=5, ipady=5)


# -------------------------------------------------------------------------------------------------------------------------


def quit_login():

    answer = messagebox.askquestion("Alert", "Do you really want to quit the application!")

    if answer == "yes":
        login_destroy()

    else:
        pass


def login_page():

    # First Window
    global loginpage
    loginpage = Tk()
    loginpage.title("SUPERMARKET GO...")
    loginpage.geometry("700x450+350+250")
    loginpage.configure(background="cyan")

    # Entry Data Variables
    global user_fetch
    global pass_fetch
    user_fetch = StringVar()
    pass_fetch = StringVar()

    # Login Page Widgets
    heading = Label(loginpage, text="Welcome to supermarket Go", font="futura 50", fg="blue", bg="cyan")
    heading.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky="NEWS")

    blanklabel1 = Label(loginpage, text="       ", bg="cyan")
    blanklabel1.grid(row=1, column=0, columnspan=2)

    label_user = Label(loginpage, text="Username:", font="futura 20", fg="blue", bg="cyan")
    label_user.grid(row=2, column=0, sticky=E)

    entry_user = Entry(loginpage, textvariable=user_fetch, borderwidth=10)
    entry_user.grid(row=2, column=1, ipady = 3)

    blanklabel2 = Label(loginpage, text="", bg="cyan")
    blanklabel2.grid(row=3, column=0, columnspan=2)

    label_pass = Label(loginpage, text="Password:", font="futura 20", fg="blue", bg="cyan")
    label_pass.grid(row=4, column=0, sticky=E)

    entry_pass = Entry(loginpage, textvariable=pass_fetch, borderwidth=10, show="*")
    entry_pass.grid(row=4, column=1, ipady = 3)

    blanklabel3 = Label(loginpage, text="", bg="cyan")
    blanklabel3.grid(row=5, column=0, columnspan=2)

    submit = Button(loginpage, text="Login", font="futura 20", fg="blue", borderwidth=10, width=20, command=processing)
    submit.grid(row=6, column=0, columnspan=2, ipadx=5, ipady=5)

    blanklabel4 = Label(loginpage, text="", bg="cyan")
    blanklabel4.grid(row=7, column=0, columnspan=2)

    reg = Button(loginpage, text="Register", font="futura 20", fg="blue", borderwidth=7, width=20,
                 command=goto_registerpage)
    reg.grid(row=8, column=0, columnspan=2, ipadx=5, ipady=5)

    blanklabel5 = Label(loginpage, text="", bg="cyan")
    blanklabel5.grid(row=9, column=0, columnspan=2)

    quit_app = Button(loginpage, text="Quit Application", font="futura 20", fg="blue", borderwidth=7, width=20,
                      command=quit_login)
    quit_app.grid(row=10, column=0, columnspan=2, ipadx=5, ipady=5)


# -----------------------------------------------------------------------------------------------------------------------

# Mapping all the windows together.
def ser_prod_destroy():
    ser_prod_page.destroy()

def del_rec_destroy():
    del_rec_page.destroy()

def rec_destroy():
    showrecord.destroy()

def set_destroy():
    settingpage.destroy()


def del_prod_destroy():
    del_prod_page.destroy()


def notify_destroy():
    notifypage.destroy()


def products_page_destroy():
    productspage.destroy()


def append_destroy():
    appendpage.destroy()


def home_destroy():
    homepage.destroy()


def register_destroy():
    registerpage.destroy()


def login_destroy():
    loginpage.destroy()


# -----------------------------------------------------------------------------------------------------------------------  

def goto_ser_prod():
    home_destroy()
    search_product()

def goto_del_record():
    set_destroy()
    delete_record()

def goto_showrecord():
    set_destroy()
    show_record()

def goto_settingpage():
    home_destroy()
    settings()


def goto_deleteproduct():
    home_destroy()
    delete_product()


def goto_notifypage():
    home_destroy()
    notification()


def goto_productspage():
    home_destroy()
    show_products()


def goto_appendpage():
    home_destroy()
    add_new_products()


def goto_homepage():
    login_destroy()
    home()


def goto_registerpage():
    login_destroy()
    register()


# -----------------------------------------------------------------------------------------------------------------------
def ser_prod_to_home():
    ser_prod_destroy()
    home()

def del_rec_to_setpage():
    del_rec_destroy()
    settings()

def showrec_to_setpage():
    rec_destroy()
    settings()

def setting_to_home():
    set_destroy()
    home()


def delete_product_to_home():
    del_prod_destroy()
    home()


def notify_to_home():
    notify_destroy()
    home()


def showproducts_to_home():
    products_page_destroy()
    home()


def appendpage_to_home():
    append_destroy()
    home()


def homepage_to_login():
    home_destroy()
    login_page()


def register_to_login():
    register_destroy()
    login_page()


# -----------------------------------------------------------------------------------------------------------------------

login_page()
