import gzip
import pickle
import os


def save_data(students, courses, marks):
    data = {
        "students": students,
        "courses": courses,
        "marks": marks
    }

    with gzip.open("students.dat", "wb") as file:
        pickle.dump(data, file)


def load_data():
    if not os.path.exists("students.dat"):
        return [], [], {}

    with gzip.open("students.dat", "rb") as file:
        data = pickle.load(file)

    students = data["students"]
    courses = data["courses"]
    marks = data["marks"]

    return students, courses, marks