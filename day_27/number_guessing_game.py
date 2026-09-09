import random

computer = random.randint(1000, 9999)
attempts = 0
max_attempts = 10

print("Welcome to the 4-Digit Guessing Game!")
print("You have 10 attempts to guess the number.")

while attempts < max_attempts:
    user = int(input("Enter a 4 digit number: "))

    if user < 1000 or user > 9999:
        print("Please enter exactly a 4-digit number.")
        continue

    attempts += 1

    if user == computer:
        print("Correct! 🎉")
        print("You guessed it in", attempts, "attempts.")
        break

    elif user < computer:
        print("Too low! Try again.")

    else:
        print("Too high! Try again.")

    print("Attempts left:", max_attempts - attempts)

else:
    print("\nGame Over!")
    print("The correct number was:", computer)