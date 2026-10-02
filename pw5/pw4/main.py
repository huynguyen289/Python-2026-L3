from storage import load_students, load_courses, load_data

import curses

from input import (
    input_students,
    input_courses,
    input_marks,
    get_input
)

from output import (
    list_students,
    list_courses,
    show_marks,
    show_gpa
)

from storage import (
    load_students,
    load_courses,
    load_marks,
    compress_data,
    decompress_data
)


load_students()
load_courses()
load_marks()


def main(stdscr):
    curses.curs_set(1)

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

        if key == ord("1"):
            input_students(
                stdscr,
                students
            )

        elif key == ord("2"):
            input_courses(
                stdscr,
                courses
            )

        elif key == ord("3"):
            input_marks(
                stdscr,
                students,
                marks
            )

        elif key == ord("4"):
            list_students(
                stdscr,
                students
            )

        elif key == ord("5"):
            list_courses(
                stdscr,
                courses
            )

        elif key == ord("6"):
            show_marks(
                stdscr,
                students,
                marks,
                get_input
            )

        elif key == ord("7"):
            show_gpa(
                stdscr,
                students,
                courses,
                marks
            )

        elif key == ord("0"):
            compress_data()
            break

decompress_data()
students = load_students()
courses = load_courses()
marks = load_marks()

curses.wrapper(main)

