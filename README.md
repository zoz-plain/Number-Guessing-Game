# Number Guessing Game


## Overview

The **Number Guessing Game** is a fun, interactive game where players try to guess a number that the computer is thinking of between 1 and 100. Players can choose from different difficulty levels, receive hints, and track their high score as they aim to guess the number in as few attempts as possible. The game also features a timer to track how quickly the player can guess the correct number, and it allows for multiple rounds until the player decides to quit.

## Features

- **Difficulty Levels:**
  - Easy: 10 chances to guess
  - Medium: 5 chances to guess
  - Hard: 3 chances to guess
- **Hint System:** 
  - Receive feedback on how far your guess is from the correct number. 
  - "You're far off" for large differences and "You're very close" for small differences.
- **High Score Tracking:** 
  - Keep track of the fewest attempts it takes to guess the number. Try to beat your own record!
- **Timer:** 
  - See how long it takes you to guess the correct number in seconds.
- **Multiple Rounds:** 
  - The game continues until the player decides to quit.

## How to Play

1. Run the Python script.
2. Select your desired difficulty level.
3. Guess the number between 1 and 100.
4. After each guess, the game will tell you if your guess is too high, too low, or correct.
5. Use the provided hints to improve your guesses.
6. Once you win or lose, you can choose to play again or quit the game.
7. Your best score (in terms of attempts) will be displayed after each round.

## Game Flow

1. **Start the game:** The game welcomes you and prompts you to choose a difficulty level.
2. **Make guesses:** You will enter a number, and the game will guide you whether the number is too high or too low. If you're close to the correct answer, you'll get a hint.
3. **Win or lose:** If you guess correctly, you'll win and see how long it took you. If you run out of chances, you'll lose, and the correct number will be revealed.
4. **Play again or quit:** After each round, you can choose to play another round or quit the game.

## Requirements

- **Python 3.x** must be installed to run the game.

## Setup Instructions

1. Clone or download the repository.
2. Open a terminal or command prompt and navigate to the folder containing the script.
3. Run the script using the following command:
   ```bash
   python number_guessing_game.py

## Roadmap Project
You can find the following project idea [here](https://roadmap.sh/projects/number-guessing-game)