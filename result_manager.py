from config import (
    STUDENT_FILE,
    RESULT_FILE,
    SUBJECTS
)

from storage import load_data, save_data

from utils import (
    generate_id,
    find_by_id,
    calculate_result
)


def enter_marks():
    students = load_data(STUDENT_FILE)
    results = load_data(RESULT_FILE)

    if not students:
        print("Please add students first.")
        return

    student_id = input("Enter Student ID: ").strip()

    student = find_by_id(students, student_id)

    if not student:
        print("Student not found.")
        return

    existing_result = None

    for result in results:
        if result["student_id"] == student["id"]:
            existing_result = result
            break

    if existing_result:
        print("Result already exists for this student.")
        print("Use update marks instead.")
        return

    marks = {}

    print("\nEnter marks out of 100")

    for subject in SUBJECTS:
        while True:
            try:
                mark = float(
                    input(f"{subject}: ")
                )

                if 0 <= mark <= 100:
                    marks[subject] = mark
                    break

                print("Marks must be between 0 and 100.")

            except ValueError:
                print("Enter a valid number.")

    summary = calculate_result(marks)

    result = {
        "id": generate_id(results, "R"),
        "student_id": student["id"],
        "student_name": student["name"],
        "roll_number": student["roll_number"],
        "marks": marks,
        **summary
    }

    results.append(result)

    save_data(RESULT_FILE, results)

    print("\nResult saved successfully.")
    display_result(result)


def display_result(result):
    print("\n" + "=" * 60)
    print("STUDENT RESULT")
    print("=" * 60)

    print(f"Student : {result['student_name']}")
    print(f"Roll No : {result['roll_number']}")
    print("-" * 60)

    for subject, marks in result["marks"].items():
        print(f"{subject:<25} {marks:>6.2f}")

    print("-" * 60)
    print(f"Total      : {result['total']}/{result['maximum']}")
    print(f"Percentage : {result['percentage']}%")
    print(f"Grade      : {result['grade']}")
    print(f"Status     : {result['status']}")


def view_result():
    results = load_data(RESULT_FILE)

    student_id = input("Enter Student ID: ").strip()

    result = None

    for item in results:
        if item["student_id"].lower() == student_id.lower():
            result = item
            break

    if not result:
        print("Result not found.")
        return

    display_result(result)


def update_marks():
    results = load_data(RESULT_FILE)

    student_id = input("Enter Student ID: ").strip()

    result = None

    for item in results:
        if item["student_id"].lower() == student_id.lower():
            result = item
            break

    if not result:
        print("Result not found.")
        return

    print("\nUpdate Marks")

    for subject in SUBJECTS:
        while True:
            try:
                mark = float(
                    input(
                        f"{subject} "
                        f"(Current: {result['marks'][subject]}): "
                    )
                )

                if 0 <= mark <= 100:
                    result["marks"][subject] = mark
                    break

                print("Marks must be between 0 and 100.")

            except ValueError:
                print("Enter a valid number.")

    summary = calculate_result(result["marks"])

    result.update(summary)

    save_data(RESULT_FILE, results)

    print("Marks updated successfully.")

    display_result(result)


def delete_result():
    results = load_data(RESULT_FILE)

    student_id = input("Enter Student ID: ").strip()

    result = None

    for item in results:
        if item["student_id"].lower() == student_id.lower():
            result = item
            break

    if not result:
        print("Result not found.")
        return

    results.remove(result)

    save_data(RESULT_FILE, results)

    print("Result deleted successfully.")
