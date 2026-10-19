import students
import expenses


def main():

    # Load previously saved data
    students.load_students()
    expenses.load_expenses()

    while True:

        print("\n================================")
        print("   STUDENT & EXPENSE ANALYZER")
        print("================================")

        print("\n----- STUDENT MANAGEMENT -----")
        print("1. Add Student")
        print("2. View Students")
        print("3. Calculate Average Marks")
        print("4. Find Passed Students")
        print("5. Find Topper")
        print("6. Student Marks Summary")
        print("7. Display Names and Marks")

        print("\n----- EXPENSE MANAGEMENT -----")
        print("8. Add Expense")
        print("9. View Expenses")
        print("10. Calculate Total Expenses")
        print("11. Find Highest Expense")
        print("12. Delete Expense")

        print("\n----- OTHER OPTIONS -----")
        print("13. Test *args")
        print("14. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            students.add_student()

        elif choice == "2":
            students.view_students()

        elif choice == "3":
            students.calculate_average()

        elif choice == "4":
            students.passed_students()

        elif choice == "5":
            students.find_topper()

        elif choice == "6":
            students.student_marks_summary()

        elif choice == "7":
            students.display_names_and_marks()

        elif choice == "8":
            expenses.add_expense()

        elif choice == "9":
            expenses.view_expenses()

        elif choice == "10":
            expenses.calculate_expense_total()

        elif choice == "11":
            expenses.highest_expense()

        elif choice == "12":
            expenses.delete_expense()

        elif choice == "13":
            result = expenses.calculate_total(100, 200, 300)
            print("Total:", result)

        elif choice == "14":
            print("Thank you for using the application!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()