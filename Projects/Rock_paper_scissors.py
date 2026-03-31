import random

user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

possible_choices = ["rock", "paper", "scissors"]
computer_choice = random.choice(possible_choices)
print(f"You chose: {user_choice}, Computer chose: {computer_choice}")

if user_choice == computer_choice:
    print("It's a tie!")
elif (user_choice == "rock" and computer_choice == "scissors") or \
	 (user_choice == "paper" and computer_choice == "rock") or \
	 (user_choice == "scissors" and computer_choice == "paper"):
    print("You win!")
else:
    print("You lose!")
print("Do you want to play again? (yes/no)")
play_again = input().lower()
if play_again == "yes":
	# Restart the game
	exec(open(__file__).read())
     