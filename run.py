# Imports
import gspread
from google.oauth2.service_account import Credentials
import random
import os
import time
import math
from hangman_stages import HANGMAN_STAGES
import pandas as pd

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
    Picks a random word from the category the users choose
    gets the word from Google sheets
    """
    global word, hint

    print("1: MOVIES")
    print("2: ANIMALS")
    print("3: VIDEO GAMES")
    print("4: SPORTS")
    print("5: FRUITS")
    category = input("Select a category: ")

    # valid_choices = ["1", "2", "3", "4". "5"]
        #if category not in valid_choices:
            #print(f"No category found, try again.")
            #get_word()
    if category == "1":
        word_list = WORD_SHEET.col_values(1)
        word = random.choice(word_list)
        input_user()            
    elif category == "2":
        word_list = WORD_SHEET.col_values(2)
        word = random.choice(word_list)
        input_user()
    elif category == "3":
        word_list = WORD_SHEET.col_values(3)
        word = random.choice(word_list)
        input_user()
    elif category == "4":
        word_list = WORD_SHEET.col_values(4)
        word = random.choice(word_list)
        input_user()
    elif category == "5":
        word_list = WORD_SHEET.col_values(5)
        word = random.choice(word_list)
        input_user()
    else:
        print("No Category found, choose between 1 - 5")
        get_word()

    print("Loading Game")
    
    #word_list = WORD_SHEET.col_values(1)
    
    


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
        hint = update_hint(guess, hint, wrong_guesses_left)
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


def update_hint(guess, hint, wrong_guesses_left):
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
       seconds = round(seconds, 2)
       print(seconds)
       calculate_score(wrong_guesses_left, seconds)
       get_username(wrong_guesses_left, seconds, score)
       print("Game Over! You won, returning to Main Menu for now")
       main_menu()

    return hint


def username_validation(username):
    """
    Validate username to be all letters and within 12 characters
    """
    try:
        if not username.isalpha() or len(username) > 12:
            raise ValueError(
                f"Your input {username}"
            )
    except ValueError as e:
        print(f"Invalid username: {e} please try again.\nYou need to enter max 12 letter/s only.\n")
        return False
    else: 
        return True


def get_username(wrong_guesses_left, seconds, score):
    """
    getting and validating username and add it with the time
    and wrong guesses left to the scoreboard 
    """
    username_to_validate = False
    while username_to_validate is False:
        username = input("Enter username (max. 12 letters): ")
        username_to_validate = username_validation(username)
        user_data_row = []
        user_data_row.append(username)
        user_data_row.append(wrong_guesses_left)
        user_data_row.append(seconds)
        user_data_row.append(score)
        print(user_data_row)
        scoreboard_worksheet = SHEET.worksheet("scoreboard")
        scoreboard_worksheet.append_row(user_data_row)
        scoreboard_update(scoreboard_worksheet)



def calculate_score(wrong_guesses_left, seconds):
    """
    calculates a score, based on the word lenght, guesses left and time
    """
    global score
    score = math.ceil((len(word) * 1000) + (wrong_guesses_left * 1000) / seconds)
    print(score)


def scoreboard_update(worksheet):
    """
    sorts scoreboard with fastest time on number 1
    """
    user_data_score = worksheet.get_all_values()
    columns = user_data_score[0]
    user_score = user_data_score[1:]
    user_score_line = pd.DataFrame(user_score, columns = columns)
    pd.set_option("display.colheader_justify", "center")
    user_score_line = user_score_line.sort_values(
        by = [ "SCORE"],
        ascending = [True]
    )
    user_score_line = user_score_line.reset_index(drop = True)
    user_score_line.index = user_score_line.index + 1

    print(user_score_line.head(10))


def main_menu():
    """
    Main Menu function
    Takes user input and runs user choice
    """
    print("[1] Play Hangman")
    print("[2] Game Instructions")
    print("[3] Scoreboard")
    print("[4] Exit the program")
    choice = int(input("Enter your option: "))

    while choice != 0:
        if choice == 1:
            # Opens Hangman Game
            print("You choose 1, Game will start shortly....")
            get_word()
            #input_user()
        elif choice == 2:
            # Opens Game Instructions
            print("You choose 2, Game Instructions will show in a few seconds....")
        elif choice == 3:
            # opens Scoreboard
            print("Scoreboard is opening...")
            scoreboard_worksheet = SHEET.worksheet("scoreboard")
            scoreboard_update(scoreboard_worksheet)
            main_menu()
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