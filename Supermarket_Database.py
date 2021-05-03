''' This is a program aimed at helping with the inventory management of a supermarket.
Designed and Developed By Anil Himam and Amaan Mohamed'''

import mysql.connector #importing mysql connector

mydb = mysql.connector.connect(host="localhost",user="root",passwd="anil@1234") # connecting database
crsr = mydb.cursor()

crsr.execute("CREATE DATABASE IF NOT EXISTS smm") # creating database
crsr.execute("USE smm")
crsr.execute("""CREATE TABLE IF NOT EXISTS super_market_management(Sno int(10) PRIMARY KEY,P_name varchar(50),P_qnt INT,P_catg varchar(30))""") # creating coloumns

def Appending_Content():# function declaration
    
    n=int(input("Enter the number of products you want to add: "))  # adding items
    ctg=["1.Food","2.Electronics","3.Household","4.Toys","5.Stationary"]

    for i in range(n):
        p_num=int(input("Enter the product number"))
        name=input("Product Name: ")
        qnt=int(input("Quantity: "))

        for j in ctg:
            print(j)

        catg=int(input("Enter catgory number: "))
        val=(p_num,name,qnt,ctg[(catg-1)]) # holds the user entered values
        sql="INSERT INTO super_market_management VALUES(%s,%s,%s,%s)"
        crsr.execute(sql,val)

    mydb.commit()
    crsr.execute('SELECT * FROM super_market_management')
    query=crsr.fetchall()
    print("Updated product db")
    for i in query:
        print(i)
        
def Notification():# function declaration

    crsr.execute('SELECT P_name FROM super_market_management WHERE P_qnt<10')
    prd=crsr.fetchall()
    print("The items:",end=" ")

    for i in prd:
      print(i[0],end=" ")

    print("has very less quantity left\n\
        Please buy more of this product soon...\n")             # indication of less quantity of particular products 

Appending_Content()  # function call
Notification()








