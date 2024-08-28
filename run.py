# Imports
import gspread
from google.oauth2.service_account import Credentials
import random

# Variables for google sheet
SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("words_sheet")
WORD_SHEET = SHEET.worksheet("words")

def main_menu():
    """
    Main Menu function
    Takes user input and runs user choice
    """
    print("[1] Play Hangman")
    print("[2] Game Instructions")
    print("[3] maybe i add something later")
    print("[0] Exit the program")

"""main_menu()
choice = int(input("Enter your option: "))

while choice != 0:
    if choice == 1:
        # Opens Hangman Game
        print("You choose 1, Game will start shortly....")
    elif choice == 2:
        # Opens Game Instructions
        print("You choose 2, Game Instructions will show in a few seconds....")
    elif choice == 3:
        # maybe there is a 3th Option :D
        print("Nothing to see in choice 3, maybe later..")
    else: 
        print("choice not available")
    
    print()
    main_menu()
    choice = int(input("Enter your option: "))

print("Thanks for playing the game")
"""

"""
valid_choices = ["1", "2", "3"]

while choice not in valid_choices:
    main_menu()

    tried with validator - doesn't work at the moment, will comeback to it later
"""

def get_word():
    """
    Picks a random word form Google sheet.
    """
    
    word_list = WORD_SHEET.col_values(1)
    word = random.choice(word_list)


get_word()
print(get_word())