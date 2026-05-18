# Simple Learning Management System (LMS)
# Core classes: Student, Course, Teacher

class Student:
    """Student class to manage student data and enrollments"""
    def __init__(self, student_id, name, email):
        self.student_id = student_id
        self.name = name
        self.email = email
        self.enrolled_courses = []
    
    def enroll_course(self, course):
        """Enroll student in a course"""
        if course not in self.enrolled_courses:
            self.enrolled_courses.append(course)
            print(f"{self.name} enrolled in {course.course_name}")
        else:
            print(f"{self.name} is already enrolled in {course.course_name}")
    
    def view_courses(self):
        """View all enrolled courses"""
        if not self.enrolled_courses:
            print(f"{self.name} has no enrolled courses")
            return []
        return [course.course_name for course in self.enrolled_courses]
    
    def drop_course(self, course):
        """Unenroll student from a course"""
        if course in self.enrolled_courses:
            self.enrolled_courses.remove(course)
            print(f"{self.name} dropped {course.course_name}")
            if self in course.students:
                course.students.remove(self)
        else:
            print(f"{self.name} is not enrolled in {course.course_name}")
    
    def __repr__(self):
        return self.name


class Course:
    """Course class to manage course information"""
    def __init__(self, course_id, course_name, teacher_name):
        self.course_id = course_id
        self.course_name = course_name
        self.teacher_name = teacher_name
        self.materials = []
        self.students = []
    
    def add_material(self, material):
        """Add course material (chapter, lecture, etc.)"""
        if material not in self.materials:
            self.materials.append(material)
            print(f"Material '{material}' added to {self.course_name}")
        else:
            print(f"Material '{material}' already exists")
    
    def add_student(self, student):
        """Add student to course"""
        if student not in self.students:
            self.students.append(student)
            print(f"Student {student.name} added to {self.course_name}")
        else:
            print(f"Student {student.name} already in {self.course_name}")
    
    def view_students(self):
        """View all students in course"""
        return [student.name for student in self.students]
    
    def view_materials(self):
        """View all course materials"""
        return self.materials
    
    def __repr__(self):
        return self.course_name


class Teacher:
    """Teacher class to manage teacher data and courses"""
    def __init__(self, teacher_id, name, email):
        self.teacher_id = teacher_id
        self.name = name
        self.email = email
        self.courses = []
    
    def create_course(self, course_id, course_name):
        """Create a new course"""
        course = Course(course_id, course_name, self.name)
        self.courses.append(course)
        print(f"Course '{course_name}' created by {self.name}")
        return course
    
    def view_courses(self):
        """View all courses created by teacher"""
        return [course.course_name for course in self.courses]
    
    def __repr__(self):
        return self.name


# Demo
if __name__ == "__main__":
    print("=== Simple Learning Management System ===")
    print()
    
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
    print()
    
    # Enroll students
    student1.enroll_course(course)
    student2.enroll_course(course)
    student3.enroll_course(course)
    print()
    
    # Add students to course
    course.add_student(student1)
    course.add_student(student2)
    course.add_student(student3)
    print()
    
    # Display information
    print("=== Course Information ===")
    print(f"Course: {course.course_name}")
    print(f"Teacher: {course.teacher_name}")
    print(f"Students: {course.view_students()}")
    print(f"Materials: {course.view_materials()}")
    print()
    
    # Student view
    print("=== Student View ===")
    print(f"{student1.name}'s Courses: {student1.view_courses()}")
    print(f"{student2.name}'s Courses: {student2.view_courses()}")
    print()
    
    # Teacher view
    print("=== Teacher View ===")
    print(f"{teacher.name}'s Courses: {teacher.view_courses()}")
