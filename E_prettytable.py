import pandas
from tabulate import tabulate

def currency(x):
    """Formats numbers as currency."""
    return "${:.2f}".format(x)

# lists for panda
all_items = ['A', 'B', 'C']
all_amounts = [10, 10, 10]
all_dollar_per_item = [1, 2, 3]

# expenses dict
expenses_dict = {
    "Item": all_items,
    "Amount": all_amounts,
    "$ / Item": all_dollar_per_item
}

expenses_frame = pandas.DataFrame(expenses_dict)
expenses_frame['Cost'] = expenses_frame['Amount'] * expenses_frame['$ / Item']

# apply currency formatting to currency columns
add_dollars = ['Amount', '$ / Item', 'Cost']
for var_item in add_dollars:
    expenses_frame[var_item] = expenses_frame[var_item].apply(currency)

    print(tabulate(expenses_frame, headers='keys', tablefmt='psql', showindex=False))

    # use tabulate to generate a string instead of printing
    print("=== All Columns ===")
    expenses_string = tabulate(expenses_frame, headers='keys', tablefmt='psql',
                               showindex=False)
    print(expenses_string)
    print()

    print("=== Fixed Expenses Columns ===")
    fixed_string = tabulate(expenses_frame[['Item', 'Cost']], headers='keys',
                            tablefmt='psql', showindex=False)
    print(fixed_string)