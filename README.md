# Simple Learning Management System (LMS)

A simple Python-based Learning Management System with core features for managing students, courses, and teachers.

## Features

- **Student Management**: Create students and manage enrollments
- **Course Management**: Create courses and add materials
- **Teacher Management**: Teachers can create and manage courses
- **Enrollment System**: Students can enroll in courses
- **Material Management**: Add course materials (chapters, lectures, etc.)

## Classes

### Student
- `__init__(student_id, name, email)` - Create a student
- `enroll_course(course)` - Enroll in a course
- `view_courses()` - View all enrolled courses

### Course
- `__init__(course_id, course_name, teacher_name)` - Create a course
- `add_material(material)` - Add course material
- `add_student(student)` - Add student to course
- `view_students()` - View all students in course
- `view_materials()` - View all course materials

### Teacher
- `__init__(teacher_id, name, email)` - Create a teacher
- `create_course(course_id, course_name)` - Create a new course
- `view_courses()` - View all courses created by teacher

## Installation

No external dependencies required. Just Python 3.6+

```bash
git clone https://github.com/Abdull003/learning-management-system.git
cd learning-management-system
```

## Usage

### Run the Demo

```bash
python simple_lms.py
```

### Run Tests

```bash
python -m unittest test_simple_lms.py
```

### Example Code

```python
from simple_lms import Student, Course, Teacher

# Create teacher
teacher = Teacher(1, "Mr. John", "john@school.com")

# Create course
course = teacher.create_course(101, "Python Basics")

# Add materials
course.add_material("Chapter 1: Introduction")
course.add_material("Chapter 2: Variables")

# Create students
student1 = Student(1, "Alice", "alice@school.com")
student2 = Student(2, "Bob", "bob@school.com")

# Enroll students
student1.enroll_course(course)
student2.enroll_course(course)

# Add to course
course.add_student(student1)
course.add_student(student2)

# View information
print(f"Course: {course.course_name}")
print(f"Students: {course.view_students()}")
print(f"Materials: {course.view_materials()}")
```

## Project Structure

```
learning-management-system/
├── simple_lms.py           # Main LMS implementation
├── test_simple_lms.py      # Unit tests
└── README.md               # This file
```

## Testing

The project includes comprehensive unit tests:
- Student class tests
- Course class tests
- Teacher class tests
- Integration tests

## Future Enhancements

- Assignment submission system
- Grading system
- Attendance tracking
- Notification system
- Database integration
- Web API (Flask/Django)
- User authentication

## License

MIT License

## Author

Abdull003
