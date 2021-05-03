import mysql.connector as sql
import matplotlib.pyplot as pl
from tkinter import *

passwords_database = sql.connect(host = "localhost", user = "root", passwd = "anil@1234", database = "supermarket_passwords")
product_database = sql.connect(host = "localhost", user = "root", passwd = "anil@1234", database = "product_management")

password_cursor = passwords_database.cursor()
product_cursor = product_database.cursor()

#-------------------------------------------------------------------------------------------------------------------------

def statistics():

    sqlFormula = "select * from product_details"
    product_cursor.execute(sqlFormula)

    result = list(product_cursor.fetchall())

    names = []
    values = []

    for i in result:

        names.append(i[1])
        values.append(int(i[2]))

    xval = []

    for i in range(len(names)):
        xval.append(i)

    pl.title("Order Statistics")
    pl.xlabel("Products")
    pl.ylabel("Quantity")
    pl.bar(xval, values, width = 0.6, color = "yellow", label = "Products")
    pl.legend(loc = "upper right")
    pl.xticks(xval, names)
    pl.show()
    

#-------------------------------------------------------------------------------------------------------------------------
statistics()
