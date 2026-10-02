import math
import curses

from domains.student import Student
from domains.course import Course
from domains.mark import Mark


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


def input_students(stdscr, students):
    stdscr.clear()

    value = get_input(
        stdscr,
        1,
        2,
        "Enter number of students: "
    )

    if value == "":
        return

    num_students = int(value)

    for i in range(num_students):
        stdscr.clear()

        stdscr.addstr(1, 2, f"Student {i + 1}")

        s_id = get_input(stdscr, 3, 2, "Student ID: ")
        name = get_input(stdscr, 4, 2, "Student Name: ")
        dob = get_input(stdscr, 5, 2, "Date of Birth: ")

        students.append(
            Student(s_id, name, dob)
        )

    stdscr.addstr(7, 2, "Students added successfully!")
    stdscr.addstr(9, 2, "Press any key to return...")
    stdscr.getch()


def input_courses(stdscr, courses):
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

        courses.append(
            Course(c_id, name, credits)
        )

    stdscr.addstr(7, 2, "Courses added successfully!")
    stdscr.addstr(9, 2, "Press any key to return...")
    stdscr.getch()


def input_marks(stdscr, students, marks):
    stdscr.clear()

    course_id = get_input(
        stdscr,
        1,
        2,
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
                f"Enter mark for {student.name}: "
            )
        )

        mark = math.floor(mark * 10) / 10

        marks[course_id][student.id] = mark

        row += 1

    stdscr.addstr(row + 1, 2, "Marks added successfully!")
    stdscr.addstr(row + 2, 2, "Press any key to return...")
    stdscr.getch()

    