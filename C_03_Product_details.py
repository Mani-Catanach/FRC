def num_check(question, num_type="float"):
    """Checks that response is a float / integer more than 0"""

    if num_type == "float":
        error = "Please enter a number for than 0"
    else:
        error = " Please enter an integer more than 0"

    while True:
        try:

            if num_type == "float":
                response = float(input(question))
            else:
                response = int(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

def not_blank(question):

    while True:
        response = input(question)

        if response != "":
            return response

        print("Sorry, this can't be blank. Please try again. \n")


# Main routine goes here

# loop for testing prposes
while True:
    product_name = not_blank("Product Name")
    quantity_made = num_check("Quantity being made: ", "integer")
    print(f"You are making {quantity_made} {product_name}")
    print()