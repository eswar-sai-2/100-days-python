import json
from pathlib import Path


DATA_FILE = Path(__file__).resolve().parent / "students.json"

students = []



def add_student():
    name = input("Enter student name: ").strip()

    if not name:
        print("Student name cannot be empty.")
        return

    try:
        marks = float(input("Enter student marks (0-100): "))

        if not 0 <= marks <= 100:
            print("Marks must be between 0 and 100.")
            return

    except ValueError:
        print("Please enter valid marks.")
        return

    student = {
        "name": name,
        "marks": marks
    }

    students.append(student)
    save_students()

    print("Student added successfully!")



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


def search_student():
    if not students:
        print("No students found.")
        return

    search_name = input(
        "Enter student name to search: "
    ).strip()

    if not search_name:
        print("Student name cannot be empty.")
        return

    found_students = [
        student
        for student in students
        if student["name"].casefold() == search_name.casefold()
    ]

    if not found_students:
        print("Student not found.")
        return

    print("\n===== SEARCH RESULTS =====")

    for student in found_students:
        print("Name:", student["name"])
        print("Marks:", student["marks"])

        if student["marks"] >= 40:
            print("Result: Passed")
        else:
            print("Result: Failed")


def update_student_marks():
    if not students:
        print("No students found.")
        return

    view_students()

    try:
        number = int(
            input("Enter student number to update: ")
        )

        if not 1 <= number <= len(students):
            print("Invalid student number.")
            return

        student = students[number - 1]

        print("\nStudent:", student["name"])
        print("Current Marks:", student["marks"])

        new_marks = float(
            input("Enter new marks (0-100): ")
        )

        if not 0 <= new_marks <= 100:
            print("Marks must be between 0 and 100.")
            return

        student["marks"] = new_marks

        save_students()

        print("Student marks updated successfully!")

    except ValueError:
        print("Please enter valid numbers.")


def sort_students_by_marks():
    if not students:
        print("No students found.")
        return

    sorted_students = sorted(
        students,
        key=lambda student: student["marks"],
        reverse=True
    )

    print("\n===== STUDENTS RANKED BY MARKS =====")

    for rank, student in enumerate(sorted_students, start=1):
        print(
            f"{rank}. {student['name']} - "
            f"{student['marks']}"
        )



def calculate_average():
    if not students:
        print("No students found.")
        return

    marks = [
        student["marks"]
        for student in students
    ]

    average = sum(marks) / len(marks)

    print(f"Average Marks: {average:.2f}")



def passed_students():
    passed = list(
        filter(
            lambda student: student["marks"] >= 40,
            students
        )
    )

    if not passed:
        print("No students passed.")
        return

    print("\n===== PASSED STUDENTS =====")

    for student in passed:
        print(
            f"{student['name']} - "
            f"{student['marks']}"
        )



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



def display_names_and_marks():
    if not students:
        print("No students found.")
        return

    names = [
        student["name"]
        for student in students
    ]

    marks = [
        student["marks"]
        for student in students
    ]

    print("\n===== STUDENT RESULTS =====")

    for name, mark in zip(names, marks):
        print(f"{name} scored {mark}")



def save_students():
    try:
        with DATA_FILE.open("w", encoding="utf-8") as file:
            json.dump(students, file, indent=4)

    except OSError as error:
        print(f"Could not save student data: {error}")


def load_students():
    global students

    try:
        with DATA_FILE.open("r", encoding="utf-8") as file:
            data = json.load(file)

        if not isinstance(data, list):
            print("Invalid student data format.")
            students = []
            return

       
        students = [
            student
            for student in data
            if (
                isinstance(student, dict)
                and isinstance(student.get("name"), str)
                and isinstance(student.get("marks"), (int, float))
                and not isinstance(student.get("marks"), bool)
                and 0 <= student["marks"] <= 100
            )
        ]

        if len(students) != len(data):
            print("Some invalid student records were ignored.")

    except FileNotFoundError:
        students = []

    except json.JSONDecodeError:
        print("Student data file contains invalid JSON.")
        students = []

    except OSError as error:
        print(f"Could not load student data: {error}")
        students = []