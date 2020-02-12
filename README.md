# Expenses Keeper

Expenses Keeper is a simple tool to help keep track of one's expenses. Users can add an expense to a comma separated file to categorize them and keep track of them. I also intended it as a learning tool for new programmers.

Here is an example of the end result of a file built with Expense Keeper:

![Expenses Keeper File](/home/jared/Projects/expenses-keeper/expenses-file-screenshot.png?raw=True)

This is useful because it is an easy way to see a running list of all of one's expenses in one place and be able to do some simple analysis on it.

## Anatomy

1. __expense-categories.txt__ - This file holds a list of categories that make up the header of the expenses file. Before starting to use the CLI, simply add your categories to the list each on its own line. You can add new categories at any time but make sure to preserve the original order and add them at the end of the list.
2. __expenses.csv__ - This is the file where the expenses are recorder.
3. __expenses_keeper.py__ - This is the source file of the program.

## Usage

To run Expenses Keeper, simply:

```
1. Open a terminal
2. Change directories to the folder containing expenses_keeper.py
3. Run: python expenses_keeper.py
4. Follow the prompts
```

## Notes

This is obviously the bare minimum implementation of such a program. There are multiple things that could be added including category management and simple expense calculations like totaling. However, I've found it useful to keep track of my own expenses and maybe you will too!

