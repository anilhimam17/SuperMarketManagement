''' This is a program aimed on helping with the inventory management of a supermarket
Designed and Developed By Anil Himam and Amaan'''

'''These are the global variables present in the program'''

import matplotlib.pyplot as pl
import tkinter as tk


food = { "Apple" : 100, "Lays Spanish Tomato Tango" : 20,
        "Dairy Milk Oreo" : 50, "Coca - cola" : 40}
    
stationary = {"Parker Pens" : 20, "Apsara Back-To-School-Kit" : 100,
              "Staedtler Stationary" : 60, "Charts" : 1000, "Classmate Note Books" : 1000}
    
toys = {"Nerf Blaster" : 100, "BeyBlades" : 300,
        "Board Games" : 100, "RC Toys" : 50, "Barbie Dolls" : 100}

house_hold = {"Detergents" : 200, "Mr. Muscle" : 200,
              "Broom Stick - Mop Stick" : 1000, "Shampoo" : 100, "Scrubbers" : 100}
    
electronics = {"One Plus 7 Pro" : 1000, "Samsung QHD +" : 1000,
               "Devialt Phantom" : 100, "Godrej Washing Machines" : 100}


'''This is the log file responsible for maintaining the main product quantity information of the store'''
inventory_file = open("inventory.txt", "a")



#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
def Appending_Content():

    print("The products present in the store previously were:\n\n", 
      "1", food, "\n\n", "2", stationary, "\n\n", 
      "3", toys, "\n\n", "4", house_hold, "\n\n", 
      "5", electronics, "\n\n")

    print("If you want to re - enter the main menu \n\
  	Input - 6")

    item_category = int(input("Enter the number choose the category in which you want to add new products:\n"))

    if item_category == 1:

        no_of_items = int(input("\n\nEnter the number of food items you want to add:\n"))
        for i in range(no_of_items):

            key = input("Enter the Name of the Food Product:\n")
            value = int(input("Enter the quantity of the Product:\n"))

            food[key] = value

        Home_Page()

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

    elif item_category == 2:

        no_of_items = int(input("Enter the number of stationary items you want to add:\n"))
        for i in range(no_of_items):

            key = input("Enter the Name of the Stationary Product:\n")
            value = int(input("Enter the quantity of Statonary the Product:\n"))

            stationary[key] = value

        Home_Page()

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

    elif item_category == 3:

        no_of_items = int(input("Enter the number of toy products you want to add:\n"))
        for i in range(no_of_items):

            key = input("Enter the Name of the Toys:\n")
            value = int(input("Enter the quantity of the Toys:\n"))

            toys[key] = value

        Home_Page()

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

    elif item_category == 4:

        no_of_items = int(input("Enter the number of House Hold Products you want to add:\n"))
        for i in range(no_of_items):

            key = input("Enter the Name of the House Hold Product:\n")
            value = int(input("Enter the quantity of the House Hold Product:\n"))

            house_hold[key] = value

        Home_Page()

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

    elif item_category == 5:

        no_of_items = int(input("Enter the number of Electronic Appliances you want to add:\n"))
        for i in range(no_of_items):

            key = input("Enter the Name of the Electronic Appliances:\n")
            value = int(input("Enter the quantity of the Electronic Appliance:\n"))

            electronics[key] = value

        Home_Page()

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

    elif item_category == 6:

        print("\n\nExiting Appending_Content function\n\
Enter into the main menu.......\n\n\n")

        Home_Page()

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

    else:

        count_1 = 5

        while count_1 > 0:

            print("The entered values are wrong you have\n", count_1, "chances left\n\
Please enter the correct values")

            print("The products present in the store previously were:\n\n",
                  "1", food, "\n\n", "2", stationary, "\n\n",
                  "3", toys, "\n\n", "4", house_hold, "\n\n",
                  "5", electronics, "\n\n")

            print("If you want to re - enter the main menu \n\
Input - 6")

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
            
            item_category = int(input("Enter the number choose the category in which you want to add new products:\n"))


            if item_category == 1:

                no_of_items = int(input("\n\nEnter the number of food items you want to add:\n"))
                for i in range(no_of_items):

                    key = input("Enter the Name of the Food Product:\n")
                    value = int(input("Enter the quantity of the Product:\n"))

                food[key] = value
                Home_Page()

                break

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

            elif item_category == 2:

                no_of_items = int(input("Enter the number of stationary items you want to add:\n"))
                for i in range(no_of_items):

                    key = input("Enter the Name of the Stationary Product:\n")
                    value = int(input("Enter the quantity of Statonary the Product:\n"))

                stationary[key] = value
                Home_Page()

                break

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

            elif item_category == 3:

                no_of_items = int(input("Enter the number of toy products you want to add:\n"))
                for i in range(no_of_items):

                    key = input("Enter the Name of the Toys:\n")
                    value = int(input("Enter the quantity of the Toys:\n"))

                toys[key] = value
                Home_Page()

                break

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

            elif item_category == 4:

                no_of_items = int(input("Enter the number of House Hold Products you want to add:\n"))
                for i in range(no_of_items):

                    key = input("Enter the Name of the House Hold Product:\n")
                    value = int(input("Enter the quantity of the House Hold Product:\n"))

                house_hold[key] = value
                Home_Page()

                break

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

            elif item_category == 5:

                no_of_items = int(input("Enter the number of Electronic Appliances you want to add:\n"))
                for i in range(no_of_items):

                    key = input("Enter the Name of the Electronic Appliances:\n")
                    value = int(input("Enter the quantity of the Electronic Appliance:\n"))

                electronics[key] = value
                Home_Page()

                break

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

            elif item_category == 6:

                print("\n\nExiting Appending_Content function\n\
Enter into the main menu.......\n\n\n")

                Home_Page()

                break

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
            
            else:

                count_1 -= 1

        else:

            print("The values entered by the user are incorrect please quit the program and then re - start the program")
            quit()

            

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------


def Notification(mydict):

    category_items = mydict.items()

    for i, j in category_items:

        if j < 50:
            print("The item:", i, "has very less quantity left\n\
Please buy more of this product soon...\n")

        else:
            pass

    print("Entering the Home_Page\n\
  	Exiting the main menu.......")

    Home_Page()

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------
    
def Statistcs():
    pass

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

def Database_Management():
    pass

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

def Sales():

    print("These are the product categories present in the store:\n\
1) Food\n\
2) Stationary\n\
3) Toys\n\
4) House Hold\n\
5) Electronics")
    
    category_choice = int(input("Enter the choice for the category from which you to buy the products:"))

    if category_choice == 1:
        print("You have chosen category of food items.\n\
These are the items present in the store:\n")

        
#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

def Home_Page():

    print("\n\nWelcome to SuperMarket GO\n\n\
You can do the following in this software\n\
1) Checking The Quantity of Products present in the store.\n\
2) Checking the requirements of Products for the next ordering\n\n")


    choice = int(input("Enter a number to perform the required function:"))

    if choice == 1:
        Appending_Content()

    elif choice == 2:

        print("The products present in the store previously were:\n\n",
              "1", food, "\n\n", "2", stationary, "\n\n", "3", toys, "\n\n",
              "4", house_hold, "\n\n", "5", electronics, "\n\n")

        choice_category = int(input("Enter the number to choose the respective category to attain notification:"))


        if choice_category == 1:
            Notification(food)


        elif choice_category == 2:
            Notification(stationary)


        elif choice_category == 3:
            Notification(toys)


        elif choice_category == 4:
            Notification(house_hold)


        elif choice_category == 5:
            Notification(electronics)

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

        else:

            count_3 = 5

            while count_3 > 0:

                print("The entered values are wrong you have\n", count_3, "chances left\n\
Please enter the correct values\n")

                print("The products present in the store previously were:\n\n",
                      "1", food, "\n\n", "2", stationary, "\n\n", "3", toys, "\n\n",
                      "4", house_hold, "\n\n", "5", electronics, "\n\n")

                choice_category = int(input("Enter the number to choose the respective category to attain notification:"))

                if choice_category == 1:
                    Notification(food)


                elif choice_category == 2:
                    Notification(stationary)


                elif choice_category == 3:
                    Notification(toys)


                elif choice_category == 4:
                    Notification(house_hold)


                elif choice_category == 5:
                    Notification(electronics)


                else:
                    count_3 -= 1

            else:

                print("The given input parameters by the user are incorrect\n\
Please quit the program and re - start the program")
                quit()

#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

    else:

        count_2 = 5

        while count_2 > 0:

            print("The entered values are wrong you have\n", count_2, "chances left\n\
Please enter the correct values\n")

            print("\n\nWelcome to SuperMarket GO\n\n\
You can do the following in this software\n\
1) Checking The Quantity of Products present in the store.\n\
2) Checking the requirements of Products for the next ordering\n\n")


            choice = int(input("Enter a number to perform the required function:"))

            if choice == 1:
                Appending_Content()
                break


            elif choice == 2:
                print("The products present in the store previously were:\n\n",
                      "1", food, "\n\n", "2", stationary, "\n\n", "3", toys, "\n\n",
                      "4", house_hold, "\n\n", "5", electronics, "\n\n")

                choice_category = int(input("Enter the number to choose the respective category to attain notification:"))

                if choice_category == 1:
                    Notification(food)
                    break


                elif choice_category == 2:
                    Notification(stationary)
                    break


                elif choice_category == 3:
                    Notification(toys)
                    break


                elif choice_category == 4:
                    Notification(house_hold)
                    break


                elif choice_category == 5:
                    Notification(electronics)
                    break


            else:
                count_2 -= 1

        else:
            print("The values entered by you for the input parameters are incorrect,\n\
Please quit the program and then restart the program")
            quit()


#--------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------

            
Home_Page()
