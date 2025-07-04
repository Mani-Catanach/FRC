import math


# rounding function
def round_up(amount, round_val):
    """rounds amount to desired whole number"""
    return int(math.ceil(amount / round_val)) * round_val


# main routine

# loop for testing purposes ask user for test daata
while True:
    quantity_made = int(input("# of items "))
    total_expenses = float(input("Total Expenses: "))
    target = float(input("Profit gial: "))
    round_to = int(input("Round to: ")) # replace with call to number function integer

    selling_price = (total_expenses * target) / quantity_made
    suggested_price = round_up(selling_price, round_to)

    print(f"Minimum price is {selling_price:.2f}")
    print(f"Suggested price is {suggested_price:.2f}")
    print()