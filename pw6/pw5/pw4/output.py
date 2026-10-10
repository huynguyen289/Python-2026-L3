import numpy as np


def list_courses(stdscr, courses):
    stdscr.clear()

    stdscr.addstr(1, 2, "===== COURSE LIST =====")

    row = 3

    for course in courses:
        stdscr.addstr(
            row,
            2,
            f"ID: {course.id}, Name: {course.name}, Credits: {course.credits}"
        )
        row += 1

    stdscr.addstr(row + 1, 2, "Press any key to return...")
    stdscr.getch()


def list_students(stdscr, students):
    stdscr.clear()

    stdscr.addstr(1, 2, "===== STUDENT LIST =====")

    row = 3

    for student in students:
        stdscr.addstr(
            row,
            2,
            f"ID: {student.id}, Name: {student.name}, DoB: {student.dob}"
        )
        row += 1

    stdscr.addstr(row + 1, 2, "Press any key to return...")
    stdscr.getch()


def show_marks(stdscr, students, marks, get_input):
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
                student.id,
                "No mark"
            )

            stdscr.addstr(
                row,
                2,
                f"{student.name}: {student_mark}"
            )

            row += 1

    else:
        stdscr.addstr(
            row,
            2,
            "No marks found for this course."
        )

        row += 1

    stdscr.addstr(row + 1, 2, "Press any key to return...")
    stdscr.getch()


def calculate_gpa(student_id, courses, marks):
    student_marks = []
    student_credits = []

    for course in courses:

        course_id = course.id

        if course_id in marks and student_id in marks[course_id]:

            student_marks.append(
                marks[course_id][student_id]
            )

            student_credits.append(
                course.credits
            )

    if len(student_marks) == 0:
        return 0

    marks_array = np.array(student_marks)
    credits_array = np.array(student_credits)

    gpa = (
        np.sum(marks_array * credits_array)
        / np.sum(credits_array)
    )

    return gpa


def show_gpa(stdscr, students, courses, marks):
    stdscr.clear()

    stdscr.addstr(1, 2, "===== GPA RANKING =====")

    sorted_students = sorted(
        students,
        key=lambda student: calculate_gpa(
            student.id,
            courses,
            marks
        ),
        reverse=True
    )

    row = 3

    for student in sorted_students:

        gpa = calculate_gpa(
            student.id,
            courses,
            marks
        )

        stdscr.addstr(
            row,
            2,
            f"{student.name}: GPA = {gpa:.2f}"
        )

        row += 1

    stdscr.addstr(row + 1, 2, "Press any key to return...")
    stdscr.getch()