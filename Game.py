import random


# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
            (user_choice == "paper" and computer_choice == "rock") or \
            (user_choice == "scissors" and computer_choice == "paper"):
        return "You win!"
    else:
        return "Computer wins!"


# List of possible choices
choices = ["rock", "paper", "scissors"]


# Function to play a single round of the game
def play_round():
    # Ask user for input
    user_choice = input("Enter rock, paper, or scissors: ").lower()

    # Check if user input is valid
    while user_choice not in choices:
        print("Invalid input! Please choose rock, paper, or scissors.")
        user_choice = input("Enter rock, paper, or scissors: ").lower()

    # Computer makes a random choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner and print the result
    result = determine_winner(user_choice, computer_choice)
    print(result)
    return result


# Main game loop
def play_game():
    user_score = 0
    computer_score = 0
    ties = 0
    rounds_played = 0

    print("Welcome to the Rock Paper Scissors Game!")

    while True:
        print("\nStarting a new round!")

        # Play a single round and get the result
        result = play_round()
        rounds_played += 1

        # Update scores based on result
        if result == "You win!":
            user_score += 1
        elif result == "Computer wins!":
            computer_score += 1
        else:
            ties += 1

        # Show current score
        print(f"\nCurrent Score: You: {user_score} | Computer: {computer_score} | Ties: {ties}")

        # Ask if the user wants to play another round
        play_again = input("\nDo you want to play another round? (yes/no): ").lower()
        if play_again != "yes":
            break

    # Game summary after the user decides to quit
    print("\nGame Over!")
    print(f"Total rounds played: {rounds_played}")
    print(f"Your final score: {user_score}")
    print(f"Computer's final score: {computer_score}")
    print(f"Ties: {ties}")

    if user_score > computer_score:
        print("You are the overall winner!")
    elif user_score < computer_score:
        print("Computer is the overall winner!")
    else:
        print("It's a tie overall!")


# Run the game
if __name__ == "__main__":
    play_game()
