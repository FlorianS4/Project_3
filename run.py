# Imports
import gspread
from google.oauth2.service_account import Credentials
import random
import os
import time
from hangman_stages import HANGMAN_STAGES

# width for characters
term_width = 80

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

def get_word():
    """
    Picks a random word form Google sheet.
    """
    
    word_list = WORD_SHEET.col_values(1)
    global word, hint
    word = random.choice(word_list)
    


 #for x in word:
        #print("_", end = " ")

def input_user():
    """
    takes input from user
    """
    letters_guessed = []
    game_over = False
    wrong_guesses_left = 7
    hangman_index = 0
    global timer_start
    timer_start = time.time()

    os.system("clear")

    hint = ""
    for i in range(0, len(word)):
        hint += "_"
    

    while game_over is False:
        print(hint)
        letters_guessed_str = " ".join(letters_guessed)

        print(f"Guessed letters: {letters_guessed_str} and guess left {wrong_guesses_left}")
        guess = input("Guess a letter: ").upper()

        if guess == "HELP":
            print(word)
        elif guess in letters_guessed:
            print("Letter already guessed, try another")
        elif not guess.isalpha() or len(guess) > 1:
            print("Guess not vialble, guess again")
        else:
            letters_guessed.append(guess)
            letters_guessed.sort()
            wrong_guesses_left, hangman_index, hint, game_over  = check_guess(guess, wrong_guesses_left, hangman_index, hint, game_over)
            


def check_guess(guess, wrong_guesses_left, hangman_index, hint, game_over):
    """
    Validates if letter is in word
    """
    if guess in word:
        print("Guess was correct!")
        hint = update_hint(guess, hint)
    elif guess not in word and hangman_index == 6:
        wrong_guesses_left -= 1
        print(wrong_guesses_left)
        print("     " + HANGMAN_STAGES[hangman_index])
        game_over = True
        print("Game Over! Returning to main menu")
        timer_end = time.time()
        main_menu()
    else:
        print("Incorrect guess, try another letter")
        print(wrong_guesses_left)
        wrong_guesses_left -= 1
        print(wrong_guesses_left)
        print("     " + HANGMAN_STAGES[hangman_index])
        hangman_index += 1
    return wrong_guesses_left, hangman_index, hint, game_over

def update_hint(guess, hint):
    """
    Adds a correct guess and updates hint
    """
    pos_of_guess = [i for i, character in enumerate(word) if character == guess]
    hint_arr = list(hint)

    for i in pos_of_guess:
        hint_arr[i] = guess
    
    hint = "".join(hint_arr)


    if "_" not in hint:
       game_over = True
       timer_end = time.time()
       seconds = timer_end - timer_start
       print(seconds)
       print("Game Over! You won, returning to Main Menu for now")
       main_menu()

    return hint

def main_menu():
    """
    Main Menu function
    Takes user input and runs user choice
    """
    print("[1] Play Hangman")
    print("[2] Game Instructions")
    print("[3] maybe i add something later")
    print("[4] Exit the program")
    choice = int(input("Enter your option: "))

    while choice != 0:
        if choice == 1:
            # Opens Hangman Game
            print("You choose 1, Game will start shortly....")
            get_word()
            input_user()
        elif choice == 2:
            # Opens Game Instructions
            print("You choose 2, Game Instructions will show in a few seconds....")
        elif choice == 3:
            # maybe there is a 3th Option :D
            print("Nothing to see in choice 3, maybe later..")
        elif choice == 4:
            exit()
        else: 
            print("choice not available")
    
    print()
    main_menu()
    choice = int(input("Enter your option: "))

print("Thanks for playing the game")


main_menu()


"""
valid_choices = ["1", "2", "3"]

while choice not in valid_choices:
    main_menu()

    tried with validator - doesn't work at the moment, will comeback to it later
"""


"""
get_word()
print(get_word())
"""

"""
input_user()
print(input(user))
"""

main_menu()
print(main_menu())