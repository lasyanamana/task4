import random

def get_user_choice():
    """Get user input for their choice."""
    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if user_choice in ("rock", "paper", "scissors"):
            return user_choice
        else:
            print("Invalid choice. Please enter rock, paper, or scissors.")

def get_computer_choice():
    """Generate a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    """Determine the winner based on user and computer choices."""
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "Computer wins!"

def play_game():
    """Play a single round of Rock-Paper-Scissors."""
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()

    print(f"You chose {user_choice}.")
    print(f"Computer chose {computer_choice}.")

    result = determine_winner(user_choice, computer_choice)
    print(result)

# Main game loop
while True:
    play_game()
    play_again = input("Play again? (yes/no): ").lower()
    if play_again != "yes":
        break

print("Thanks for playing! Have a great day!")
