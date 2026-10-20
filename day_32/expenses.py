import json
from datetime import date, datetime
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent / "expenses.json"

expenses = []



def add_expense():
    try:
        amount = float(input("Enter expense amount: "))

        if amount <= 0:
            print("Amount must be greater than 0.")
            return

    except ValueError:
        print("Please enter a valid amount.")
        return

    category = input("Enter expense category: ").strip()

    if not category:
        print("Category cannot be empty.")
        return

    expense_date = input(
        "Enter expense date (YYYY-MM-DD), "
        "or press Enter for today: "
    ).strip()

    if not expense_date:
        expense_date = date.today().isoformat()

    else:
        try:
            expense_date = datetime.strptime(
                expense_date, "%Y-%m-%d"
            ).date().isoformat()

        except ValueError:
            print("Invalid date. Use YYYY-MM-DD.")
            return

    expense = {
        "amount": amount,
        "category": category,
        "date": expense_date
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully!")
    print(f"Date: {expense_date}")



def view_expenses():
    if not expenses:
        print("No expenses found.")
        return

    print("\n===== EXPENSE DETAILS =====")

    for i, expense in enumerate(expenses, start=1):
        expense_date = expense.get(
            "date", "Date unavailable"
        )

        print(
            f"{i}. ₹{expense['amount']:.2f} "
            f"| Category: {expense['category']} "
            f"| Date: {expense_date}"
        )



def calculate_expense_total():
    if not expenses:
        print("No expenses found.")
        return

    total = sum(
        expense["amount"]
        for expense in expenses
    )

    print(f"Total Expenses: ₹{total:.2f}")



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
    print("Date:", highest.get("date", "Date unavailable"))



def delete_expense():
    if not expenses:
        print("No expenses found.")
        return

    view_expenses()

    try:
        number = int(
            input("Enter expense number to delete: ")
        )

        if not 1 <= number <= len(expenses):
            print("Invalid expense number.")
            return

        deleted = expenses.pop(number - 1)

        save_expenses()

        print("Expense deleted successfully!")
        print("Deleted expense:", deleted)

    except ValueError:
        print("Please enter a valid number.")


def calculate_total(*args):
    return sum(args)



def search_expenses_by_category():
    if not expenses:
        print("No expenses found.")
        return

    search_category = input(
        "Enter category to search: "
    ).strip()

    if not search_category:
        print("Category cannot be empty.")
        return

    matching_expenses = [
        expense
        for expense in expenses
        if expense["category"].strip().casefold()
        == search_category.casefold()
    ]

    if not matching_expenses:
        print("No expenses found in this category.")
        return

    print("\n===== EXPENSES BY CATEGORY =====")

    for i, expense in enumerate(matching_expenses, start=1):
        print(
            f"{i}. ₹{expense['amount']:.2f} "
            f"| Category: {expense['category']} "
            f"| Date: {expense.get('date', 'Date unavailable')}"
        )

    total = sum(
        expense["amount"]
        for expense in matching_expenses
    )

    print(
        f"\nTotal {search_category} Expenses: "
        f"₹{total:.2f}"
    )



def category_wise_expenses():
    if not expenses:
        print("No expenses found.")
        return

    category_totals = {}

    for expense in expenses:
        category = expense["category"].strip().title()
        amount = expense["amount"]

        category_totals[category] = (
            category_totals.get(category, 0) + amount
        )

    print("\n===== CATEGORY-WISE EXPENSE REPORT =====")

    for category, total in sorted(category_totals.items()):
        print(f"{category}: ₹{total:.2f}")

    overall_total = sum(category_totals.values())

    print("---------------------------------------")
    print(f"Total Expenses: ₹{overall_total:.2f}")
    print(f"Number of Categories: {len(category_totals)}")



def monthly_expense_report():
    if not expenses:
        print("No expenses found.")
        return

    month_input = input(
        "Enter month (YYYY-MM), or press Enter for current month: "
    ).strip()

    if not month_input:
        month_input = date.today().strftime("%Y-%m")

    try:
        selected_month = datetime.strptime(
            month_input, "%Y-%m"
        ).strftime("%Y-%m")

    except ValueError:
        print("Invalid month. Use YYYY-MM, for example 2026-10.")
        return

    monthly_categories = {}
    skipped_records = 0

    for expense in expenses:
        expense_date = expense.get("date")

       
        if not expense_date:
            skipped_records += 1
            continue

        try:
            parsed_date = date.fromisoformat(expense_date)

        except (ValueError, TypeError):
            skipped_records += 1
            continue

        if parsed_date.strftime("%Y-%m") == selected_month:
            category = expense["category"].strip().title()

            monthly_categories[category] = (
                monthly_categories.get(category, 0)
                + expense["amount"]
            )

    print("\n===== MONTHLY EXPENSE REPORT =====")
    print("Month:", selected_month)

    if not monthly_categories:
        print("No dated expenses found for this month.")
    else:
        for category, total in sorted(monthly_categories.items()):
            print(f"{category}: ₹{total:.2f}")

        monthly_total = sum(monthly_categories.values())

        print("---------------------------------")
        print(f"Monthly Total: ₹{monthly_total:.2f}")
        print(f"Categories: {len(monthly_categories)}")

    if skipped_records:
        print(
            f"Note: {skipped_records} expense record(s) "
            "were skipped because their dates are missing or invalid."
        )


def save_expenses():
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(expenses, file, indent=4)

    except OSError as error:
        print(f"Could not save expense data: {error}")


def load_expenses():
    global expenses

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Invalid expense data format.")
            expenses = []
            return

        valid_expenses = []

        for expense in data:
            if not isinstance(expense, dict):
                continue

            amount = expense.get("amount")
            category = expense.get("category")

            if (
                isinstance(amount, bool)
                or not isinstance(amount, (int, float))
                or amount <= 0
                or not isinstance(category, str)
                or not category.strip()
            ):
                continue

       
            saved_expense = {
                "amount": amount,
                "category": category
            }

            if "date" in expense:
                saved_expense["date"] = expense["date"]

            valid_expenses.append(saved_expense)

        expenses = valid_expenses

        if len(expenses) != len(data):
            print("Some invalid expense records were ignored.")

    except FileNotFoundError:
        expenses = []

    except json.JSONDecodeError:
        print("Expense data file contains invalid JSON.")
        expenses = []

    except OSError as error:
        print(f"Could not load expense data: {error}")
        expenses = []