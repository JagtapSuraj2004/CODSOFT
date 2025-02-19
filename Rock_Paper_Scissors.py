import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "Computer wins!"

def main():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock-Paper-Scissors Game")
        print("1. Play Rock-Paper-Scissors")
        print("2. Check Score")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            user_choice = input("Enter rock, paper, or scissors: ").lower()
            if user_choice not in ["rock", "paper", "scissors"]:
                print("Invalid choice! Please enter rock, paper, or scissors.")
                continue

            computer_choice = get_computer_choice()
            print(f"Computer chose: {computer_choice}")

            result = determine_winner(user_choice, computer_choice)
            print(result)

            if result == "You win!":
                user_score += 1
            elif result == "Computer wins!":
                computer_score += 1

        elif choice == "2":
            print(f"Your score: {user_score}")
            print(f"Computer's score: {computer_score}")

        elif choice == "3":
            print("Thanks for playing! Goodbye!")
            break

        else:
            print("Invalid choice! Please enter 1, 2, or 3.")

if __name__ == '__main__':
    main()