# 🔐 Day 15 - Login System with Username and Password

## 📖 Description

This Python program simulates a simple login system.

The user has **3 attempts** to enter the correct username and password. If both credentials are correct, the login is successful and the program stops. If all three attempts fail, the program displays a final message.

---

## 🚀 Features

- Takes username and password as input
- Allows up to 3 login attempts
- Verifies both username and password
- Uses `break` to stop the loop after a successful login
- Uses `for...else` to detect when all attempts are used

---

## 🛠️ Concepts Used

- Variables
- input()
- for loop
- if-else
- Comparison Operator (`==`)
- Logical Operator (`and`)
- break
- for...else
- f-strings

---

## 💻 Code

```python
username = "sai-eswar"
password = "220"

for i in range(3):
    u = input("Enter Username : ")
    p = input("Enter Password : ")

    if u == username and p == password:
        print("Login Successfully")
        break
    else:
        print(f"Attempt {i + 1} failed.")
        print("Login Failed!")

else:
    print("Your 3 attempts are finished")
```

---

## ▶️ Sample Output

### Successful Login

```
Enter Username : sai-eswar
Enter Password : 220

Login Successfully
```

### Failed Login

```
Enter Username : sai
Enter Password : 123

Attempt 1 failed.
Login Failed!

Enter Username : sai
Enter Password : 123

Attempt 2 failed.
Login Failed!

Enter Username : sai
Enter Password : 123

Attempt 3 failed.
Login Failed!

Your 3 attempts are finished
```

---

## 📚 What I Learned

- How to validate username and password
- How to use the `and` operator
- How to repeat login attempts using a loop
- How `break` stops a loop
- How `for...else` works

---

## 📅 100 Days of Python Challenge

**Day 15 Completed ✅**

Keep learning, keep building, and improve every day! 🚀