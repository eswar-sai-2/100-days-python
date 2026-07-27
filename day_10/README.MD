# Day 10 - Random Password Generator

## 📌 Description

This program generates a random password based on the length entered by the user.

## 💻 Program

```python
import random

chars = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+-=[]:*1234567890"

length = int(input("Enter your password length: "))

password = ""

for i in range(length):
    password += random.choice(chars)

print("Generated password is:", password)
```

## 📚 Concepts Learned

- import
- random module
- random.choice()
- User Input
- for loop
- range()
- String Concatenation

## 🎯 Key Takeaways

- `random.choice()` selects one random character.
- `range(length)` repeats the loop according to the user's input.
- `+=` appends each new character to the password.
- User input makes the program dynamic.

⭐ Day 10 of my #100DaysOfPython challenge