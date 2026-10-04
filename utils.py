def generate_id(items, prefix):
    if not items:
        return f"{prefix}001"

    numbers = []

    for item in items:
        item_id = item.get("id", "")

        if item_id.startswith(prefix):
            try:
                numbers.append(
                    int(item_id[len(prefix):])
                )
            except ValueError:
                pass

    next_number = max(numbers, default=0) + 1

    return f"{prefix}{next_number:03d}"


def find_by_id(items, item_id):
    for item in items:
        if item.get("id", "").lower() == item_id.lower():
            return item

    return None


def calculate_grade(percentage):
    if percentage >= 90:
        return "A+"
    elif percentage >= 80:
        return "A"
    elif percentage >= 70:
        return "B"
    elif percentage >= 60:
        return "C"
    elif percentage >= 50:
        return "D"
    elif percentage >= 35:
        return "E"
    else:
        return "F"


def calculate_result(marks):
    total = sum(marks.values())

    subject_count = len(marks)

    maximum = subject_count * 100

    percentage = (total / maximum) * 100

    passed = all(mark >= 35 for mark in marks.values())

    grade = calculate_grade(percentage)

    status = "Pass" if passed else "Fail"

    return {
        "total": total,
        "maximum": maximum,
        "percentage": round(percentage, 2),
        "grade": grade,
        "status": status
    }
