import random

def get_user_choice():
    print("\nChoose one: rock, paper, or scissors")
    user_choice = input("Your choice: ").lower()
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        return None
    return user_choice

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

def display_result(user, computer, winner):
    print(f"\n🧑 You chose: {user}")
    print(f"💻 Computer chose: {computer}")
    if winner == "tie":
        print("🔄 It's a tie!")
    elif winner == "user":
        print("🎉 You win!")
    else:
        print("😔 You lose!")

def main():
    user_score = 0
    computer_score = 0
    round_number = 1

    print("🎮 Welcome to Rock-Paper-Scissors Game!")

    while True:
        print(f"\n--- Round {round_number} ---")
        user_choice = get_user_choice()
        if user_choice is None:
            continue
        
        computer_choice = get_computer_choice()
        winner = determine_winner(user_choice, computer_choice)
        display_result(user_choice, computer_choice, winner)

        if winner == "user":
            user_score += 1
        elif winner == "computer":
            computer_score += 1

        print(f"\n📊 Score => You: {user_score} | Computer: {computer_score}")

        play_again = input("\nPlay another round? (yes/no): ").lower()
        if play_again != "yes":
            print("\nThanks for playing! Final Score:")
            print(f"🧑 You: {user_score} | 💻 Computer: {computer_score}")
            break

        round_number += 1

if __name__ == "__main__":
    main()
