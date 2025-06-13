import pandas


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


def get_expenses(exp_type):
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

        all_items.append(item_name)

    #RETurn all items for now so we can check loop
    return all_items