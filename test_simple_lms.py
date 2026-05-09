import unittest
from simple_lms import Student, Course, Teacher


class TestStudent(unittest.TestCase):
    """Test cases for Student class"""
    
    def setUp(self):
        self.student = Student(1, "Alice", "alice@school.com")
        self.course = Course(101, "Python Basics", "Mr. John")
    
    def test_student_creation(self):
        """Test student object creation"""
        self.assertEqual(self.student.name, "Alice")
        self.assertEqual(self.student.email, "alice@school.com")
        self.assertEqual(self.student.student_id, 1)
    
    def test_enroll_course(self):
        """Test student enrollment in course"""
        self.student.enroll_course(self.course)
        self.assertIn(self.course, self.student.enrolled_courses)
    
    def test_view_courses(self):
        """Test viewing enrolled courses"""
        self.student.enroll_course(self.course)
        courses = self.student.view_courses()
        self.assertIn("Python Basics", courses)
    
    def test_duplicate_enrollment(self):
        """Test preventing duplicate enrollment"""
        self.student.enroll_course(self.course)
        initial_count = len(self.student.enrolled_courses)
        self.student.enroll_course(self.course)
        self.assertEqual(len(self.student.enrolled_courses), initial_count)


class TestCourse(unittest.TestCase):
    """Test cases for Course class"""
    
    def setUp(self):
        self.course = Course(101, "Python Basics", "Mr. John")
        self.student = Student(1, "Alice", "alice@school.com")
    
    def test_course_creation(self):
        """Test course object creation"""
        self.assertEqual(self.course.course_name, "Python Basics")
        self.assertEqual(self.course.teacher_name, "Mr. John")
        self.assertEqual(self.course.course_id, 101)
    
    def test_add_material(self):
        """Test adding course material"""
        self.course.add_material("Chapter 1")
        self.assertIn("Chapter 1", self.course.materials)
    
    def test_add_student(self):
        """Test adding student to course"""
        self.course.add_student(self.student)
        self.assertIn(self.student, self.course.students)
    
    def test_view_materials(self):
        """Test viewing course materials"""
        self.course.add_material("Chapter 1")
        self.course.add_material("Chapter 2")
        materials = self.course.view_materials()
        self.assertEqual(len(materials), 2)
    
    def test_view_students(self):
        """Test viewing course students"""
        self.course.add_student(self.student)
        students = self.course.view_students()
        self.assertIn("Alice", students)


class TestTeacher(unittest.TestCase):
    """Test cases for Teacher class"""
    
    def setUp(self):
        self.teacher = Teacher(1, "Mr. John", "john@school.com")
    
    def test_teacher_creation(self):
        """Test teacher object creation"""
        self.assertEqual(self.teacher.name, "Mr. John")
        self.assertEqual(self.teacher.email, "john@school.com")
        self.assertEqual(self.teacher.teacher_id, 1)
    
    def test_create_course(self):
        """Test creating a course"""
        course = self.teacher.create_course(101, "Python Basics")
        self.assertIn(course, self.teacher.courses)
    
    def test_view_courses(self):
        """Test viewing teacher's courses"""
        self.teacher.create_course(101, "Python Basics")
        self.teacher.create_course(102, "Web Development")
        courses = self.teacher.view_courses()
        self.assertEqual(len(courses), 2)
        self.assertIn("Python Basics", courses)


class TestIntegration(unittest.TestCase):
    """Integration tests for LMS system"""
    
    def setUp(self):
        self.teacher = Teacher(1, "Mr. John", "john@school.com")
        self.course = self.teacher.create_course(101, "Python Basics")
        self.student1 = Student(1, "Alice", "alice@school.com")
        self.student2 = Student(2, "Bob", "bob@school.com")
    
    def test_full_workflow(self):
        """Test complete LMS workflow"""
        # Teacher creates course and adds materials
        self.course.add_material("Chapter 1: Intro")
        self.course.add_material("Chapter 2: Variables")
        
        # Students enroll
        self.student1.enroll_course(self.course)
        self.student2.enroll_course(self.course)
        
        # Add students to course
        self.course.add_student(self.student1)
        self.course.add_student(self.student2)
        
        # Verify
        self.assertEqual(len(self.course.students), 2)
        self.assertEqual(len(self.course.materials), 2)
        self.assertEqual(len(self.student1.enrolled_courses), 1)


if __name__ == "__main__":
    unittest.main()
