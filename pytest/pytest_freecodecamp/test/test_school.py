import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents

# Определим фикстуры для teacher, students, classroom
@pytest.fixture
def teacher():
    """Create a teacher fixture"""
    return Teacher("Professor Dumbledore")

@pytest.fixture
def student():
    """Create a student fixture"""
    return Student("Harry Potter")

@pytest.fixture
def classroom(teacher, student):
    """Create a classroom fixture"""
    return Classroom(teacher, [student], "Defense Against the Dark Arts")

def test_add_student(classroom, student):
    """Test adding a student to the classroom"""
    new_student = Student("Ron Weasley")
    classroom.add_student(new_student)
    assert len(classroom.students) == 2

@pytest.mark.parametrize("num_students", [1, 5, 10])
def test_add_multiple_students(classroom, num_students):
    """Test adding multiple students to the classroom"""
    for _ in range(num_students):
        classroom.add_student(Student(f"Student {_}"))
    assert len(classroom.students) == num_students + 1

def test_add_too_many_students(classroom):
    """Test adding too many students to the classroom"""
    for _ in range(10):
        classroom.add_student(Student(f"Student {_}"))
    with pytest.raises(TooManyStudents):
        classroom.add_student(Student("Too Many Students"))

def test_remove_student(classroom, student):
    """Test removing a student from the classroom"""
    classroom.remove_student(student.name)
    assert len(classroom.students) == 0

def test_change_teacher(classroom, teacher):
    """Test changing the teacher of the classroom"""
    new_teacher = Teacher("Professor Snape")
    classroom.change_teacher(new_teacher)
    assert classroom.teacher.name == "Professor Snape"

# pytest test/test_school.py