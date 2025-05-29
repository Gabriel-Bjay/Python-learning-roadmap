from tasks import computer_choice, player_choice


def play_rps():
    player = player_choice()
    computer = computer_choice()

    print(f"\nPlayer chose: {player.capitalize()}")
    print(f"Computer chose: {computer.capitalize()}")

    if player == computer:
        print("It's a tie🫡!")
    elif (player == 'rock' and computer == 'scissors') or \
         (player == 'paper' and computer == 'rock') or \
         (player == 'scissors' and computer == 'paper'):
        print("Player wins 😍👍!")
    else:
        print("Computer wins 🙌😒!")


# Optional replay loop
if __name__ == '__main__':
    while True:
        play_rps()
        again = input("\nPlay again? (y/n): ").strip().lower()
        if again != 'y':
            print("\nThanks for playing!😊")
            print("Goodbye!👋")
            break
