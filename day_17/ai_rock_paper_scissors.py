import random
import time
items = ["rock", "scissor", "paper"]
name = input("Enter your name : ").upper()
print(f"WELCOME {name}. ")

print("AI IS ACTIVATING..")
scan = int(input("Enter how many seconds to take ai : "))
for i in range(scan, 0, -1):
    print(i)
    time.sleep(1)


print("AI ACTIVATED...")

while True:


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
    again = input("Play again? (yes/no): ").lower()
    if again != "yes":
        print(f"THANK YOU {name} FOR PLAYING THIS GAME.")
        break

         
