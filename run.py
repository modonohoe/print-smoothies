import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint
from datetime import datetime, timedelta

# The scope lists the APIs the program should access in order to run
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


# based on w3schools article and geeksforgeeks.or for .timedelta
current_time = datetime.now()
collection_time = current_time + timedelta(hours=1.5)
# print(current_time.strftime("%X"))

# code modified from Love Sandwiches tutorial and influenced by TechWithTim


class Order:
    """
    creates an instance of customer's smoothie order
    items are lists to allow multiple items
    """
    def __init__(self, name, smoothie, _size, yoghurt, price):
        self.name = name
        self.smoothie = smoothie
        self._size = _size
        self.yoghurt = yoghurt
        self.price = price


cust_order = Order("Damien", "Berry Blast", "Large", "Soya", 5)


def get_name(cust_order):
    """
    gets the customers name
    this will then be linked to their order
    customer name must be 10 characters max and letters only
    """
    cust_order.name = None

    while True:
        cust_order.name = input("Whose name should we put on this order?\n")
        if not cust_order.name.isalpha() or not len(cust_order.name) < 10:
            print("Please try again - ensure your name does not:")
            print("exceed 10 characters or include any numbers")
            continue
        else:
            break
    print("Thank you " + cust_order.name.capitalize() + "!")
    return cust_order.name


def select_smoothie(cust_order):
    """
    User enters the id number of their chosen smoothie
    Number will choose corresponding index from list
    The choice is then appended to the Order
    """

    print("MAKE YOUR CHOICE:\n")
    print("1 = Tropical Dreamwave")
    print("2 = Berry Bliss")
    print("3 = Peanut Butter Power")
    print("4 = Strawbalicious Banana Blast")
    print("5 = Protein-Packed Choco Cherry")
    print("6 = Green Energy Boost")
    print("7 = Mango Mix")
    print("8 = Pomegranate Passion")
    print("9 = Peaches and Cream")
    print("10 = print(smoothies) Power Pop\n")

    smoothies = ["Tropical Dreamwave", "Berry Bliss", "Peanut Butter Power",
                 "Strawbalicious Banana Blast", "Protein-Packed Choco Cherry",
                 "Green Energy Boost", "Mango Mix", "Pomegranate Passion",
                 "Peaches and Cream", "print(smoothies) Power Pop"]

    cust_order.smoothie = int(input("Enter smoothie id number: "))
    # parse user input to use as an index number

    while True:
        # condition checks that number is not <10
        if 1 <= cust_order.smoothie <= len(smoothies):
            cust_order.smoothie = smoothies[cust_order.smoothie - 1]
            print(cust_order.smoothie + " added to order ✨\n")
            break
        else:
            print("Invalid smoothie number. Please try again.")
    return cust_order.smoothie


def select_size(cust_order):
    """
    Prompts customer for the size smoothie
    Appends choice to Order._size
    """
    print("What size would you like?")
    print("--> type R for regular (500ml) €4")
    print("--> type L for large (700ml) €5")
    cust_order._size = None

    while True:
        cust_order._size = input("Enter size: \n").upper()  # converts if lower

        if cust_order._size == "R":
            print("You chose regular \n")
            cust_order._size = "regular"
            break
        elif cust_order._size == "L":
            print("You chose large \n")
            cust_order._size = "large"
            break
        else:
            print("Please enter either 'R' or 'L'")


if cust_order._size == "regular":
    cust_order.price = 4
else:
    cust_order.price = 5


def select_yoghurt(cust_order):
    """
    Prompts customer for the size smoothie
    Appends choice to rder.yoghurt
    """
    print("Which yoghurt would you like?")
    print("--> type D for dairy")
    print("--> type S for soya")

    cust_order.yoghurt = None

    while True:
        cust_order.yoghurt = input("Enter choice: \n").upper()
        # converts if lower case

        if cust_order.yoghurt == "D":
            print("You chose dairy yoghurt 🥛 \n")
            cust_order.yoghurt = "dairy"
            break
        elif cust_order.yoghurt == "S":
            print("You chose soya yoghurt 🥛 \n")
            cust_order.yoghurt = "soya"
            break
        else:
            print("Please enter either 'D' or 'S'")


def review(cust_order):
    """
    displays current order to customer
    gives option to edit the order
    or proceed and confirm the order
    """
    print("--- ORDER REVIEW ---\n\nYour order:")
    print("Name: " + f" {cust_order.name}")
    print("Smoothie: " + f"{cust_order.smoothie}")
    print("Details: " + f"{cust_order._size}, {cust_order.yoghurt}")
    print("Price: €" + f" {cust_order.price}")

    print("Please enter Y to confirm, or N to edit your order 🙂")
    print("(Note: Payment for your order upon collection)\n")

    while True:
        confirmation = input("Are you happy to proceed with this order?: ")

        if confirmation in ("Y", "y"):
            break

        elif confirmation in ("N", "n"):
            # edit_order()
            break
        else:
            print("Please enter either Y or N (previous entry not valid)")


def end_single():
    """
    Displays final confirmation message
    for a 'one-off' single order
    """
    print("\n🎉 🎉 🎉   ORDER SUCCESSFUL!  🎉 🎉 🎉\n")
    print("Your order will be available for collection TODAY from:\n")
    print("           " + collection_time.strftime("%X") + "\n")
    print("Thank you for ordering with print(smoothies)\n\n")

    # adapted return_to_main_menu function
    while True:
        end_single = input("\nReturn to main menu? Y / N\n")
        if end_single in ("Y", "y"):
            main_menu()
            break
        elif end_single in ("N", "n"):
            print("Have a great day 🙂")
            break
        else:
            print("Please enter either Y or N (previous entry not valid)")


def return_to_main_menu():
    """
    gives option to return to Main Menu
    """
    print("\n\nReturn to main Menu or begin order:")
    while True:
        return_to_main_menu = input("Return to main menu? Y / N\n")
        if return_to_main_menu in ("Y", "y"):
            main_menu()
            break
        elif return_to_main_menu in ("N", "n"):
            get_name(cust_order)
            break
        else:
            print("Please enter either Y or N (previous entry not valid)")


def display_menu():
    """
    displays menu items for customer
    """
    print("Here is our current menu: \n")
    print("          DRINKS MENU         \n")
    print("All of our drinks are made with a yoghurt base (dairy OR soya)")
    print("PLEASE NOTE YOUR SMOOTHIE'S NUMBER FOR THE ORDERING PROCESS \n")

    pprint(current_menu)  # Google Sheets data
    return_to_main_menu()


def main_menu():
    """
    Welcome message to customer
    Displays options to view menu, order or
    set up a reoccuring order
    """
    print("\n\nWelcome to print(smoothies)!\n")
    print("Dublin's famous on-the-go smoothie bar 🍹 \n")
    print("We are open from Monday to Friday 7am-4pm\n")
    print("Drop in to order one of our speciality smoothies")
    print("or order for collection through this terminal!\n")
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n")
    print("Please enter one of the following (1, 2 or 3) then PRESS ENTER:")
    print(" 1 = view current menu \n 2 = place order for collection \n")

    menu_action = input("Your Choice: ")

    if menu_action == "1":
        display_menu()
    elif menu_action == "2":
        get_name(cust_order)
    else:
        raise ValueError(
            f"Please enter either 1, 2 or 3 (previous entry not valid)"
        )


main_menu()
select_smoothie(cust_order)
select_size(cust_order)
select_yoghurt(cust_order)
review(cust_order)
end_single()
