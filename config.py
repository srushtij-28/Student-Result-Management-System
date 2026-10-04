import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_DIR = os.path.join(BASE_DIR, "data")

STUDENT_FILE = os.path.join(DATA_DIR, "students.json")
RESULT_FILE = os.path.join(DATA_DIR, "results.json")

SUBJECTS = [
    "Python",
    "Database",
    "Web Technology",
    "Computer Network",
    "Software Engineering"
]

MAX_MARKS = 100
PASS_MARKS = 35
