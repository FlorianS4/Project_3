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

First Time User:

- I want to take a Halo Memory Game.

        * The user can play this Halo Memory Game.

- I want the site to be responsive to my device.

        * The user can play the game on whichever device they like.

- I want to play the game whenever, wherever.

        * The user can play the game whenever they like on whichever device they like, as long as they have internet connection.

- I want the website to be easy to navigate.

        * The website layout is structured so it is user friendly, with a common and easy to understand layout. The user can understand the purpose of the website without having to look deeply into it.

Returning User:

- I want to be able to play the game with memory cards in a different order.

        * The user can play the game and every time the memory cards will be shuffeled randomly.

Frequent User:

- I want to be able to see my score to see how I am performing and to beat my old highscore.

        * After completting the game, the score will be added to the scoreboard, where the best 3 tries on the used machine are dispalyed.

### Manual Testing

- Main Page 

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


I also used following sides to test responsivness
- [Responsinator](http://www.responsinator.com/?url=https%3A%2F%2Fflorians4.github.io%2FProject-2-Memory-Game-JS%2Findex.html)
- [Am I Responsive](https://ui.dev/amiresponsive?url=https://florians4.github.io/Project-2-Memory-Game-JS/index.html)