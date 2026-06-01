# Simple Learning Management System (LMS)
# Core classes: Student, Course, Teacher, Assignment + Grades

from datetime import date


# ---------------------------------------------------------------------------
# Grade Utilities
# ---------------------------------------------------------------------------

def calculate_letter_grade(percentage: float) -> str:
    """Convert a percentage score to a letter grade."""
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage >= 50:
        return "E"
    else:
        return "F"


def letter_to_gpa(letter: str) -> float:
    """Convert a letter grade to a 4.0 GPA point value."""
    return {"A": 4.0, "B": 3.0, "C": 2.0, "D": 1.0, "F": 0.0}.get(letter, 0.0)


class Assignment:
    """Represents a course assignment with a title, description, due date, and max points."""

    def __init__(self, assignment_id, title, description, due_date: date, max_points=100):
        self.assignment_id = assignment_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.max_points = max_points
        self.submissions = {}  # {student_id: {"content": ..., "score": None}}

    def submit(self, student, content):
        """Accept a submission from a student."""
        if student.student_id in self.submissions:
            print(f"{student.name} has already submitted '{self.title}'. Overwriting.")
        self.submissions[student.student_id] = {"content": content, "score": None}
        print(f"'{self.title}' submitted by {student.name}.")

    def grade_submission(self, student, score):
        """Assign a score to a student's submission."""
        if student.student_id not in self.submissions:
            print(f"No submission found from {student.name} for '{self.title}'.")
            return
        if score > self.max_points:
            print(f"Score {score} exceeds max points ({self.max_points}).")
            return
        self.submissions[student.student_id]["score"] = score
        pct = (score / self.max_points) * 100
        letter = calculate_letter_grade(pct)
        print(f"{student.name} scored {score}/{self.max_points} ({pct:.1f}% — {letter}) on '{self.title}'.")

    def get_student_grade(self, student_id):
        """Return (score, percentage, letter) for a student, or None if ungraded."""
        sub = self.submissions.get(student_id)
        if sub is None or sub["score"] is None:
            return None
        score = sub["score"]
        pct = (score / self.max_points) * 100
        return score, pct, calculate_letter_grade(pct)

    def view_submissions(self):
        """Return a summary of all submissions."""
        return {
            sid: {
                "content": data["content"],
                "score": data["score"] if data["score"] is not None else "Not graded"
            }
            for sid, data in self.submissions.items()
        }

    def __repr__(self):
        return f"Assignment({self.title}, due={self.due_date})"


class Student:
    """Student class to manage student data and enrollments."""

    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.enrolled_courses = []

    def enroll_course(self, course):
        """Enroll student in a course."""
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            print(f"{self.name} enrolled in {course.course_name}")
        else:
            print(f"{self.name} is already enrolled in {course.course_name}")

    def view_courses(self):
        """View all enrolled courses."""
        if not self.enrolled_courses:
            print(f"{self.name} has no enrolled courses")
            return []
        return [course.course_name for course in self.enrolled_courses]

    def drop_course(self, course):
        """Unenroll student from a course."""
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)
            print(f"{self.name} dropped {course.course_name}")
            if self in course.students:
                course.students.remove(self)
        else:
            print(f"{self.name} is not enrolled in {course.course_name}")

    def submit_assignment(self, assignment, content):
        """Submit work for a specific assignment."""
        assignment.submit(self, content)

    def view_assignments(self, course):
        """List all assignments for an enrolled course."""
        if course not in self.enrolled_courses:
            print(f"{self.name} is not enrolled in {course.course_name}.")
            return []
        assignments = course.view_assignments()
        if not assignments:
            print(f"No assignments in {course.course_name} yet.")
        return assignments

    def view_my_grades(self, course):
        """View personal scores, percentages, and letter grades for a course."""
        print(f"\n--- {self.name}'s Grades in {course.course_name} ---")
        graded_pcts = []
        found = False
        for assignment in course.assignments:
            result = assignment.get_student_grade(self.student_id)
            if result:
                score, pct, letter = result
                print(f"  {assignment.title}: {score}/{assignment.max_points} ({pct:.1f}% — {letter})")
                graded_pcts.append(pct)
                found = True
            else:
                sub = assignment.submissions.get(self.student_id)
                if sub:
                    print(f"  {assignment.title}: Submitted — Not graded yet")
                    found = True
        if not found:
            print("  No submissions found.")
        if graded_pcts:
            avg = sum(graded_pcts) / len(graded_pcts)
            overall_letter = calculate_letter_grade(avg)
            print(f"  ─────────────────────────────────")
            print(f"  Course Average: {avg:.1f}% — {overall_letter}")

    def __repr__(self):
        return self.name


class Course:
    """Course class to manage course information."""

    def __init__(self, course_id, course_name, teacher_name):
        self.course_id = course_id
        self.course_name = course_name
        self.teacher_name = teacher_name
        self.materials = []
        self.students = []
        self.assignments = []

    def add_material(self, material):
        """Add course material (chapter, lecture, etc.)."""
        if material not in self.materials:
            self.materials.append(material)
            print(f"Material '{material}' added to {self.course_name}")
        else:
            print(f"Material '{material}' already exists")

    def add_student(self, student):
        """Add student to course."""
        if student not in self.students:
            self.students.append(student)
            print(f"Student {student.name} added to {self.course_name}")
        else:
            print(f"Student {student.name} already in {self.course_name}")

    def add_assignment(self, assignment):
        """Add an assignment to the course."""
        if assignment not in self.assignments:
            self.assignments.append(assignment)
            print(f"Assignment '{assignment.title}' added to {self.course_name}")
        else:
            print(f"Assignment '{assignment.title}' already exists in {self.course_name}")

    def view_students(self):
        """View all students in course."""
        return [student.name for student in self.students]

    def view_materials(self):
        """View all course materials."""
        return self.materials

    def view_assignments(self):
        """View all assignments in the course."""
        return [(a.title, str(a.due_date), a.max_points) for a in self.assignments]

    def __repr__(self):
        return self.course_name


class Teacher:
    """Teacher class to manage teacher data and courses."""

    def __init__(self, teacher_id, name, email):
        self.teacher_id = teacher_id
        self.name = name
        self.email = email
        self.courses = []

    def create_course(self, course_id, course_name):
        """Create a new course."""
        course = Course(course_id, course_name, self.name)
        self.courses.append(course)
        print(f"Course '{course_name}' created by {self.name}")
        return course

    def create_assignment(self, course, assignment_id, title, description, due_date, max_points=100):
        """Create and add an assignment to a course."""
        assignment = Assignment(assignment_id, title, description, due_date, max_points)
        course.add_assignment(assignment)
        return assignment

    def grade_assignment(self, assignment, student, score):
        """Grade a student's submission for an assignment."""
        assignment.grade_submission(student, score)

    def view_submissions(self, assignment):
        """View all submissions for an assignment."""
        print(f"\n--- Submissions for '{assignment.title}' ---")
        subs = assignment.view_submissions()
        if not subs:
            print("  No submissions yet.")
        for sid, data in subs.items():
            print(f"  Student ID {sid}: Score={data['score']}, Content='{data['content']}'")

    def view_courses(self):
        """View all courses created by teacher."""
        return [course.course_name for course in self.courses]

    def __repr__(self):
        return self.name


# Demo
if __name__ == "__main__":
    print("=== Simple Learning Management System ===\n")

    # Create teacher
    teacher = Teacher(1, "Mr. John", "john@school.com")

    # Create course
    course = teacher.create_course(101, "Python Basics")
    print()

    # Add materials
    course.add_material("Chapter 1: Introduction")
    course.add_material("Chapter 2: Variables")
    course.add_material("Chapter 3: Loops")
    print()

    # Create students
    student1 = Student(1, "Alice", "alice@school.com")
    student2 = Student(2, "Bob", "bob@school.com")
    student3 = Student(3, "Charlie", "charlie@school.com")

    # Enroll and add students
    for student in [student1, student2, student3]:
        student.enroll_course(course)
        course.add_student(student)
    print()

    # --- Assignments Feature ---
    print("=== Assignments ===\n")

    # Teacher creates assignments
    a1 = teacher.create_assignment(
        course, 1, "Hello World Program",
        "Write a Python script that prints Hello, World!",
        due_date=date(2025, 6, 10)
    )
    a2 = teacher.create_assignment(
        course, 2, "Variables Quiz",
        "Answer 10 questions about Python variables.",
        due_date=date(2025, 6, 20), max_points=50
    )
    print()

    # Students view assignments
    print(f"{student1.name}'s assignments in {course.course_name}:")
    for title, due, pts in student1.view_assignments(course):
        print(f"  - {title} | Due: {due} | Max Points: {pts}")
    print()

    # Students submit assignments
    student1.submit_assignment(a1, "print('Hello, World!')")
    student2.submit_assignment(a1, "print('Hello World')")
    student3.submit_assignment(a1, "print('hello, world')")
    print()

    # Teacher grades submissions
    print("=== Grading ===\n")
    teacher.grade_assignment(a1, student1, 100)
    teacher.grade_assignment(a1, student2, 90)
    teacher.grade_assignment(a1, student3, 75)
    print()

    # Teacher views all submissions
    teacher.view_submissions(a1)

    # Students view their own grades
    student1.view_my_grades(course)
    student2.view_my_grades(course)

    # Display course info
    print("\n=== Course Information ===")
    print(f"Course: {course.course_name}")
    print(f"Teacher: {course.teacher_name}")
    print(f"Students: {course.view_students()}")
    print(f"Materials: {course.view_materials()}")
    print(f"Assignments: {[a[0] for a in course.view_assignments()]}")

    print("\n=== Teacher View ===")
    print(f"{teacher.name}'s Courses: {teacher.view_courses()}")