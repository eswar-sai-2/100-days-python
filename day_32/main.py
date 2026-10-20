import students
import expenses


def main():
    
    students.load_students()
    expenses.load_expenses()

    while True:
        print("\n================================")
        print("   STUDENT & EXPENSE ANALYZER")
        print("================================")

        print("\n----- STUDENT MANAGEMENT -----")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Update Student Marks")
        print("5. Sort Students by Marks")
        print("6. Calculate Average Marks")
        print("7. Find Passed Students")
        print("8. Find Topper")
        print("9. Student Marks Summary")
        print("10. Display Names and Marks")

        print("\n----- EXPENSE MANAGEMENT -----")
        print("11. Add Expense")
        print("12. View Expenses")
        print("13. Calculate Total Expenses")
        print("14. Find Highest Expense")
        print("15. Delete Expense")
        print("16. Search Expenses by Category")
        print("17. Category-Wise Expense Analysis")
        print("18. Monthly Expense Report")

        print("\n----- OTHER OPTIONS -----")
        print("19. Test *args")
        print("20. Exit")

        choice = input("\nEnter your choice: ").strip()

       
        if choice == "1":
            students.add_student()

        elif choice == "2":
            students.view_students()

        elif choice == "3":
            students.search_student()

        elif choice == "4":
            students.update_student_marks()

        elif choice == "5":
            students.sort_students_by_marks()

        elif choice == "6":
            students.calculate_average()

        elif choice == "7":
            students.passed_students()

        elif choice == "8":
            students.find_topper()

        elif choice == "9":
            students.student_marks_summary()

        elif choice == "10":
            students.display_names_and_marks()

       
        elif choice == "11":
            expenses.add_expense()

        elif choice == "12":
            expenses.view_expenses()

        elif choice == "13":
            expenses.calculate_expense_total()

        elif choice == "14":
            expenses.highest_expense()

        elif choice == "15":
            expenses.delete_expense()

        elif choice == "16":
            expenses.search_expenses_by_category()

        elif choice == "17":
            expenses.category_wise_expenses()

        elif choice == "18":
            expenses.monthly_expense_report()

        
        elif choice == "19":
            result = expenses.calculate_total(100, 200, 300)
            print("Total:", result)

        elif choice == "20":
            print("Thank you for using the application!")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 20.")


if __name__ == "__main__":
    main()