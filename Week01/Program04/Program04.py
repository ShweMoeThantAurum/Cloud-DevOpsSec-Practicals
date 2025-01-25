# Question 4
# Think about a game that you like to play, implement a program that will allow you to play the game from the terminal.

import random

def main():
    print("Welcome to the Higher or Lower game!")
    print("Guess if the next number will be higher or lower.")
    print("Type 'h' for higher, 'l' for lower, or 'q' to quit.\n")

    # Initialize game state
    current_number = random.randint(1, 100)
    score = 0

    while True:
        print(f"Current number: {current_number}")
        guess = input("Will the next number be higher (h) or lower (l)? ").strip().lower()

        # Check for quit option
        if guess == 'q':
            print("Thanks for playing!")
            print(f"Your final score: {score}")
            break

        # Generate the next random number
        next_number = random.randint(1, 100)

        # Compare the numbers based on the user's guess
        if (guess == 'h' and next_number > current_number) or (guess == 'l' and next_number < current_number):
            score += 1
            print(f"Correct! The next number was {next_number}.")
            current_number = next_number  # Update the current number
        else:
            print(f"Wrong! The next number was {next_number}.")
            print(f"Game over! Your final score is: {score}")
            break

main()