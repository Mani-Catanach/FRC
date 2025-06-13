# Functions go here...
def yes_no(question):
    """Checks that users enter yes / y or no / n to a question"""

    while True:
        response = input(question).lower()

        if response == "yes" or response == "y":
            return "yes"
        elif response == "no" or response == "n":
            return "no"
        else:
            print("Please enter yes (y) or no (n).\n")

def make_statement(statement, decoration):
    """Emphasises headings by adding decoration at the start and end"""

    print(f"{decoration * 3} {statement} {decoration * 3}")

def instructions():
    make_statement("Instructions",decoration="{}")

    print('''This progrram will ask you for...
    - How many items you plan on selling 
    - The name of the product uou are selling
    - The costs for each component of the product
        (variable expenses)
    - Whether or not you have fixed expenses (if you have fixed expenses
        it will ask you what they are).
    -How much money you want to make
    
It will also  ask you  how much the reccomended sales price should be rounded to

The program outputs an itemised list of the variable and fixed expenses

Finally it will tell yoou how much you should sell each item for to reach your profit goal

The data will also be written to a text file which has the same name as your product and todays date
''')


# Main Routine goes here
print(make_statement("Fund Raising csalculator", "[]"))

print()
want_instructions =yes_no("Do you want to see the instructions?")
print()

if want_instructions == "yes":
    instructions()

print()
print(" program continues")
