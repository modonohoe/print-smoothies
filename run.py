import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
from datetime import datetime, timedelta

# The scope lists the APIs the program should access in order to run
# variables whose value does not change are 'constants'
# constant variable names are written in capital letters
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('print_smoothies')

# accesses names and ingredients of smoothies
menu = SHEET.worksheet('menu')
current_menu = menu.get_all_values()

orders = SHEET.worksheet('orders')

regulars = SHEET.worksheet('regulars')

# https://www.geeksforgeeks.org/python-datetime-timedelta-function/
# https://www.w3schools.com/python/python_datetime.asp
# future feature could import timezone library
current_time = datetime.now()
collection_time = current_time + timedelta(hours=1.5)
# print(current_time.strftime("%X"))

# Code modified from Love Sandwiches tutorial
# https://www.youtube.com/watch?v=JeznW_7DlB0&ab_channel=TechWithTim

smoothies = ["Tropical Dreamwave", "Berry Bliss", "Peanut Butter Power",
             "Strawbalicious Banana Blast", "Protein-Packed Choco Cherry",
             "Green Energy Boost", "Mango Magic Mix", "Pomegranate Passion",
             "Peaches and Cream", "print(smoothies) Power Pop"]

class Order:
    # creates an instance of order
    def __init__(self, customer, smoothie, _size, yoghurt, price):
        self.customer = customer
        self.smoothie = smoothie
        self._size = _size
        self.yoghurt = yoghurt
        self.price = price

    def ticket(self):
        print(f"{self.customer}'s order:")
        print(f"Smoothie(s): {self.smoothie}")
        print(f"Size(s): {self._size}")
        print(f"Yoghurt(s): {self.yoghurt}")
        print(f"Total: €{self.price}")


# class Reoccuring(Order):
    # adds further methods to a regular order
    # def __init__(self, collection_day)
    #     super().__init__(customer, smoothie, _size, yoghurt, price)
    #     self.collection_day = collection_day


def return_to_main_menu():
    # give option to return to Main Menu
    while True:
        return_to_main_menu = input("\nReturn to main menu? Y / N\n")
        if return_to_main_menu in ("Y", "y"):
            main_menu()
            break
        # option to order CALL ORDER FUNCTION
        elif return_to_main_menu in ("N", "n"):
            print("okay")
            break
        else:
            print("Please enter either Y or N(previous entry not valid)")


def display_menu():
    """
    Displays menu items for customer
    """
    print("Here is our current menu: \n")
    print("          DRINKS MENU         \n")
    print("All of our drinks are made with a yoghurt base (dairy OR soya)")
    print("PLEASE NOTE YOUR SMOOTHIE'S NUMBER FOR THE ORDERING PROCESS \n")
    pprint(current_menu)
    return_to_main_menu()


def get_name():
    customer_name = None

    while True:
        customer_name = input("Whose name should we put on this order?\n")

        if not customer_name.isalpha() or len(customer_name) < 10:
            print("Please try again - ensure your name does not:")
            print("exceed 10 characters or include any numbers")
            continue
        else:
            break
    print("Thank you " + customer_name.capitalize() + "!")

    return customer_name


def select_smoothie():
    print("Choose your smoothie:")
    print("1 = Tropical Dreamwave\n")
    print("2 = Berry Bliss")
    print("3 = Peanut Butter Power")
    print("4 = Strawbalicious Banana Blast")
    print("5 = Protein-Packed Choco Cherry")
    print("6 = Green Energy Boost")
    print("7 = Mango Magic Mix")
    print("8 = Pomegranate Passion")
    print("9 = Peaches and Cream")
    print("10 = print(smoothies) Power Pop")

    chosen_smoothie = input("Enter smoothie number(id): ")

    

def main_menu():
    print("Welcome to print(smoothies)!\n")
    print("Dublin's famous on-the-go smoothie bar 🍹 \n")
    print("We are open from Monday to Friday 7am-4pm\n")
    print("Drop in to order one of our speciality smoothies\n")
    print("or order for collection through this terminal!\n")
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n")
    print("Please enter one of the following (1, 2 or 3) then PRESS ENTER:")
    print(" 1 = view menu \n 2 = order \n 3 = set up reocurring order \n")

    menu_action = input("Your Choice: ")

    if menu_action == "1":
        display_menu()
    elif menu_action == "2":
        print("let's goooo")
    elif menu_action == "3":
        print("Let's set up order")
    else:
        raise ValueError(
            f"Please enter either 1, 2 or 3 (previous entry not valid)"
        )


def main():
    main_menu()


main()
