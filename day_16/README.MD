# 🎲 Day 16 - Random Username Generator

## 📖 Description

This Python program generates random username suggestions based on the user's name.

The user enters their name and chooses how many usernames they want. The program combines the name with a random style and a random number to create unique usernames.

---

## 🚀 Features

- Takes the user's name as input
- Lets the user choose how many usernames to generate
- Uses random words and numbers
- Generates unique username suggestions
- Uses Python's `random` module

---

## 🛠️ Concepts Used

- Variables
- Lists
- input()
- for loop
- range()
- random.choice()
- random.randint()
- f-strings

---

## 💻 Code

```python
import random

name = input("Enter your name : ")

vibes = ["cool", "pro", "soft", "introvert", "x_x", "$##"]

count = int(input("How many usernames do you want? "))

for i in range(count):
    username = f"{name}{random.choice(vibes)}{random.randint(1,99)}"
    print(username)
```

---

## ▶️ Sample Output

```
Enter your name : Eswar
How many usernames do you want? 5

Eswarcool24
Eswarpro81
Eswarsoft15
Eswarintrovert63
Eswarx_x42
```

---

## 📚 What I Learned

- How to import and use the `random` module
- How to use `random.choice()` to select a random item from a list
- How to use `random.randint()` to generate random numbers
- How to use f-strings
- How to use loops for repeated output
- How to create dynamic programs using user input

---

### 📅 100 Days of Python Challenge

**Day 16 Completed ✅**