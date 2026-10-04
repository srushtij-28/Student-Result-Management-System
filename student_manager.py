from config import STUDENT_FILE
from storage import load_data, save_data
from utils import generate_id, find_by_id


def add_student():
    students = load_data(STUDENT_FILE)

    name = input("Enter student name: ").strip()
    roll_number = input("Enter roll number: ").strip()
    course = input("Enter course: ").strip()
    semester = input("Enter semester: ").strip()

    if not name or not roll_number or not course:
        print("Required fields cannot be empty.")
        return

    for student in students:
        if student["roll_number"].lower() == roll_number.lower():
            print("Roll number already exists.")
            return

    student = {
        "id": generate_id(students, "S"),
        "name": name,
        "roll_number": roll_number,
        "course": course,
        "semester": semester
    }

    students.append(student)

    save_data(STUDENT_FILE, students)

    print("\nStudent added successfully.")
    print(f"Student ID: {student['id']}")


def view_students():
    students = load_data(STUDENT_FILE)

    if not students:
        print("No students found.")
        return

    print("\n" + "=" * 75)
    print("STUDENT LIST")
    print("=" * 75)

    for student in students:
        print(f"ID         : {student['id']}")
        print(f"Name       : {student['name']}")
        print(f"Roll No    : {student['roll_number']}")
        print(f"Course     : {student['course']}")
        print(f"Semester   : {student['semester']}")
        print("-" * 75)


def search_student():
    students = load_data(STUDENT_FILE)

    keyword = input(
        "Enter student ID, name, or roll number: "
    ).strip().lower()

    results = [
        student
        for student in students
        if keyword in student["id"].lower()
        or keyword in student["name"].lower()
        or keyword in student["roll_number"].lower()
    ]

    if not results:
        print("No student found.")
        return

    print("\nSearch Results")

    for student in results:
        print(
            f"{student['id']} | "
            f"{student['name']} | "
            f"Roll: {student['roll_number']} | "
            f"{student['course']}"
        )


def delete_student():
    students = load_data(STUDENT_FILE)

    student_id = input("Enter Student ID: ").strip()

    student = find_by_id(students, student_id)

    if not student:
        print("Student not found.")
        return

    students.remove(student)

    save_data(STUDENT_FILE, students)

    print("Student deleted successfully.")
