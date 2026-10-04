import os

from config import (
    DATA_DIR,
    STUDENT_FILE,
    RESULT_FILE
)

from storage import save_data

from student_manager import (
    add_student,
    view_students,
    search_student,
    delete_student
)

from result_manager import (
    enter_marks,
    view_result,
    update_marks,
    delete_result
)

from report_manager import (
    class_statistics,
    subject_report,
    topper_list
)


def initialize_files():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)

    files = [
        STUDENT_FILE,
        RESULT_FILE
    ]

    for filename in files:
        if not os.path.exists(filename):
            save_data(filename, [])


def show_menu():
    print("\n")
    print("=" * 60)
    print("       STUDENT RESULT MANAGEMENT SYSTEM")
    print("=" * 60)

    print("\nSTUDENT MANAGEMENT")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Delete Student")

    print("\nRESULT MANAGEMENT")
    print("5. Enter Marks")
    print("6. View Result")
    print("7. Update Marks")
    print("8. Delete Result")

    print("\nREPORTS")
    print("9. Class Statistics")
    print("10. Subject Report")
    print("11. Top Students")

    print("\n12. Exit")

    print("=" * 60)


def main():
    initialize_files()

    while True:
        show_menu()

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_student()

        elif choice == "2":
            view_students()

        elif choice == "3":
            search_student()

        elif choice == "4":
            delete_student()

        elif choice == "5":
            enter_marks()

        elif choice == "6":
            view_result()

        elif choice == "7":
            update_marks()

        elif choice == "8":
            delete_result()

        elif choice == "9":
            class_statistics()

        elif choice == "10":
            subject_report()

        elif choice == "11":
            topper_list()

        elif choice == "12":
            print("Thank you for using Student Result Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
