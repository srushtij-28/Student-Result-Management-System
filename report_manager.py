from config import RESULT_FILE
from storage import load_data


def class_statistics():
    results = load_data(RESULT_FILE)

    if not results:
        print("No results available.")
        return

    total_students = len(results)

    passed = sum(
        1
        for result in results
        if result["status"] == "Pass"
    )

    failed = total_students - passed

    average_percentage = (
        sum(result["percentage"] for result in results)
        / total_students
    )

    highest = max(
        results,
        key=lambda result: result["percentage"]
    )

    lowest = min(
        results,
        key=lambda result: result["percentage"]
    )

    print("\n" + "=" * 60)
    print("CLASS STATISTICS")
    print("=" * 60)

    print(f"Total Students       : {total_students}")
    print(f"Passed Students      : {passed}")
    print(f"Failed Students      : {failed}")
    print(f"Average Percentage   : {average_percentage:.2f}%")

    print(
        f"Highest Percentage   : "
        f"{highest['student_name']} "
        f"({highest['percentage']}%)"
    )

    print(
        f"Lowest Percentage    : "
        f"{lowest['student_name']} "
        f"({lowest['percentage']}%)"
    )


def subject_report():
    results = load_data(RESULT_FILE)

    if not results:
        print("No results available.")
        return

    print("\n" + "=" * 60)
    print("SUBJECT AVERAGE REPORT")
    print("=" * 60)

    subjects = results[0]["marks"].keys()

    for subject in subjects:
        total = sum(
            result["marks"][subject]
            for result in results
        )

        average = total / len(results)

        print(
            f"{subject:<25}: "
            f"{average:.2f}"
        )


def topper_list():
    results = load_data(RESULT_FILE)

    if not results:
        print("No results available.")
        return

    sorted_results = sorted(
        results,
        key=lambda result: result["percentage"],
        reverse=True
    )

    print("\n" + "=" * 60)
    print("TOP STUDENTS")
    print("=" * 60)

    for position, result in enumerate(
        sorted_results[:5],
        start=1
    ):
        print(
            f"{position}. "
            f"{result['student_name']} - "
            f"{result['percentage']}% - "
            f"Grade {result['grade']}"
        )
