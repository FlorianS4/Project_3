# Hangman Game - Testing

![Hangman Game Start PNG](/assets/docs/readme-images/hangman-game-picture.png)

Visit the deployed site: [Hangman Game](https://hangman-project-3-fs-e5867a39357d.herokuapp.com/)



## Content
- [Validator Testing](#validator-testing)
     - [PEP8 Testing](#pep8-testing)
- [Browser Testing](#browser-testing)
- [Input Testing](#input-testing)
- [User Testing](#user-testing)
- [Manual Testing](#manual-testing)


### Validator Testing

#### PEP8 Testing

For validation of the python code i used the [PEP8 Validator](https://pep8ci.herokuapp.com/#).

<details>
<summary>PEP8 Validation for run.py</summary>

![PEP8 Validation run.py](/assets/docs/readme-images/pep8-validation.png)
</details>

<details>
<summary>PEP8 Validation for hangman_stages.py</summary>

![PEP8 Validation hangman_stages.py](/assets/docs/readme-images/hangman-stages-pep8-validation.png)
</details>

### Browser Testing
The website was successfully tested on the following browsers:
- Google Chrome
- Safari
- Mozilla Firefox

### Input Testing

I implemented a validator testing for every input the user has to make and they work correctly.

<details>
<summary>Validator Main Menu</summary>

![Validator Main Menu](/assets/docs/readme-images/main-menu-validation.png)
</details>

<details>
<summary>Validator Back to Menu</summary>

![Validator Back to Menu](/assets/docs/readme-images/validator-testing-back-to-menu.png)
</details>

<details>
<summary>Validator End of Game Menu</summary>

![Validator End of Game Menu](/assets/docs/readme-images/input-validator-end-of-game-menu.png)
</details>

<details>
<summary>Validator Word Input in Game</summary>

![Validator Game Input](/assets/docs/readme-images/validator-testing-input-game.png)
</details>

<details>
<summary>Validator username Input</summary>

![Validator Username](/assets/docs/readme-images/validator-enter-username.png)
</details>

### User Testing

**First Time User:**

- **I want to play a word-guessing game / Hangman game.**

    The user can play the game as one of the choices in the menu.
- **I want the site read instructions on how to play.**

    The user can find instructions on how to play in the main menu.
- **I want the program to be easy to navigate and use.**

    The navigation of the program is pretty simple, one just has to use numbers between 1-5.
- **I want to be able to test my knowledge in different categories.**

    There are 5 categories the user can choose from.
- **I want to take the quiz whenever, wherever.**

    The user can play the hangman game at whichever time he likes on all browsers. He only needs a stable internet connection.

**Returning User:**

- **I want to be able to try different categories.**

    There are 5 categories the user can choose from. 
- **I want different words in the same category.**

    If the user wants to he can replay the same categories again for a different random word.

**Frequent User:**

- **I want to save my highscore to a scoreboard.**

    The user has the option to save his score, after he won the game.
- **I want to see how well I did and compare myself to others.**

    The score will be transfered to a google sheet, and if the score is under the best 10 he will be displayed.
- **I want to play again, after I won the game.**

    The user has 3 options after he won, Add to scoreboard, Play again and Exit the Program.


### Manual Testing

- **Main Menu**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Pressing 1 to play the game | Category selection opens | Enter 1 | Category selections opens | Pass |
| Pressing 2 to open instractions | Instructions opens | Enter 2 | Instructions opens | Pass |
| Pressing 3 to open scoreboard | Scoreboard opens | Enter 3 | Scoreboard opens | Pass |
| Pressing 4 to exit the program | Program closes | Enter 4 | Program closes | Pass |
| Validation for input | Displaying error message when entering something other than numbers beetween 1-4 | Entering letters, whitespaces, higher numbers | Error message displays | Pass |

- **Game Instructions**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Displaying instrucations | Displaying instrucations | Opening instrucations via main menu input | Instrucations opens | Pass |
| Pressing 1 to get back to main menu | Return to main menu | Enter 1 | Returns to main menu | Pass |
| Pressing 2 to exit the program | Program closes | Enter 2 | Program closes | Pass |
| Validation for input | Displaying error message when entering something other than numbers beetween 1-2 | Entering letters, whitespaces, higher numbers | Error message displays | Pass |

- **Scoreboard**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Displays Scoreboard with the 10 best scores | Displaying scoreboard | Opening scoreboard via main menu input | Scoreboard opens | Pass |
| Pressing 1 to get back to main menu | Return to main menu | Enter 1 | Returns to main menu | Pass |
| Pressing 2 to exit the program | Program closes | Enter 2 | Program closes | Pass |
| Validation for input | Displaying error message when entering something other than numbers beetween 1-2 | Entering letters, whitespaces, higher numbers | Error message displays | Pass |

- **Play Hangman**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Displaying 5 categories | 5 categories are displayed for the user to choose from | Opening Play Hangman via main menu input | 5 categories are displayed | Pass |
| Pressing 1 to play category MOVIES | Picking a random word out of choosen category and starting the Hangman game | Enter 1 | Picks words from choosen category and starts game | Pass |
| Pressing 2 to play category ANIMALS | Picking a random word out of choosen category and starting the Hangman game | Enter 2 | Picks words from choosen category and starts game | Pass |
| Pressing 3 to play category VIDEO GAMES | Picking a random word out of choosen category and starting the Hangman game | Enter 3 | Picks words from choosen category and starts game | Pass |
| Pressing 4 to play category SPORTS | Picking a random word out of choosen category and starting the Hangman game | Enter 4 | Picks words from choosen category and starts game | Pass |
| Pressing 5 to play category FRUITS | Picking a random word out of choosen category and starting the Hangman game | Enter 5 | Picks words from choosen category and starts game | Pass |
| Validation for input | Displaying error message when entering something other than numbers beetween 1-5 | Entering letters, whitespaces, higher numbers | Error message displays | Pass |

- **Playing the game**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Entering correct letter to guess the word | If correct letter is guessed, "_" hint will be replaced by guessed letter | Entering a letter | If letter is correct, "_" hint will be recplaced by correct letter | Pass |
| Entering wrong letter to guess the word | If wrong letter is guessed, error message will be displayed, Hangman figure will be displayed | Entering a letter | If letter is wrong, error message will be displayed and hangman figure will be updated | Pass |
| Validation for letter input | Displaying error message when entering something other than 1 letter at a time | Entering more than 1 letter, whitespaces, numbers | Error message displays | Pass |
| Winning the Game | If word is guessed correctly, Game Won insert will be displayed and a Menu will open | Guessing the word correctly | Game Won insert displays and menu opens | Pass |
| Losing the Game | If word wasn't guessd, Game Over will be displayed and Game Over menu opens | Loosing the game | Game Over insert will be displayed and menu opens | Pass |

- **Game Won Display**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Game Won display with features | Score will be displayed and a Menu with options what to do next | Winning the game and seeing the menu | Score is displayed and menu will show underneath | Pass |
| Score will be displayed with a message for the user | Score will be calculated and score will be displayed | Finishing the game | Score is calulated correctly and displayed | Pass |
| Pressing 1 to add score to Scoreboard | Program will ask for Username | Enter 1 | Program asks for username with validation, no more than 12 letters and letters only | Pass |
| Pressing 2 to play again | Category sections opens for user | Enter 2 | Category selection opens | Pass |
| Pressing 3 to exit the program | Program closes | Enter 3 | Program closes | Pass |
| Validation for input | Displaying error message when entering something other than numbers beetween 1-3 | Entering letters, whitespaces, higher numbers | Error message displays | Pass |


- **Game Over Display**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Game Over display with features | Game Over with the game word will be displayed and options what to do next | Loosing the game | Game over display with menu underneath | Pass |
| Pressing 1 to play again | Category sections opens for user | Enter 1 | Category selection opens | Pass |
| Pressing 2 to get back to main menu | Return to main menu | Enter 2 | Returns to main menu | Pass |
| Pressing 3 to exit the program | Program closes | Enter 3 | Program closes | Pass |
| Validation for input | Displaying error message when entering something other than numbers beetween 1-3 | Entering letters, whitespaces, higher numbers | Error message displays | Pass |
