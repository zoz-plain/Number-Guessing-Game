import time
from random import randint

# High score tracker
high_score = None

def play_game():
    global high_score  # To update the high score across multiple games

    greet_mess = """Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100."""
    print(greet_mess + "\n")

    computer = randint(1, 100)

    # Difficulty level selection
    print("Please select the difficulty level:")
    diff_mess = """1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n"""
    print(diff_mess)

    diff_input = int(input("Enter your choice: "))

    if diff_input == 1:
        chances = 10
        print("Great! You have selected the Easy difficulty level.")
    elif diff_input == 2:
        chances = 5
        print("Great! You have selected the Medium difficulty level.")
    elif diff_input == 3:
        chances = 3
        print("Great! You have selected the Hard difficulty level.")
    else:
        print("Wrong option, exiting.....")
        return  # Exit the current game if wrong input is provided

    # Start the timer
    start_time = time.time()

    print("\nLet's start the game!")

    for i in range(chances):
        guess_input = int(input(f"\nEnter your guess ({i+1}/{chances}): "))

        # Check guess
        if guess_input == computer:
            print("Congratulations! You guessed the correct number!")

            # Calculate time taken to guess
            time_taken = round(time.time() - start_time, 2)
            print(f"You guessed the number in {i+1} attempts and took {time_taken} seconds.")

            # Check if this is a new high score
            if high_score is None or i+1 < high_score:
                high_score = i+1
                print(f"New high score! You guessed the number in {i+1} attempts.")
            else:
                print(f"Your current high score is {high_score} attempts.")

            break
        elif guess_input > computer:
            print(f"Incorrect! The number is less than {guess_input}.")
        elif guess_input < computer:
            print(f"Incorrect! The number is greater than {guess_input}.")

        # Hint system
        difference = abs(guess_input - computer)
        if difference > 20:
            print("Hint: You're far off.")
        elif difference <= 5:
            print("Hint: You're very close!")

    else:
        # If the loop completes without a correct guess
        print(f"Sorry, you've used all your chances. The correct number was {computer}.")

# Main game loop for multiple rounds
while True:
    play_game()

    # Ask if the player wants to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break
