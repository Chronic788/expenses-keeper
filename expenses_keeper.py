
import os.path
from os import path

# Got write out correct
# Last thing is to write logic to add category to header if does not exist

def addAnExpense():
    
    print("\nYou have chosen to add an expense...\n")

    categories_file_name = "expense-categories.txt"
    if not os.path.exists(categories_file_name):
        print("Categories file does not exist! Create it by adding a category in the main menu.\n")
        return

    categories_file = open(categories_file_name, "r+")
    categories = categories_file.readlines()

    if len(categories) == 0:
        categories_file.close()
        viewCategories()
        categories_file.open()

    while True:

        date = input("Enter the expense date: ")
        description = input("What was the expense for? ")
        amount = input("How much was the expense? ")
        amount = amount.replace("$", "")
        print("\nSelect the category of the expense: ")
        index = 1
        for c in categories:
            print(str(index) + ". " + c.strip("\n"))
            index = index + 1
        category_index = input("")
        category = categories[int(category_index) - 1]

        print("\nHere is your expense summary:")
        print(" Date: " + date)
        print(" Description: " + description)
        print(" Amount: " + amount)
        print(" Category: " + category)
        
        record = input("\nRecord this expense?\n1 = Yes\n2 = No\n\n")
        if record == "1":
            
            expense = date + "," + description

            for i in range(int(category_index)):
                expense = expense + ","
            expense = expense + amount
            for i in range(len(categories) - int(category_index)):
                expense = expense + ","

            expense_file_name = "expenses.csv"
            if not path.exists(expense_file_name):
                temp_file = open(expense_file_name, "w")
                temp_file.close()
            expense_file = open(expense_file_name, "r+")
            expense_lines = expense_file.readlines()

            expense_write_lines = []

            # Write out header
            just_wrote_header = False
            if len(expense_lines) == 0:
                categories_line = "Date,Description,"
                for i in range(len(categories)):
                    categories_line = categories_line + categories[i].strip("\n")
                    categories_line = categories_line + ","
                categories_line = categories_line + "\n"
                expense_write_lines.append(categories_line)
                just_wrote_header = True



            expense_write_lines.append(expense)
            expense_write_lines.append("\n")

            expense_file.writelines(expense_write_lines)

            expense_file.close()

            print("Expense recorded...")
        else:
            print("Expense not recorded...")
            categories_file.close()
            return

        option = input("\nWould you like to add another expense?\n1 = Yes\n2 = No\n")
        if option == "2":
            break

    categories_file.close()

def viewCategories():

    # Name the file
    categories_file_name = "expense-categories.txt"

    if not path.exists(categories_file_name):
        tempFile = open(categories_file_name, "w")
        tempFile.close()

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
            print(str(index) + ". " + category.strip("\n"))
            index = index + 1
        print()

    option = input("Would you like to add a Category?\n1 = Yes\n2 = No\n")
    if option == "1":
        while True:
            new_category = []
            new_category.append(input("\nWhat Category would you like to add?\n") + "\n")
            categories_file.writelines(new_category)
            print("\nCategory added...\n")
            another = input("Add another?\n1 = Yes\n2 = No\n")
            if another == "1":
                continue
            else:
                break
    print()
    categories_file.close()

def main():

    print("\nWelcome to your Expenses Keeper!")

    while True:
        print()
        print("Choose an option:")
        print("1. Add an expense")
        print("2. View and add Categories")
        print("3. Exit")

        option = input("")

        if option == "1":
            addAnExpense()
        elif option == "2":
            viewCategories()
        elif option == "3":
            print("\nExiting Expenses Keeper...\n")
            break

if __name__ == "__main__":
    main()
