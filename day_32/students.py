import json

students = []


# Add a student
def add_student():
    try:
        name = input("Enter student name: ").strip()

        if not name:
            print("Student name cannot be empty.")
            return

        marks = float(input("Enter student marks: "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        student = {
            "name": name,
            "marks": marks
        }

        students.append(student)
        save_students()

        print("Student added successfully!")

    except ValueError:
        print("Please enter valid marks.")


# View all students
def view_students():
    if not students:
        print("No students found.")
        return

    print("\n===== STUDENT DETAILS =====")

    for i, student in enumerate(students, start=1):
        print(
            f"{i}. Name: {student['name']} "
            f"| Marks: {student['marks']}"
        )


# Calculate average marks
def calculate_average():
    if not students:
        print("No students found.")
        return

    marks = [student["marks"] for student in students]

    average = sum(marks) / len(marks)

    print("Average Marks:", round(average, 2))


# Find passed students
def passed_students():
    passed = list(
        filter(lambda student: student["marks"] >= 40, students)
    )

    if not passed:
        print("No students passed.")
        return

    print("\n===== PASSED STUDENTS =====")

    for student in passed:
        print(f"{student['name']} - {student['marks']}")


# Find the topper
def find_topper():
    if not students:
        print("No students found.")
        return

    topper = max(
        students,
        key=lambda student: student["marks"]
    )

    print("\n===== CLASS TOPPER =====")
    print("Name:", topper["name"])
    print("Marks:", topper["marks"])


# Create a dictionary of student names and marks
def student_marks_summary():
    if not students:
        print("No students found.")
        return

    summary = {
        student["name"]: student["marks"]
        for student in students
    }

    print("\n===== STUDENT MARKS SUMMARY =====")
    print(summary)


# Display names and marks using zip()
def display_names_and_marks():
    if not students:
        print("No students found.")
        return

    names = [student["name"] for student in students]
    marks = [student["marks"] for student in students]

    print("\n===== STUDENT RESULTS =====")

    for name, mark in zip(names, marks):
        print(f"{name} scored {mark}")


# Save student data to JSON
def save_students():
    with open("students.json", "w", encoding="utf-8") as file:
        json.dump(students, file, indent=4)


# Load student data from JSON
def load_students():
    global students

    try:
        with open("students.json", "r", encoding="utf-8") as file:
            students = json.load(file)

        if not isinstance(students, list):
            print("Invalid student data format. Starting with an empty list.")
            students = []

    except FileNotFoundError:
        students = []

    except json.JSONDecodeError:
        print("Student data file is invalid. Starting with an empty list.")
        students = []