
import os.path
from os import path

def addAnExpense():
    pass

def viewExpenses():
    pass

def viewCategories():

    # Name the file
    categories_file_name = "expense-categories.txt"

    categories_file = open(categories_file_name, "r+")
    categories = categories_file.readlines()

    # Print the categories
    print()
    if len(categories) == 0:
        print("You have no categories! Make sure to add one!\n")
    else:
        print("Here are your categories:")
        index = 1
        for category in categories:
            print(str(index) + ". " + category)
            index = index + 1
        print()

    option = input("Would you like to add a Category?\n1 = Yes\n2 = No\n")
    if option == "1":
        while True:
            categories_file.write(input("\nWhat Category would you like to add?\n"))
            print("Category added...\n")
            another = input("Add another?\n1 = Yes\n2 = No\n")
            if another == "1":
                continue
            else:
                break
    print()
    
    categories_file.close()

    add = input("Add an expense?\n1 = Yes\n2 = No\n")
    if add == "1":
        addAnExpense()

def main():

    print("Welcome to your Expenses Keeper!")
    print("Choose an option:")
    print("1. Add an expense")
    print("2. View Expenses")
    print("3. View and add Categories")

    option = input("")

    if option == "1":
        addAnExpense()
    elif option == "2":
        viewExpenses()
    elif option == "3":
        viewCategories()

if __name__ == "__main__":
    main()
