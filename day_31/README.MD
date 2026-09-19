# 💰 Day 31 — Personal Expense Tracker

A beginner-friendly Python Expense Tracker built using **Modules, Functions, JSON, and File Handling**.

## 🚀 Features

- ➕ Add expenses
- 📋 View all expenses
- 💰 Calculate total expenses
- 📈 Find highest expense
- 🗑️ Delete an expense
- 💾 Save expenses to JSON
- 📂 Load saved expenses automatically
- ⚠️ Handle invalid user input

## 🧠 Concepts Learned

- Python Modules
- `import`
- Functions
- Lists
- Dictionaries
- `for` loops
- `enumerate()`
- `if / elif / else`
- Exception Handling
- `try / except`
- JSON
- `json.dump()`
- `json.load()`
- File Handling
- `global` variables

## 📁 Project Structure

day_31/
│
├── main.py
├── expense.py
├── expenses.json
└── README.md

⚙️ How It Works

The project is divided into two Python files.

main.py

Contains the menu and controls the application.

expense.py

Contains the expense-related functions:

add_expense()
view_expenses()
calculate_total()
highest_expense()
delete_expense()
save_expenses()
load_expenses()
JSON Storage

Expenses are stored in:

expenses.json

The program uses:

json.dump()

to save data and:

json.load()

to load saved data.

▶️ Run the Project

Open the terminal inside the day_32 folder and run:

python main.py
📌 Example
===== EXPENSE TRACKER =====
1. Add Expense
2. View Expenses
3. Calculate Total
4. Highest Expense
5. Delete Expense
6. Exit

Enter your choice:
🎯 What I Learned

Through this project, I learned how to divide Python code into modules, store structured data using JSON, handle files, manage user input, and build a small real-world application.