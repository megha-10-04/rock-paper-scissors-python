import random


def display_menu():
    """Displays game instructions."""
    print("\n Rock Paper Scissors Game")
    print("Choices: rock, paper, scissors")
    print("Type 'exit' to quit the game\n")


def get_user_choice():
    """Gets and validates user input."""
    while True:
        choice = input("Enter your choice: ").lower()
        if choice in ["rock", "paper", "scissors", "exit"]:
            return choice
        print(" Invalid input. Please choose rock, paper, or scissors.")


def get_computer_choice():
    """Returns a random choice for the computer."""
    return random.choice(["rock", "paper", "scissors"])


def decide_winner(user, computer):
    """Determines the winner of the round."""
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "win"
    else:
        return "loss"


def display_score(score):
    """Displays the current score."""
    print("\n Scoreboard")
    print(f"Wins: {score['wins']} | Losses: {score['losses']} | Ties: {score['ties']}\n")


def play_game():
    """Main game loop."""
    score = {"wins": 0, "losses": 0, "ties": 0}
    display_menu()

    while True:
        user_choice = get_user_choice()

        if user_choice == "exit":
            print("\n Thanks for playing!")
            display_score(score)
            break

        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        result = decide_winner(user_choice, computer_choice)

        if result == "win":
            print(" You win this round!")
            score["wins"] += 1
        elif result == "loss":
            print(" Computer wins this round!")
            score["losses"] += 1
        else:
            print(" It's a tie!")
            score["ties"] += 1

        display_score(score)


# Run the game
if __name__ == "__main__":
    play_game()
