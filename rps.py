import random
choices = ["rock", "paper", "scissors"]
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win...!"
    else:
        return "Computer wins!"
while True:
    user_choice = input("Enter your choice (rock/paper/scissors) or 'q' to quit: ").lower()
    if user_choice == 'q':
        break
    if user_choice not in choices:
        print("Invalid choice :( ")
        continue
    computer_choice = random.choice(choices)
    print(f"\nYou chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")
    winner = determine_winner(user_choice, computer_choice)
    print(winner)
print("Thanks for playing!")