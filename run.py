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
data = menu.get_all_values()

orders = SHEET.worksheet('orders')

regulars = SHEET.worksheet('regulars')


print("Welcome to print(smoothies)!\n")
print("Dublin's famous on-the-go smoothie bar 🍹 \n")
print("Location: Dublin City Centre\n")
print("We are open from Monday to Friday 7am-4pm\n")
print("Drop in to order one of our speciality smoothies\n")
print("or order for collection through this terminal!\n")
print("~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ \n")

print("Please enter one of the following options (1, 2 or 3):")
print(" 1 = view current menu \n 2 = order \n 3 = set up reocurring order \n")


