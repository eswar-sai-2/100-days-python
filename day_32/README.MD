# 🎓 Student & Expense Analyzer

A Python-based command-line application that combines student record management with personal expense tracking.

This project helps users manage student information, analyze academic performance, record expenses, and generate useful financial reports. It uses JSON files to store data persistently, so records remain available after the application closes.

Built as part of my **100 Days of Python Challenge** to improve my Python programming, problem-solving, and project development skills.

---

## 🚀 Features

### 🎓 Student Management

- ➕ Add new student records
- 📋 View all students
- 🔍 Search students by name
- ✏️ Update student marks
- 🏆 Sort students by marks in descending order
- 📊 Calculate average marks
- ✅ Display passed students
- 🥇 Find the class topper
- 📝 Generate a student marks summary
- 🔗 Display student names and marks using `zip()`

### 💰 Expense Management

- ➕ Add expenses with an amount, category, and date
- 📋 View all recorded expenses
- 💵 Calculate total expenses
- 📈 Find the highest expense
- 🗑️ Delete an expense
- 🔍 Search expenses by category
- 📊 Generate category-wise expense reports
- 📅 Generate monthly expense reports

### 💾 Data Persistence

- Store student records in `students.json`
- Store expense records in `expenses.json`
- Automatically load saved records when the application starts
- Save changes when records are added, updated, or deleted
- Handle older expense records that do not contain dates

### 🛡️ Input Validation and Error Handling

- Validate student names and marks
- Prevent negative or zero expense amounts
- Validate expense categories
- Validate dates using the `YYYY-MM-DD` format
- Handle invalid numeric input
- Handle missing or malformed JSON files

---

## 🛠️ Technologies Used

| Technology            | Purpose                                       |
|---                    |---                                            |
| Python                | Application logic                             |
| JSON                  | Persistent data storage                       |
| `pathlib`             | Reliable file path handling                   |
| `datetime`            | Date validation and monthly reports           |
| `lambda`              | Custom sorting and filtering                  |
| List Comprehensions   | Searching and processing records              |
| `filter()`            | Finding passed students                       |
| `max()`               | Finding the highest marks and expense         |
| `sorted()`            | Ranking students and sorting categories       |
| `zip()`               | Combining student names and marks             |
| `*args`               | Practicing variable-length function arguments |
| Exception Handling    | Handling invalid input and file errors        |

**External libraries required:** None. The application uses Python's standard library.

---

## 📂 Project Structure

```text
day_32/
│
├── main.py
├── students.py
├── expenses.py
├── students.json
├── expenses.json
└── README.md
```

### File Descriptions

| File               | Description                              |
|---                 |---                                       |
| `main.py`          | Main application and interactive menu    |
| `students.py`      | Student management and academic analysis |
| `expenses.py`      | Expense management and financial reports |
| `students.json`    | Persistent student records               |
| `expenses.json`    | Persistent expense records               |
| `README.md`        | Project documentation                    |

The JSON files are created automatically when data is saved for the first time.

---

## ⚙️ Installation and Setup

### Prerequisites

- Python 3.10 or newer recommended
- Visual Studio Code or another Python editor
- Git (optional, for version control)

### Step 1: Clone the Repository

```bash
git clone https://github.com/eswar-sai-2/100-days-python.git
```

### Step 2: Navigate to the Project Folder

```bash
cd 100-days-python/day_32
```

### Step 3: Run the Application

```bash
python main.py
```

On some Windows systems, you may need to use:

```bash
py main.py
```

No third-party packages are required.

---

## 🖥️ Application Menu

When you run the application, the following menu is displayed:

```text
================================
   STUDENT & EXPENSE ANALYZER
================================

----- STUDENT MANAGEMENT -----
1. Add Student
2. View Students
3. Search Student
4. Update Student Marks
5. Sort Students by Marks
6. Calculate Average Marks
7. Find Passed Students
8. Find Topper
9. Student Marks Summary
10. Display Names and Marks

----- EXPENSE MANAGEMENT -----
11. Add Expense
12. View Expenses
13. Calculate Total Expenses
14. Find Highest Expense
15. Delete Expense
16. Search Expenses by Category
17. Category-Wise Expense Analysis
18. Monthly Expense Report

----- OTHER OPTIONS -----
19. Test *args
20. Exit
```

Enter the corresponding option number to perform an operation.

---

## 📊 Example Usage

### 1. Adding a Student

```text
Enter student name: Sai
Enter student marks (0-100): 85
Student added successfully!
```

The student's details are saved in `students.json`.

### 2. Finding the Class Topper

```text
===== CLASS TOPPER =====
Name: Surya
Marks: 92.0
```

The application identifies the student with the highest marks.

### 3. Adding an Expense

```text
Enter expense amount: 200
Enter expense category: Food
Enter expense date (YYYY-MM-DD), or press Enter for today:
Expense added successfully!
Date: 2026-10-20
```

Pressing Enter uses the current date.

### 4. Category-Wise Expense Report

Example:

```text
===== CATEGORY-WISE EXPENSE REPORT =====
Education: ₹500.00
Food: ₹350.00
Travel: ₹600.00
---------------------------------------
Total Expenses: ₹1450.00
Number of Categories: 3
```

The report groups expenses by category and calculates their totals.

### 5. Monthly Expense Report

Enter a month in `YYYY-MM` format.

Example:

```text
Enter month (YYYY-MM), or press Enter for current month: 2026-10
```

The application displays expenses recorded during that month, grouped by category.

---

## 🧠 Python Concepts Practiced

This project demonstrates practical applications of:

- Variables and data types
- Conditional statements and loops
- Functions and modules
- Lists and dictionaries
- List comprehensions
- Lambda functions
- `filter()`, `max()`, `sorted()`, and `zip()`
- Variable-length arguments using `*args`
- JSON serialization and deserialization
- File handling with `pathlib`
- Exception handling using `try` and `except`
- Date parsing and validation
- Searching, sorting, grouping, and aggregation
- Input validation and data persistence

---

## 🎯 Learning Objectives

The main objectives of this project are to:

1. Strengthen Python programming fundamentals.
2. Understand how to divide a project into multiple modules.
3. Practice reading and writing JSON files.
4. Implement CRUD-style operations for student and expense records.
5. Apply Python's built-in functions to real-world problems.
6. Generate useful summaries from stored data.
7. Develop a maintainable command-line application.

---

## 🔮 Future Improvements

Potential future enhancements include:

- [ ] Automated testing using `unittest` or `pytest`
- [ ] Export reports to CSV
- [ ] Visualize expenses using Matplotlib
- [ ] Add expense budgets and spending alerts
- [ ] Add student grades and grade classification
- [ ] Improve the command-line interface
- [ ] Build a web interface using Flask
- [ ] Add database support using SQLite or MySQL

---

## 👨‍💻 Author

**Sai Eswar Vittanala**

B.Tech — Artificial Intelligence and Machine Learning

Aditya University

### GitHub

Explore my projects and Python learning journey:

https://github.com/eswar-sai-2

---

## 📌 Project Information

- **Project Name:** Student & Expense Analyzer
- **Challenge:** 100 Days of Python
- **Day:** 32
- **Language:** Python
- **Application Type:** Command-Line Application
- **Data Storage:** JSON
- **Dependencies:** Python Standard Library

---

## ⭐ Acknowledgment

This project is part of my journey to improve my Python programming skills through hands-on development.

If you find this project useful, consider giving the repository a star!

**Keep learning, keep building, and keep improving! 🚀**