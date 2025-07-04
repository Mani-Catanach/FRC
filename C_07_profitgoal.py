import pandas
from tabulate import tabulate

#Functions go here
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


def profit_goal(total_costs):
    """calculates profit goal work out profit goal and total sales required"""
    # initialise variables and error message
    error = "please enter a valid profit goal\n"
    profit_type = ""
    amount = 0

    valid = False
    while not valid:

        #ask for profit goal...
        response = input("What is your profit goal (eg 500 or 50%)")

        #check if first character is $
        if response[0] == "$":
            profit_type = "$"
            # Get amount everything after the $
            amount = response[:-1]

        elif response[-1] == "%":
            profit_type = "%"
            # get amount ( everything before the %)
            amount = response[:-1]

        else:
            # set response to unknown amount for now
            profit_type = "unknown"
            amount = response

        try:
            # check amount is a number more than zero...
            amount = float(amount)
            if amount <= 0:
                print(error)
                continue

        except ValueError:
            print(error)
            continue

        if profit_type == "unknown" and amount >= 100:
            dollar_type = yes_no(f"Do you mean ${amount:.2f}. ie {amount:.2f} dollars? , y/n")

            # set profit type based on user answer above
            if dollar_type == "yes":
                profit_type = "$"
            else:
                profit_type = "%"

        elif profit_type == "unknown" and amount <= 100:
            percent_type = yes_no(f"Do you mean {amount}%? , y/n: ")
            if percent_type == "yes":
                profit_type = "%"
            else:
                profit_type = "$"

        # return profit goal to main routine
        if profit_type == "$":
            return amount
        else:
            goal = (amount/100) * total_costs
            return goal

# main routine goes here

# loop for testing purposes
while True:
     total_expenses = 200
     target = profit_goal(total_expenses)
     sales_target = total_expenses + target
     print(f"Profit Goal: ${target:.2f}")
     print(f"Sales Target: ${sales_target:.2f}")
     print()