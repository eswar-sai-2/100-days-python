# ✊📄✂️ Day 13 - Rock Paper Scissors Game

## 📖 Description

This is a simple Rock Paper Scissors game built using Python.

The computer randomly chooses **Rock**, **Paper**, or **Scissor**, and the user enters their choice. The program compares both choices and displays the winner. It also checks for invalid user input.

---

## 🚀 Features

- User enters their choice
- Computer selects a random choice
- Determines the winner
- Detects a draw
- Validates user input
- Uses lowercase conversion to handle uppercase input

---

## 🛠️ Concepts Used

- Variables
- Lists
- `import random`
- `random.choice()`
- `input()`
- `.lower()`
- `if`, `elif`, `else`
- Logical operator (`and`)
- Membership operator (`not in`)

---

## 💻 Code

```python
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
```

---

## ▶️ Sample Output

### User Wins

```
Choose one (paper, scissor, rock): rock

Computer choice is scissor

You win.
```

### Draw

```
Choose one (paper, scissor, rock): paper

Computer choice is paper

The match is drawn!
```

### Computer Wins

```
Choose one (paper, scissor, rock): scissor

Computer choice is rock

Computer wins.
```

### Invalid Input

```
Choose one (paper, scissor, rock): banana

Invalid choice! Please enter rock, paper, or scissor.
```

---

## 📚 What I Learned

- How to import Python modules
- How to generate random values using `random.choice()`
- How to use lists
- How to compare multiple conditions using `if`, `elif`, and `else`
- How to use the `and` operator
- How to convert user input to lowercase using `.lower()`
- How to validate user input using `not in`

---

## 🎯 Future Improvements

- Play multiple rounds
- Keep score for user and computer
- Add "Play Again" option
- Display emojis (🪨 📄 ✂️)
- Create a menu-driven game
- Use functions to organize the code

---

### 📅 100 Days of Python Challenge

**Day 13 Completed ✅**

Building Python skills one project at a time. 🚀