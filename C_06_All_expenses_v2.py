import pandas
from tabulate import tabulate

#Functions go here
def not_blank(question):

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")


def num_check(question, num_type="float", exit_code=None):
    """checks user enter integer / float >0"""

    if num_type == "integer":
        error = "Oops - please enter an integer more than zero."
        change_to = int
    else:
        error = "Oops - please enter an integer more than zero."
        change_to = float
    while True:
        response = input(question)

        # check for the xit code
        if response == exit_code:
            return response

        try:

            if num_type == "float":
                response = float(response)
            else:
                response = int(response)

            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


def get_expenses(exp_type, how_many):
    """Gets variable / fixed expenses and outputs
    panda as a string and a subtotal of the expenses"""

    # Lists for panda
    all_items = []
    all_amounts = []
    all_dollar_per_item = []

    # Expenses dictionary
    expenses_dict = {
        "Item": all_items,
        "Amount": all_amounts,
        "$ / Item": all_dollar_per_item
    }

    # default amount to 1 for fixed expenses and to avoid PEP8 error for variable expenses
    amount = 1

    # loop to gey expenses
    while True:
        item_name = not_blank("Item name")

        # checks users enter at least one varibale expense
        if (exp_type == "variable" and
            item_name == "xxx") and len(all_items) == 0:
            print("Oops - youu have not entered anything. "
                  "You  need at least one item")
            continue

        elif item_name == "xxx":
            break

        # GEt item amount <enter> defaults to numbger of products being made

        amount = num_check(f"How many <enter for {how_many}>: ", "integer")

        if amount == "":
            amount = how_many

        cost = num_check("Price for one?", "float")

        all_items.append(item_name)
        all_items.append(amount)
        all_dollar_per_item.append(cost)

    #make panda
    expense_frame = pandas.DataFrame(expenses_dict)

    # calculate  cost column
    expense_frame['Cost'] = expense_frame['Amount'] * expense_frame['$ / Item']

    # calculate subtotal
    subtotal = expense_frame['Cost'].sum()

    # apply currency formating to currency collumns
    add_dollars = ['Amount', '$ / Item', 'Cost']
    for var_item in add_dollars:
        expense_frame[var_item] = expense_frame[var_item].apply(currency)

    # make expense frame into a string with the desired column
    if exp_type == "variable":
        expense_string = tabulate(expense_frame, headers='keys',
                                  tablefmt='psql', showindex=False)
    else:
        expense_string = tabulate(expense_frame[['Item' 'Costt']], headers='keys',
                                  tablefmt='psql', showindex=False)
    # return the expenses panda and the subtotal
    return  expense_string, subtotal

def currency(x):
    """Formats numbers as currency (#.##)"""
    return "${:.2f}".format(x)

# main routine starts here

quantity_made = num_check("Quantity being made: ",
                          "integer")

print()

print("Getting Variable Costs...")
variable_expenses = get_expenses("variable", quantity_made)
print()
variable_panda = variable_expenses[0]
variable_subtotal = variable_expenses[1]

print("=== Variable Expenses ===")
print(variable_panda)
print(f"Variable subtotal: ${variable_subtotal:.2f}")
print()

print("Getting fixed costs...")
fixed_expenses = get_expenses("fixed", quantity_made)
print()
fixed_panda = fixed_expenses[0]
fixed_subtotal = fixed_panda[1]

print("=== Fixed Expenses ===")
print(fixed_panda)
print(f"Fixed Subtotal: ${fixed_subtotal:.2f}")

print()
total_expenses = variable_subtotal + fixed_subtotal
print(f"Total Expenses: ${total_expenses:.2f}")