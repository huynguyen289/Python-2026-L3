import gzip
import pickle
import os
import zipfile
import csv
import pandas as po


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

from domains.student import Student
from domains.course import Course


def load_students():
    students = []

    try:
        with open("students.txt", "r") as file:
            for line in file:
                student_id, name, dob = line.strip().split(",")

                students.append(
                    Student(student_id, name, dob)
                )

    except FileNotFoundError:
        pass

    return students

def load_courses():
    courses = []

    try:
        with open("courses.txt", "r") as file:
            for line in file:
                course_id, course_name = line.strip().split(",")

                courses.append(
                    Course(course_id, course_name, credits)
                )

    except FileNotFoundError:
        pass

    return courses

def load_marks():
    marks = {}

    try:
        with open("marks.txt", "r") as file:
            for line in file:
                course_id, student_id, mark = line.strip().split(",")
                if course_id not in marks:
                    marks[course_id] = {}

                marks[course_id][student_id] = float(mark)
    except FileNotFoundError:
        pass
    return marks

def compress_data():
    files = [
        "students.txt",
        "courses.txt",
        "marks.txt"
    ]

    with zipfile.ZipFile("students.dat", "w") as zip_file:
        for file_name in files:
            if os.path.exists(file_name):
                zip_file.write(file_name)

def decompress_data():
    if os.path.exists("students.dat"):
        if zipfile.is_zipfile("students.dat"):
            with zipfile.ZipFile("students.dat", "r") as zip_file:
                zip_file.extractall()

def export_to_csv(students):
    with open("students.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["id", "name", "dob"])

        for student in students:
            writer.writerow([student.id, student.name, student.dob])

def export_courses_to_csv(courses):
    with open("courses.csv", "w", newline="") as file:
        writer = csv.writer(file) 
        writer.writerow(["id", "name", "credits"]) 

        for course in courses:
            writer.writerow([course.id, course.name, course.credits])

def export_marks_to_csv(marks):
    with open("marks.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["course_id", "student_id", "marks"])

        for course_id in marks:
            for student_id in marks[course_id]:
                writer.writerow([course_id, student_id, marks[course_id][student_id]])

def load_students_dataframe():
    return po.read_csv("students.csv")

def load_courses_dataframe():
    return po.read_csv("courses.csv")

def load_marks_dataframe():
    return po.read_csv("marks.csv")

def query_dataframe(df, condition):
    try:
        result = df.query(condition)
        return result
    except Exception:
        return None


    