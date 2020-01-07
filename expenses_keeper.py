
import os.path
from os import path

def addAnExpense():
    
    print("You have chosen to add an expense...\n")

    categories_file_name = "expense-categories.txt"
    categories_file = open(categories_file_name, "r+")
    categories = categories_file.readlines()

    if len(categories) == 0:
        categories_file.close()
        viewCategories()
        categories_file.open()

    while True:

        date = input("Enter the expense date:")
        description = input("What was the expense for?")
        amount = input("How much was the expense?")
        amount = amount.replace("$", "")
        print("Select the category of the expense:")
        index = 1
        for c in categories:
            print(index + ". " + c)
            index = index + 1
        category_index = input("")
        category = categories[category_index - 1]

        print("Here is your expense summary:")
        print("Date: " + date)
        print("Description: " + description)
        print("Amount: " + amount)
        print("Category: " + category)
        
        record = input("\nRecord this expense?\n1 = Yes\n2 = No\n\n")
        if record == "1":
            
            expense = date + "," + description + "," + amount

            for i in range(int(category_index) - 1):
                expense = expense + ","
            for i in range(len(categories) - int(category_index) - 1):
                expense = expense + ","

            # Write out expense here. include and manage header

            print("Expense recorded...")
        else:
            print("Expense not recorded...")
            categories_file.close()
            return

        option = input("\nWould you like to add another expense?\n1 = Yes\n2 = No\n")
        if option == "2":
            break

    categories_file.close()


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
