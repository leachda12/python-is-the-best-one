# pass as many arguments as you want
def make_pizza(*toppings):
    # print the list of toppings that have been requested
    print("Here's what you asked for:")
    for topping in toppings:
        print(f"- {topping}")