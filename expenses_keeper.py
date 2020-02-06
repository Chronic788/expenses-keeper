# Expenses Keeper.py
# ----------------------------------------------------------------------------------------------------------------------
# Jared Nelsen - Jan 2020
# ----------------------------------------------------------------------------------------------------------------------
# This simple python script is a tool to help keep track of expenses. I needed a way to quickly categorize and add
# expenses so I wrote this. I tried to be as explicit and clear as I could as I intend to use this as a learning tool
# for new programmers.
#
#   The format of the expenses file is:
#
#       Header Line : In the format: Date, Description, Category 1, Category 2, Category ..., Category N
#       Expense 1   : Amount lies in some category
#       Expense 2   : Amount lies in some category
#       Expense ... : Amount lies in some category
#       Expense N   : Amount lies in some category
#
#       An example of a file might look like:
#
#       Date	Description	           Income	Rent	Utilities	Gas	Cars	Healthcare	Shopping	Clothing	Groceries	Eating Out          	Entertainment	Travel	Business	Fees
#       01/01/19	Delta Baggage Fee													                                                                                 30		
#       01/01/19	Steam Game												                                                                            37.5			
#       01/02/19	Credit Card Interest															                                                                                       89.2
#       01/02/19	Fast food											                                                        5.45				
#       01/02/19	Groceries										                                                 140.85					
#       01/02/19	Spotify												                                                                                9.99			
#       01/03/19	Chick Fil A											                                                         8.8				
# 
# Recall that Python is interpreted. This means that each time a file is read, functions that are used must be already defined. For this script, this simply means that the file should be
# read from bottom to top to understand it best.

# Imports
import os.path
from os import path

# This function adds an expense to the expenses file. This is the core functionality of the program.
def addAnExpense():
    
    # Introduction
    print("\nYou have chosen to add an expense...\n")

    # Name the categories file
    categories_file_name = "expense-categories.txt"
    # Check to see if the categories file exits and create it if it does not
    if not os.path.exists(categories_file_name):
        print("Categories file does not exist! Make sure to add catagories by adding a line to the categories file!")
        with open(categories_file_name, "w"):
            pass
        print("\nCreated empty categories file in this directory called expense-categories.txt...")
        return

    # Open the categories file in write mode and read in the lines
    categories_file = open(categories_file_name, "r+")
    categories = categories_file.readlines()

    # Check to see if the file contains any categories and warn if it does not
    if len(categories) == 0:
        print("There are no categories in the categories file! Make sure to add one or more by manually editing the expense-categories.txt file in this directory.")
        print("The categories file should be formatted with each category on a new line. There is no header in the file.")
        print("\nExiting...")
        return

    # Forever
    while True:

        # Ask the user for input
        date = input("Enter the expense date: ")
        description = input("What was the expense for? ")
        amount = input("How much was the expense? ")
        amount = amount.replace("$", "")

        # Select the category of the expense
        print("\nSelect the category of the expense: ")
        index = 1
        for c in categories:
            print(str(index) + ". " + c.strip("\n"))
            index = index + 1
        category_index = input("")
        category = categories[int(category_index) - 1]

        # Summarize the expense
        print("\nHere is your expense summary:")
        print(" Date: " + date)
        print(" Description: " + description)
        print(" Amount: " + amount)
        print(" Category: " + category)
        
        # Ask whether to record the expense
        record = input("\nRecord this expense?\n1 = Yes\n2 = No\n\n")
        if record == "1":
            
            # Begin the expense line to be written
            expense = date + "," + description

            # Add in the expense amount in the correct place in the string of commas
            for i in range(int(category_index)):
                expense = expense + ","
            expense = expense + amount
            for i in range(len(categories) - int(category_index)):
                expense = expense + ","

            # Name the expenses file
            expense_file_name = "expenses.csv"
            # Create the expenses file if it does not exist
            if not path.exists(expense_file_name):
                with open(expense_file_name, "w"):
                    pass
            # Open the expense file and read in the lines
            expense_file = open(expense_file_name, "r+")
            expense_lines = expense_file.readlines()

            # Define a list to add the expense line to (We must do this because of the way the writelines function works)
            expense_write_lines = []

            # Test to see if the header line exists and include it to write if not
            have_to_write_header = False
            # If the expense file is empty we have to write the header
            if len(expense_lines) == 0:
                have_to_write_header = True
            # If the expense file has something in it we have to do some more thorough checks
            if len(expense_lines) > 0:
                # Pick the first line in the expenses file
                first_line_in_expenses_file = expense_lines[0]
                # Pick the first category
                first_category = categories[0].strip("\n")
                # If a category is not in the first line we have to write the header
                if not first_category in first_line_in_expenses_file:
                    print("First not in")
                    print("First line: " + first_line_in_expenses_file)
                    print("First category: " + first_category)
                    print(first_category in first_line_in_expenses_file)
                    have_to_write_header = True
            
            # Add the header to the list of lines to write out if we have to
            if have_to_write_header:
                # Add the beginning of the header string
                header = "Date,Description,"
                # Append all of the categories to the end of the header string
                for c in categories:
                    header = header + c.strip("\n") + ","
                # Append new line to the end of the header
                header = header + "\n"
                # Actually add the header to the list
                expense_write_lines.append(header)

            # Write the expense lines and make sure to append new lines
            expense_write_lines.append(expense)
            expense_write_lines.append("\n")
            expense_file.writelines(expense_write_lines)

            # Close the expense file
            expense_file.close()

            print("\nExpense recorded...")
        # If the user chose not to record the expense
        else:
            print("\nExpense not recorded...")
            # Close the file and quit
            categories_file.close()
            return

        option = input("\nWould you like to add another expense?\n1 = Yes\n2 = No\n")
        if option == "2":
            break

    categories_file.close()

# This is the main function
def main():

    # Welcome
    print("\nWelcome to your Expenses Keeper!")

    # Forever
    while True:
        # Give the user options
        print()
        print("Choose an option:")
        print("1. Add an expense")
        print("2. Exit")
        option = input("")
        # Branch out. I implemented it this way in order to add new options in the future
        if option == "1":
            addAnExpense()
        else:
            # Exit
            print("\nExiting Expenses Keeper...\n")
            break

if __name__ == "__main__":
    main()
