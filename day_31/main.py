import expense

expense.load_expenses()

while True:

    print("\n===== EXPENSE TRACKER =====")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Calculate Total")
    print("4. Highest Expense")
    print("5. Delete Expense")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        expense.add_expense()

    elif choice == "2":
        expense.view_expenses()

    elif choice == "3":
        expense.calculate_total()

    elif choice == "4":
        expense.highest_expense()

    elif choice == "5":
        expense.delete_expense()

    elif choice == "6":
        expense.save_expenses()
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice.")