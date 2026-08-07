# 🤖 Day 17 - AI Rock Paper Scissors Game

## 📖 Description

This is an improved version of the classic Rock, Paper, Scissors game built using Python.

The game asks the user for their name, activates an AI simulation with a countdown, and lets the user play against the computer. After each round, the user can choose to play again or exit the game.

---

## 🚀 Features

- 👤 User name input
- 🤖 AI activation simulation
- ⏳ Countdown before the game starts
- 🎲 Random computer choice
- 🎮 User vs Computer gameplay
- ✅ Input validation
- 🔁 Play Again option
- 👋 Personalized goodbye message

---

## 🛠️ Concepts Used

- Variables
- Lists
- `input()`
- `print()`
- `if`, `elif`, `else`
- `while` loop
- `for` loop
- `break`
- `random.choice()`
- `time.sleep()`
- String methods (`upper()`, `lower()`)
- f-strings

---

## 💻 Program

```python
import random
import time

items = ["rock", "scissor", "paper"]

name = input("Enter your name: ").upper()
print(f"WELCOME {name}")

print("AI IS ACTIVATING...")
scan = int(input("Enter scanning time (seconds): "))

for i in range(scan, 0, -1):
    print(i)
    time.sleep(1)

print("AI ACTIVATED...")

while True:

    computer = random.choice(items)

    user = input("Choose one (rock, paper, scissor): ").lower()

    if user not in items:
        print("Invalid choice! Please enter rock, paper, or scissor.")

    else:
        print("Computer chose:", computer)

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
```

---

## ▶️ Sample Output

```
Enter your name: Eswar

WELCOME ESWAR

AI IS ACTIVATING...

Enter scanning time (seconds): 3

3
2
1

AI ACTIVATED...

Choose one (rock, paper, scissor): rock

Computer chose: paper

Computer wins.

Play again? (yes/no): no

THANK YOU ESWAR FOR PLAYING THIS GAME.
```

---

## 📚 What I Learned

- How to use the `random` module
- How to create and use lists
- How to use `while` loops
- How to use `for` loops
- How to use `break`
- How to validate user input
- How to build an interactive Python game
- How to simulate AI activation using `time.sleep()`

---

## 🎯 Future Improvements

- 🏆 Add a scoreboard
- 🎮 Best of 3 / Best of 5 mode
- 🎨 Add emojis for Rock, Paper and Scissors
- 🔊 Add sound effects
- 🖥️ Create a graphical interface using Tkinter
- 💾 Save game history to a file

---

## 📅 100 Days of Python Challenge

**Day 17 Completed ✅**

Building one Python program every day and improving my programming skills.

🚀 Happy Coding!