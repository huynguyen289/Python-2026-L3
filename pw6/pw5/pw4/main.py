from storage import export_courses_to_csv, export_marks_to_csv, load_courses_dataframe, load_marks_dataframe, load_students, load_courses, load_data, load_students_dataframe

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
    decompress_data,
    save_data,
    export_to_csv,
    export_courses_to_csv,
    export_marks_to_csv,
    load_students_dataframe,
    load_courses_dataframe,
    load_marks_dataframe,
    query_dataframe,
    load_students_dataframe
)

load_students()
load_courses()
load_marks()


def main(stdscr):
    curses.curs_set(1)

    while True:
        stdscr.clear()

        stdscr.addstr(0, 2, "===== STUDENT MANAGEMENT =====")
        stdscr.addstr(1, 2, "1. Input students")
        stdscr.addstr(2, 2, "2. Input courses")
        stdscr.addstr(3, 2, "3. Input marks")
        stdscr.addstr(4, 2, "4. List students")
        stdscr.addstr(5, 2, "5. List courses")
        stdscr.addstr(6, 2, "6. Show marks")
        stdscr.addstr(7, 2, "7. Show GPA")
        stdscr.addstr(8, 2, "8. Query data")
        stdscr.addstr(9, 2, "0. Exit")
        
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

        elif key == ord("8"):
            stdscr.clear()

        stdscr.addstr(1, 2, "===== QUERY DATA =====")
        stdscr.addstr(3, 2, "1. Students")
        stdscr.addstr(4, 2, "2. Courses")
        stdscr.addstr(5, 2, "3. Marks")

        choice = get_input(
            stdscr,
            13,
            2,
            "Choose data: "
        )

        if choice == "1":
            df = load_students_dataframe()

        elif choice == "2":
            df = load_courses_dataframe()

        elif choice == "3":
            df = load_marks_dataframe()

        else:
            stdscr.addstr(9, 2, "Invalid choice!")
            stdscr.addstr(11, 2, "Press any key to return...")
            stdscr.getch()
            continue

        condition = get_input(
            stdscr,
            9,
            2,
            "Enter query condition: "
        )

        result = query_dataframe(df, condition)

        stdscr.clear()

        if result is None:
            stdscr.addstr(1, 2, "Invalid query!")

        elif result.empty:
            stdscr.addstr(1, 2, "No matching data.")

        else:
            stdscr.addstr(1, 2, str(result))

        stdscr.addstr(15, 2, "Press any key to return...")
        stdscr.getch()
        



        

decompress_data()
students, courses, marks = load_data()


curses.wrapper(main)

