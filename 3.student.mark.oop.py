import math
import numpy as np
import curses

students = []
courses = []
marks = {}

def input_students(stdscr):
    stdscr.clear()

    num_students = int(
        get_input(stdscr, 1, 2, "Enter number of students: ")
    )

    for i in range(num_students):
        stdscr.clear()

        stdscr.addstr(1, 2, f"Student {i + 1}")

        s_id = get_input(stdscr, 3, 2, "Student ID: ")
        name = get_input(stdscr, 4, 2, "Student Name: ")
        dob = get_input(stdscr, 5, 2, "Date of Birth: ")

        students.append({
            "id": s_id,
            "name": name,
            "dob": dob
        })

    stdscr.addstr(7, 2, "Students added successfully!")
    stdscr.addstr(9, 2, "Press any key to return...")
    stdscr.getch()

    
def input_courses(stdscr):
    stdscr.clear()

    num_courses = int(
        get_input(stdscr, 1, 2, "Enter number of courses: ")
    )

    for i in range(num_courses):
        stdscr.clear()

        stdscr.addstr(1, 2, f"Course {i + 1}")

        c_id = get_input(stdscr, 3, 2, "Course ID: ")
        name = get_input(stdscr, 4, 2, "Course Name: ")
        credits = int(
            get_input(stdscr, 5, 2, "Credits: ")
        )

        courses.append({
            "id": c_id,
            "name": name,
            "credits": credits
        })

    stdscr.addstr(7, 2, "Courses added successfully!")
    stdscr.addstr(9, 2, "Press any key to return...")
    stdscr.getch()

def input_marks(stdscr):
    stdscr.clear()

    course_id = get_input(
        stdscr, 1, 2,
        "Enter Course ID to input marks: "
    )

    marks[course_id] = {}

    row = 3

    for student in students:
        mark = float(
            get_input(
                stdscr,
                row,
                2,
                f"Enter mark for {student['name']}: "
            )
        )

        mark = math.floor(mark * 10) / 10

        marks[course_id][student["id"]] = mark

        row += 1

    stdscr.addstr(row + 1, 2, "Marks added successfully!")
    stdscr.addstr(row + 2, 2, "Press any key to return...")
    stdscr.getch()

def list_courses(stdscr):
    stdscr.clear()

    stdscr.addstr(1, 2, "===== COURSE LIST =====")

    row = 3

    for course in courses:
        stdscr.addstr(
            row,
            2,
            f"ID: {course['id']}, Name: {course['name']}, Credits: {course['credits']}"
        )
        row += 1

    stdscr.addstr(row + 1, 2, "Press any key to return...")
    stdscr.getch()

def list_students(stdscr):
    stdscr.clear()

    stdscr.addstr(1, 2, "===== STUDENT LIST =====")

    row = 3

    for student in students:
        stdscr.addstr(
            row,
            2,
            f"ID: {student['id']}, Name: {student['name']}, DoB: {student['dob']}"
        )
        row += 1

    stdscr.addstr(row + 1, 2, "Press any key to return...")
    stdscr.getch()

def show_marks(stdscr):
    stdscr.clear()

    course_id = get_input(
        stdscr,
        1,
        2,
        "Enter Course ID to view marks: "
    )

    stdscr.clear()
    stdscr.addstr(1, 2, "===== MARKS =====")

    row = 3

    if course_id in marks:
        for student in students:
            student_mark = marks[course_id].get(
                student["id"],
                "No mark"
            )

            stdscr.addstr(
                row,
                2,
                f"{student['name']}: {student_mark}"
            )

            row += 1
    else:
        stdscr.addstr(row, 2, "No marks found for this course.")
        row += 1

    stdscr.addstr(row + 1, 2, "Press any key to return...")
    stdscr.getch()

def calculate_gpa(student_id):
    student_marks = []
    student_credits = []

    for course in courses:
        course_id = course["id"]

        if course_id in marks and student_id in marks[course_id]:
            student_marks.append(marks[course_id][student_id])
            student_credits.append(course["credits"])

    if len(student_marks) == 0:
        return 0

    marks_array = np.array(student_marks)
    credits_array = np.array(student_credits)

    gpa = np.sum(marks_array * credits_array) / np.sum(credits_array)

    return gpa

def show_gpa(stdscr):
    stdscr.clear()

    stdscr.addstr(1, 2, "===== GPA RANKING =====")

    sorted_students = sorted(
        students,
        key=lambda student: calculate_gpa(student["id"]),
        reverse=True
    )

    row = 3

    for student in sorted_students:
        gpa = calculate_gpa(student["id"])

        stdscr.addstr(
            row,
            2,
            f"{student['name']}: GPA = {gpa:.2f}"
        )

        row += 1

    stdscr.addstr(row + 1, 2, "Press any key to return...")
    stdscr.getch()
    reverse=True

def get_input(stdscr, y, x, prompt):
    curses.echo()

    stdscr.addstr(y, x, prompt)
    stdscr.refresh()

    value = stdscr.getstr(
        y,
        x + len(prompt),
        30
    ).decode("utf-8")

    curses.noecho()

    return value


def main(stdscr):
    curses.curs_set(0)

    while True:
        stdscr.clear()

        stdscr.addstr(1, 2, "===== STUDENT MANAGEMENT =====")
        stdscr.addstr(3, 2, "1. Input students")
        stdscr.addstr(4, 2, "2. Input courses")
        stdscr.addstr(5, 2, "3. Input marks")
        stdscr.addstr(6, 2, "4. List students")
        stdscr.addstr(7, 2, "5. List courses")
        stdscr.addstr(8, 2, "6. Show marks")
        stdscr.addstr(9, 2, "7. Show GPA")
        stdscr.addstr(10, 2, "0. Exit")

        stdscr.refresh()

        key = stdscr.getch()

        if key == ord('1'):
            input_students(stdscr)

        elif key == ord('2'):
            input_courses(stdscr)

        elif key == ord('3'):
            input_marks(stdscr)

        elif key == ord('4'):
            list_students(stdscr)

        elif key == ord('5'):
            list_courses(stdscr)

        elif key == ord('6'):
            show_marks(stdscr)

        elif key == ord('7'):
            show_gpa(stdscr)

        elif key == ord('0'):
            break

curses.wrapper(main)