# 📅 Day 11 - To-Do List using Python Lists

## 📖 Description
This is a simple To-Do List program built using Python.

The user enters the number of tasks they want to add, then enters each task one by one. Finally, the program displays all the tasks in a numbered list.

---

## 🚀 Features

- Accepts user input
- Stores tasks in a Python list
- Uses a `for` loop to add tasks
- Uses `append()` to store tasks
- Displays tasks with numbering
- Uses f-strings for formatted output

---

## 🛠️ Concepts Used

- Variables
- Lists
- `input()`
- `int()`
- `for` loop
- `range()`
- `len()`
- `append()`
- Indexing
- f-strings

---

## 💻 Code

```python
tasks = []

n = int(input("Enter your task size: "))

for i in range(n):
    task = input(f"Enter {i + 1} task: ")
    tasks.append(task)

print("\nYOUR TASKS ARE:")

for i in range(len(tasks)):
    print(f"{i + 1}. {tasks[i]}")
```

---

## ▶️ Sample Output

```
Enter your task size: 3

Enter 1 task: Learn Python
Enter 2 task: Complete Assignment
Enter 3 task: Go to shop

YOUR TASKS ARE:

1. Learn Python
2. Complete Assignment
3. Go to shop
```

---

## 📚 What I Learned

- How to create a list
- How to add items using `append()`
- How to use loops with lists
- How to access list elements using indexes
- How to display data in a formatted way using f-strings

---

## 🎯 Future Improvements

- Delete a task
- Update a task
- Mark tasks as completed
- Save tasks to a file
- Build a menu-driven To-Do List application

---

### 📅 100 Days of Python Challenge

**Day 11 Completed ✅**

Keep learning and improving every day! 🚀