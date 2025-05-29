import random

choices = ("rock", "paper", "scissors")  # Tuple of choices for the game


# Function to get player choice
def player_choice():
    choice = input("Please enter your choice:\n"
                   "Rock (R)\n"
                   "Paper (P)\n"
                   "Scissors (S)\n").strip().lower()

    if choice in ['rock', 'r']:
        return 'rock'
    elif choice in ['paper', 'p']:
        return 'paper'
    elif choice in ['scissors', 's']:
        return 'scissors'
    else:
        print("Invalid choice, please try again.\n")
        return player_choice()


# Function to get computer choice
def computer_choice():
    return random.choice(choices)
