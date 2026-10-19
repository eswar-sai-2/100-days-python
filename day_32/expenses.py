import json

expenses = []


# Add an expense
def add_expense():
    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

        category = input("Enter expense category: ").strip()

        if not category:
            print("Category cannot be empty.")
            return

        expense = {
            "amount": amount,
            "category": category
        }

        expenses.append(expense)
        save_expenses()

        print("Expense added successfully!")

    except ValueError:
        print("Please enter a valid amount.")


# View all expenses
def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n===== EXPENSE DETAILS =====")

    for i, expense in enumerate(expenses, start=1):
        print(
            f"{i}. ₹{expense['amount']:.2f} "
            f"| Category: {expense['category']}"
        )


# Calculate total expenses
def calculate_expense_total():
    if not expenses:
        print("No expenses found.")
        return

    total = sum(
        expense["amount"] for expense in expenses
    )

    print(f"Total Expenses: ₹{total:.2f}")


# Find the highest expense
def highest_expense():
    if not expenses:
        print("No expenses found.")
        return

    highest = max(
        expenses,
        key=lambda expense: expense["amount"]
    )

    print("\n===== HIGHEST EXPENSE =====")
    print(f"Amount: ₹{highest['amount']:.2f}")
    print("Category:", highest["category"])


# Delete an expense
def delete_expense():
    if not expenses:
        print("No expenses found.")
        return

    view_expenses()

    try:
        number = int(input("Enter expense number to delete: "))

        if 1 <= number <= len(expenses):
            deleted = expenses.pop(number - 1)

            save_expenses()

            print("Deleted expense:", deleted)

        else:
            print("Invalid expense number.")

    except ValueError:
        print("Please enter a valid number.")


# Demonstrate *args
def calculate_total(*args):
    return sum(args)


# Save expenses to JSON
def save_expenses():
    with open("expenses.json", "w", encoding="utf-8") as file:
        json.dump(expenses, file, indent=4)


# Load expenses from JSON
def load_expenses():
    global expenses

    try:
        with open("expenses.json", "r", encoding="utf-8") as file:
            expenses = json.load(file)

        if not isinstance(expenses, list):
            print("Invalid expense data format. Starting with an empty list.")
            expenses = []

    except FileNotFoundError:
        expenses = []

    except json.JSONDecodeError:
        print("Expense data file is invalid. Starting with an empty list.")
        expenses = []