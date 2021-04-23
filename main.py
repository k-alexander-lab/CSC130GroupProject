"""This is the main file I used to test the code in the classes.
    The sample menu doesn't do anything right now, it just explains
    the toppings and types in the HotDog class."""

from Stock import Stock
from HotDog import HotDog

x = Stock("Classic", 3)

x.getDetails()

myOrder = HotDog("Classic Dog", 5)

myOrder.getDetails()

def displayMenu():
    print("Welcome to Talon's Hot Dog Stand")
    print("Hot Dogs: $4.00")
    print("1. Classic Dog: Ketchup and Mustard")
    print("2. Atlanta Dog: Chili, Slaw, Mustard")
    print("3. New York Dog: Onions, Spicy Mustard")
    print("4. Chicago Dog: Mustard, Relish, Onion, Pickle, Pepper, Tomato")
    print("5. Chili Dog: Chili, Onions, Cheese")
    print("6. Talon Dog: Chef's surprise")
    choice = input("Enter the number of the customer's choice: ")
    return choice
