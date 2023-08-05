# Code taken from the 'love_sandwiches' tutorial
import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

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

customer_order = [] 
customer_total = []
 

def display_menu():
    """
    Displays menu items for customer
    """
    print("You chose option 1. Here is our current menu: \n")
    print("All of our print(smoothies) are made with a yoghurt base (dairy OR soya)")
    print("PLEASE NOTE THE NUMBER OF YOUR CHOSEN SMOOTHIE FOR THE ORDERING PROCESS \n")
    pprint(current_menu)

    # give option to order

    # give option to return to Main Menu
    return_to_main = input("\nReturn to main menu? Y / N\n")

    if return_to_main == "Y" or "y":
        main()
    
    elif return_to_main == "N" or "n":
        # option to order CALL ORDER FUNCTION
        print("okay")
    
    else:
        raise ValueError(
        f"Please enter either Y or N(previous entry not valid)"
        )

smoothies = ["Tropical Dreamwave", "Berry Bliss", "Peanut Butter Power",
             "Strawbalicious Banana Blast", "Protein-Packed Choco Cherry",
             "Green Energy Boost", "Mango Magic Mix", "Pomegranate Passion",
             "Peaches and Cream", "print(smoothies) Power Pop"]


# one-off order

class cust_order:
    """
    Defines the customers one-off order
    """
    def __init__(self):
        self.name = "Damien"
        self.smoothie_name = 5
        self.smoothie_size = 
        self.quantity = 2
        self.total = 



    def 



# reoccuring order 

def main():
    print("Welcome to print(smoothies)!\n")
    print("Dublin's famous on-the-go smoothie bar 🍹 \n")
    print("Location: Dublin City Centre\n")
    print("We are open from Monday to Friday 7am-4pm\n")
    print("Drop in to order one of our speciality smoothies\n")
    print("or order for collection through this terminal!\n")
    print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n")


    print("Please enter one of the following options (1, 2 or 3) then PRESS ENTER:")
    print(" 1 = view current menu \n 2 = order \n 3 = set up reocurring order \n")

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



main()

ticket = cust_order()














