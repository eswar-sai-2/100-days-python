import random

items = ["rock", "scissor", "paper"]

computer = random.choice(items)

user = input("Choose one (paper, scissor, rock): ").lower()

if user not in items:
    print("Invalid choice! Please enter rock, paper, or scissor.")

else:
    print("Computer choice is", computer)

    if user == computer:
        print("The match is drawn!")

    elif user == "rock" and computer == "scissor":
        print("You win.")

    elif user == "paper" and computer == "rock":
        print("You win.")

    elif user == "scissor" and computer == "paper":
        print("You win.")

    else:
        print("Computer wins.")