import random

name = input("Please provide your name: ")
print(f"Hello {name}, welcome to the number guessing game")

# Input validation loop for 'yes' or 'no'
while True:
    decision = input("Do you want to continue? (yes/no): ").strip().lower()
    if decision in ["yes", "no"]:
        break
    else:
        print("Invalid input. Please type 'yes' or 'no'.")

# Start game only if decision is 'yes'
if decision == "yes":
    print("I am thinking of a number between 1 and 20")
    secret_number = random.randint(1, 20)
    attempts = 0
    guess_limit = 5

    while attempts < guess_limit:
        try:
            user_input = int(input("Please guess the number: "))
            attempts += 1
            if user_input < secret_number:
                print("Your guess is too low.")
            elif user_input > secret_number:
                print("Your guess is too high.")
            else:
                print(f"You guessed the number correctly after {attempts} attempt(s). Congratulations!")
                break
        except ValueError:
            print("Please enter a valid number.")

    if attempts == guess_limit and user_input != secret_number:
        print(f"Sorry, you've used all your attempts. The correct number was {secret_number}.")

#  Exit message only if player said no
else:
    print("Goodbye!")
