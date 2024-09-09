# Imports
import gspread
from google.oauth2.service_account import Credentials
import random
import os
import time
import math
from hangman_stages import HANGMAN_STAGES
import pandas as pd
import colorama
from colorama import Fore, Back

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

# ASCII Art from https://www.asciiart.eu/text-to-ascii-art

HEADER_GAME = r"""
     _   _   ___   _   _ _____ ___  ___  ___   _   _ 
    | | | | / _ \ | \ | |  __ \|  \/  | / _ \ | \ | |
    | |_| |/ /_\ \|  \| | |  \/| .  . |/ /_\ \|  \| |
    |  _  ||  _  || . ` | | __ | |\/| ||  _  || . ` |
    | | | || | | || |\  | |_\ \| |  | || | | || |\  |
    \_| |_/\_| |_/\_| \_/\____/\_|  |_/\_| |_/\_| \_/      
    """

HEADER_WELCOME = r"""
    _    _ _____ _     _____ ________  ___ _____   _____ _____  
    | |  | |  ___| |   /  __ \  _  |  \/  ||  ___| |_   _|  _  | 
    | |  | | |__ | |   | /  \/ | | | .  . || |__     | | | | | | 
    | |/\| |  __|| |   | |   | | | | |\/| ||  __|    | | | | | | 
    \  /\  / |___| |___| \__/\ \_/ / |  | || |___    | | \ \_/ / 
     \/  \/\____/\_____/\____/\___/\_|  |_/\____/    \_/  \___/  
                                                                
                                                                
        _____ _   _  _____   _____   ___  ___  ___ _____        
        |_   _| | | ||  ___| |  __ \ / _ \ |  \/  ||  ___|       
        | | | |_| || |__   | |  \// /_\ \| .  . || |__         
        | | |  _  ||  __|  | | __ |  _  || |\/| ||  __|        
        | | | | | || |___  | |_\ \| | | || |  | || |___        
        \_/ \_| |_/\____/   \____/\_| |_/\_|  |_/\____/        
        """


HEADER_GAME_OVER = r"""
    _____   ___  ___  ___ _____   _____  _   _ ___________ 
    |  __ \ / _ \ |  \/  ||  ___| |  _  || | | |  ___| ___ \
    | |  \// /_\ \| .  . || |__   | | | || | | | |__ | |_/ /
    | | __ |  _  || |\/| ||  __|  | | | || | | |  __||    / 
    | |_\ \| | | || |  | || |___  \ \_/ /\ \_/ / |___| |\ \ 
    \____/\_| |_/\_|  |_/\____/   \___/  \___/\____/\_| \_|
    """


HEADER_GAME_WON = r"""
    __   _______ _   _   _    _  _____ _   _ 
    \ \ / /  _  | | | | | |  | ||  _  | \ | |
     \ V /| | | | | | | | |  | || | | |  \| |
      \ / | | | | | | | | |/\| || | | | . ` |
      | | \ \_/ / |_| | \  /\  /\ \_/ / |\  |
      \_/  \___/ \___/   \/  \/  \___/\_| \_/
    """

# Main Menu
def main_menu():
    """
    Main Menu function
    Takes user input and runs user choice
    """
    print(HEADER_GAME)
    print(HEADER_WELCOME)
    print("[1] Play Hangman")
    print("[2] Game Instructions")
    print("[3] Scoreboard")
    print("[4] Exit the program\n")

    validator = False
    while validator == False:
        choice = input("Enter your option: ")
        menu_choices = ["1", "2", "3", "4"]
        validator = to_validate(choice, menu_choices)
        
    if choice == "1":
        # Opens Hangman Game
        print("You choose 1, Game will start shortly....")
        get_word()
    elif choice == "2":
        # Opens Game Instructions
        print("You choose 2, Game Instructions will show in a few seconds....")
        get_instructions_for_game()
    elif choice == "3":
        # opens Scoreboard
        print("Scoreboard is opening...")
        scoreboard_worksheet = SHEET.worksheet("scoreboard")
        scoreboard_update(scoreboard_worksheet)
        print("\n")
        back_to_menu()
    elif choice == "4":
        exit()
    
    print()
    main_menu()
    choice = int(input("Enter your option: "))


# Instructions for Game
def get_instructions_for_game():
    """
    Instructions on how to play the game and how to navigate it
    """
    os.system("clear")
    instructions = r""" 
            _______________________________________________________
            /\                                                      \
        (O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)
            \/''''''''''''''''''''''''''''''''''''''''''''''''''''''/
            (                   How to play                        (
            )                                                      )
            (    Start the game with Option 1 for Hangman.         (
            )       Choose a category of your liking.              )

            (    Guess a word of the category of your choosing.    (
            )    Each blank represents a character of the word.    )
            (    If guessed correctly the blank will disapear and  (
            )        the guessed letter will be filled in.         )

            (        You have 7 lives or guesses per word.         (
            )  For every wrong guess the hangman starts to build.  )
            (   The game ends in two ways, either you guessed the  (
            )      word correctly or the hangman is finished.      )

            (    After you guessed correctly you can enter a       (
            )    username, so your score can be added to the       )
            (                    leaderboard.                      (
            (    Your score is made up out of how quick you        (
            )    answer, how long the word is and how many         )
            (               wrong guesses you have.                (
            /\''''''''''''''''''''''''''''''''''''''''''''''''''''''\    
        (O)===)><><><><><><><><><><><><><><><><><><><><><><><><><><><)==(O)
            \/______________________________________________________/"""
    print(instructions + "\n")
    back_to_menu()


# Scoreboard
def scoreboard_update(worksheet):
    """
    sorts scoreboard, with the lowest score on top
    
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



# Back to Menu function
def back_to_menu():
    """
    functions to get the user back to the menu, or exit the program
    """
    print("[1] Back to main menu")
    print("[2] Exit the program \n")

    validator = False
    while validator == False:
        choice = input("Enter your option: ")
        back_to_menu_choices = ["1", "2"]
        validator = to_validate(choice, back_to_menu_choices)

    if choice == "1":
        os.system("clear")
        main_menu()        
    elif choice == "2":
        exit()

# game function
def get_word():
    """
    Picks a random word from the category the users choose
    gets the word from Google sheets
    """
    global word, hint

    print("[1] MOVIES")
    print("[2] ANIMALS")
    print("[3] VIDEO GAMES")
    print("[4] SPORTS")
    print("[5] FRUITS \n")

    validator = False
    while validator == False:
        category = input("Select a category: ")
        category_choices = ["1", "2", "3", "4","5"]
        validator = to_validate(category, category_choices)
   
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

    print("Loading Game \n")


# input function
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

        print(f"Guessed letters: {letters_guessed_str} and guess left {wrong_guesses_left}\n")
        guess = input("Guess a letter: \n").upper()

        if guess == "HELP":
            print(word)
        elif guess in letters_guessed:
            print(Fore.RED + "Letter already guessed, try another"+ Fore.RESET + "\n")
        elif not guess.isalpha() or len(guess) > 1:
            print(Fore.RED + "Guess not vialble, guess again" + Fore.RESET + "\n")
        else:
            letters_guessed.append(guess)
            letters_guessed.sort()
            wrong_guesses_left, hangman_index, hint, game_over  = check_guess(guess, wrong_guesses_left, hangman_index, hint, game_over)
            

# guess function
def check_guess(guess, wrong_guesses_left, hangman_index, hint, game_over):
    """
    Validates if letter is in word
    """
    if guess in word:
        print(Fore.GREEN + "Guess was correct!" + Fore.RESET + "\n")
        hint = update_hint(guess, hint, wrong_guesses_left)
    elif guess not in word and hangman_index == 6:
        wrong_guesses_left -= 1
        print(wrong_guesses_left)
        print("     " + HANGMAN_STAGES[hangman_index])
        game_over = True
        print(HEADER_GAME_OVER)
        print("The word you were looking for was" + Fore.MAGENTA + f" {word}" + Fore.RESET + ".\n")
        print("Game Over! Return to main menu or exit the program\n")
        timer_end = time.time()
        back_to_menu()
    else:
        print(Fore.RED + "Incorrect guess, try another letter" + Fore.RESET + "\n")
        wrong_guesses_left -= 1
        print(wrong_guesses_left)
        print("     " + HANGMAN_STAGES[hangman_index])
        hangman_index += 1
    return wrong_guesses_left, hangman_index, hint, game_over


# update hint function
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
       calculate_score(wrong_guesses_left, seconds)
       get_username(wrong_guesses_left, seconds, score)
       print(HEADER_GAME_WON)
       print("Game Over! You won, congratulation!\n")
       back_to_menu()

    return hint


# username function for after game
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
        print(Fore.RED + f"Invalid username: {e} please try again.\nYou need to enter max 12 letter/s only." + Fore.RESET + "\n")
        return False
    else: 
        return True


# get username for scoreboard add
def get_username(wrong_guesses_left, seconds, score):
    """
    getting and validating username and add it with the time
    and wrong guesses left to the scoreboard 
    """
    username_to_validate = False
    while username_to_validate is False:
        username = input("Enter username (max. 12 letters): \n")
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


# calculate score function
def calculate_score(wrong_guesses_left, seconds):
    """
    calculates a score, based on the word lenght, guesses left and time
    """
    global score
    score = math.ceil(seconds * 100 / (len(word)) + (wrong_guesses_left))
    print(score)


# validation for input
def to_validate(choice, valid_list):
    """
    validate input from user againts existing list of choices
    """
    if choice in valid_list:
        validator = True
        return validator
    else:
        validator = False
        print(Fore.RED + "Choice is not valid, please try again!" + Fore.RESET + "\n")
        return validator


main_menu()