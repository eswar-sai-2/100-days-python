# Day 23 - Password Guessing Simulation 🔐

## 📌 Description

This is my Day 23 Python project from my **100 Days of Python** learning journey.

In this project, I created a simple password guessing simulation using random characters.

The program:
- Takes a password from the user.
- Generates random guesses.
- Checks each guess against the password.
- Continues until the generated guess matches the password.
- Displays a success message when the guess matches.

> ⚠️ This is only a Python learning simulation. It is not intended for attacking or accessing real accounts.

## 🛠️ Concepts Used

- `input()`
- Variables
- Strings
- `while` loop
- `for` loop
- `range()`
- `len()`
- `random.choice()`
- `+=` operator
- `time.sleep()`
- `import`

## 📚 Libraries Used

### `random`
Used to randomly select characters.

### `time`
Used to add a small delay between guesses.

## 💻 Code

```python
import time
import random

password = input("Enter your password.")

chars = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm"

guess = ""

while guess != password:
    guess = ""

    for i in range(len(password)):
        guess += random.choice(chars)

    print("Guessing your password..", guess)
    time.sleep(0.1)

print("\nPassword Cracked!", password)