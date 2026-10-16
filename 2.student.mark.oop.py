
class Student:
    def __init__(self, s_id="", name="", dob=""):
        self._s_id = s_id
        self._name = name
        self._dob = dob

    def input(self):
        self._s_id = input("Student ID: ")
        self._name = input("Student Name: ")
        self._dob = input("Date of Birth: ")

    def list(self):
        print(f"ID: {self._s_id}, Name: {self._name}, DoB: {self._dob}")

    def get_id(self):
        return self._s_id

    def get_name(self):
        return self._name

class Course:
    def __init__(self, c_id="", name=""):
        self._c_id = c_id
        self._name = name

    def input(self):
        self._c_id = input("Course ID: ")
        self._name = input("Course Name: ")

    def list(self):
        print(f"ID: {self._c_id}, Name: {self._name}")

    def get_id(self):
        return self._c_id

    def get_name(self):
        return self._name

class Mark:
    def __init__(self, course_id="", student_id="", mark=0.0):
        self._course_id = course_id
        self._student_id = student_id
        self._mark = mark

    def get_course_id(self):
        return self._course_id

    def get_student_id(self):
        return self._student_id

    def get_mark(self):
        return self._mark

class StudentMarkManagement:
    def __init__(self):
        self._students = []
        self._courses = []
        self._marks = []

    def input_students(self):
        num_students = int(input("Enter number of students: "))

        for i in range(num_students):
            student = Student()
            student.input()
            self._students.append(student)

    def input_courses(self):
        num_courses = int(input("Enter number of courses: "))

        for i in range(num_courses):
            course = Course()
            course.input()
            self._courses.append(course)

    def input_marks(self):
        course_id = input("Enter Course ID to input marks: ")

        for student in self._students:
            mark_value = float(
                input(f"Enter mark for {student.get_name()}: ")
            )

            mark = Mark(
                course_id,
                student.get_id(),
                mark_value
            )

            self._marks.append(mark)

    def list_students(self):
        for student in self._students:
            student.list()

    def list_courses(self):
        for course in self._courses:
            course.list()

    def show_marks(self):
        course_id = input("Enter Course ID to view marks: ")

        found_course = False

        for student in self._students:
            found_mark = False

            for mark in self._marks:
                if (
                    mark.get_course_id() == course_id
                    and mark.get_student_id() == student.get_id()
                ):
                    print(
                        f"{student.get_name()}: "
                        f"{mark.get_mark()}"
                    )
                    found_mark = True
                    found_course = True
                    break

            if not found_mark:
                print(f"{student.get_name()}: No mark")

        if not found_course:
            print("No marks found for this course.")

def input_students():
    num_students = int(input("Enter number of students: "))
    for i in range(num_students):
        student = Student()
        student.input()
        student.append(student)

def input_courses():
    num_courses = int(input("Enter number of courses: "))

    for i in range(num_courses):
        course = Course()
        course.input()
        course.append(course)

def input_marks():
    course_id = input("Enter Course ID to input marks: ")

    for student in student:
        mark_value = float(
            input(f"Enter mark for {student.get_name()}: ")
        )

        mark = Mark(
            course_id,
            student.get_id(),
            mark_value
        )

        mark.append(mark)

def list_courses():
    for course in course:
        course.list()

def list_students():
    for student in student:
        student.list()

def show_marks():
    course_id = input("Enter Course ID to view marks: ")

    found_course = False

    for student in student:
        found_mark = False

        for mark in mark:
            if (
                mark.get_course_id() == course_id
                and mark.get_student_id() == student.get_id()
            ):
                print(f"{student.get_name()}: {mark.get_mark()}")
                found_mark = True
                found_course = True
                break

        if not found_mark:
            print(f"{student.get_name()}: No mark")

    if not found_course:
        print("No marks found for this course.")

def main():
    management = StudentMarkManagement()

    while True:
        print("\n1. Input students | 2. Input courses | 3. Input marks")
        print("4. List students  | 5. List courses  | 6. Show marks | 0. Exit")

        choice = input("Select an option: ")

        if choice == '1':
            management.input_students()

        elif choice == '2':
            management.input_courses()

        elif choice == '3':
            management.input_marks()

        elif choice == '4':
            management.list_students()

        elif choice == '5':
            management.list_courses()

        elif choice == '6':
            management.show_marks()

        elif choice == '0':
            break


if __name__ == "__main__":
    main()