# Hangman Game - Testing

![Hangman Game Start PNG](/assets/docs/readme-images/hangman-game-picture.png)

Visit the deployed site: [Hangman Game]([here](https://hangman-project-3-fs-e5867a39357d.herokuapp.com/))


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

I implemented a validator testing for every input the user has to make.

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

    The user can play the game with the first option available for him.
- **I want the site read instructions on how to play.**

    The user can find instructions on how to play in the main menu.
- **I want the program to be easy to navigate and use.**

    The navigation of the program is preety simpli, just used numbers beetween 1-5.
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

- **Main Page**

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| The Site title(hero image) | reloads the website | clicked title(hero image) | Main Page reloads | Pass |
| Input field for username | Username has to be entered to play | enter username | game starts when enter is pressed | Pass |
| Blank Space Validation | User cannot enter white space | pressing spacebar | doesn't register in input field | pass |
| How to play button | Displays the pop-up with the instructions on how to play the game | Clicked on button | Pop-up with instructions on how to play opens | Pass |
| Play button | Opens Pop-up with memory game | Clicked on button | Game starts, only when username is entered | Pass |

- How to Play Pop-up

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| button to return to Main Page | returns to main page | Clicked on button | Returns to Main Page | Pass |

- Memory Game Pop-up

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Alert for entering name | shows up when username is entered and game pop-up opens | enter username and press play | alert shows up in front of memory game | Pass |
| Game itself | Memory cards turning over correctly, if a pair is found cards will stay face up | playing the game | cards are turning over correctly and pairs are staying face up | Pass |
| Moves counter | Moves counter starts with first two cards turned over | turned first two cards over | moves counter starts | Pass |
| Timer | Timer starts with first two cards turned over | turned first two cards over | timer starts | Pass |
| Restart Game button | restarts game | Clicked button | Game restarts | Pass |
| Finished Memory Game so End Game Screen pops-up | End Game Screen with Moves counter and timer shows up, after finishing the game | finding all matching pairs | End Game Screen pops-up | Pass |

- End Game Screen Pop-up

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| End Game Screen with moves and time to bet the game | Display Moves and Time to bet | finished the game | correct moves and time where displayed | Pass |
| Scoreboard button | Opens Scoreboard | Clicked button | Scoreboard opens | Pass |

-Scoreboard

| Feature | Expected Outcome | Testing Performed | Result | Pass/Fail |
| --- | --- | --- | --- | --- |
| Score displayed | If the users move counts is in the top 3, the username and moves will be displayed in descending order | Played 10+ Games and logged a variety of scores | Once 3 Scores where displayed, only scores that were better than the third highest were displayed | Pass |
| Return to Main Page button | Takes the user to the main page | Clicked the button | Takes user to main page | Pass |

