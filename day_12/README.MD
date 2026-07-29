# 🔐 Day 12 - Password Authentication with Multiple Attempts

## 📖 Description

This Python program checks whether the user enters the correct password.

The user gets **3 attempts** to enter the correct password. If the password is correct, access is granted and the program stops. If all attempts are used without entering the correct password, the program displays a message that the limit has been reached.

---

## 🚀 Features

- Accepts password input from the user
- Allows up to **3 login attempts**
- Grants access when the correct password is entered
- Stops the loop using `break`
- Shows remaining attempts after each incorrect password
- Displays a final message when all attempts are exhausted

---

## 🛠️ Concepts Used

- Variables
- `input()`
- `for` loop
- `range()`
- `if-else`
- Comparison Operator (`==`)
- `break`
- `for...else`
- f-strings

---

## 💻 Code

```python
for i in range(3):
    password = input("Enter Password: ")

    if password == "python123":
        print("Welcome Access Granted!")
        break
    else:
        print(f"Wrong password! Try again. Only {2 - i} attempts left.")

else:
    print("Your limit has been reached.")
```

---

## ▶️ Sample Output

### Correct Password

```
Enter Password: python123

Welcome Access Granted!
```

### Incorrect Password

```
Enter Password: abc
Wrong password! Try again. Only 2 attempts left.

Enter Password: hello
Wrong password! Try again. Only 1 attempts left.

Enter Password: test
Wrong password! Try again. Only 0 attempts left.

Your limit has been reached.
```

---

## 📚 What I Learned

- How to use `if` and `else`
- How to compare values using `==`
- How to repeat code using a `for` loop
- How `break` stops a loop immediately
- How `for...else` works
- How to display remaining attempts using f-strings

---

## 🎯 Future Improvements

- Hide password while typing
- Store the password securely
- Allow the user to create a new password
- Add username and password authentication
- Build a simple login system with a database

---

### 📅 100 Days of Python Challenge

**Day 12 Completed ✅**

Learning Python one day at a time. 🚀