import random

choices = ["Rock", "Paper", "Scissors"]
choice = int(input("Your choice... Type 0 for Rock, 1 for Paper, 2 for Scissors : "))

if choice < 0 or choice > 2:
    print(f"You entered an invalid choice : {choice}")
    exit(0)

print(f"You chose: {choices[choice]}")

computer_choice = random.randint(0, 2)
print(f"Computer chose: {choices[computer_choice]}")

result = "Lose"

if choice == 0:
    if computer_choice == 0:
        result = "Draw"
    elif computer_choice == 2:
        result = "Win"
elif choice == 1:
    if computer_choice == 1:
        result = "Draw"
    elif computer_choice == 0:
        result = "Win"
elif choice == 2:
    if computer_choice == 2:
        result = "Draw"
    elif computer_choice == 1:
        result = "Win"

print(f"You {result}...")
