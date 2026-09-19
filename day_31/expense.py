import json

expenses = []


def add_expense():
    amount = float(input("Enter expense amount: "))
    category = input("Enter expense category: ")

    expense = {
        "amount": amount,
        "category": category
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully!")


def view_expenses():

    if not expenses:
        print("No expenses found.")
        return

    print("\n===== YOUR EXPENSES =====")

    for i, expense in enumerate(expenses, start=1):
        print(f"{i}. ₹{expense['amount']} - {expense['category']}")


def calculate_total():

    total = 0

    for expense in expenses:
        total = total + expense["amount"]

    print("Total Expense: ₹", total)


def highest_expense():

    if not expenses:
        print("No expenses found.")
        return

    highest = expenses[0]

    for expense in expenses:
        if expense["amount"] > highest["amount"]:
            highest = expense

    print("\n===== HIGHEST EXPENSE =====")
    print("Amount:", highest["amount"])
    print("Category:", highest["category"])


def delete_expense():

    if not expenses:
        print("No expenses found.")
        return

    view_expenses()

    number = int(input("Enter expense number to delete: "))

    if 1 <= number <= len(expenses):
        deleted_expense = expenses.pop(number - 1)

        save_expenses()

        print("Deleted:", deleted_expense)

    else:
        print("Invalid expense number.")


def load_expenses():

    global expenses

    try:
        with open("expenses.json", "r") as file:
            expenses = json.load(file)

    except FileNotFoundError:
        expenses = []


def save_expenses():

    with open("expenses.json", "w") as file:
        json.dump(expenses, file)

    print("Expenses saved successfully!")