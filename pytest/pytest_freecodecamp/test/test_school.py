import pytest
from source.school import Classroom, Teacher, Student, TooManyStudents

# Определим фикстуры для teacher, students, classroom
# @pytest.fixture
# def teacher():
#     """Create a teacher fixture"""
#     return Teacher("Professor Dumbledore")

# @pytest.fixture
# def student():
#     """Create a student fixture"""
#     return Student("Harry Potter")

# @pytest.fixture
# def classroom(teacher, student):
#     """Create a classroom fixture"""
#     return Classroom(teacher, [student], "Defense Against the Dark Arts")

# def test_add_student(classroom, student):
#     """Test adding a student to the classroom"""
#     new_student = Student("Ron Weasley")
#     classroom.add_student(new_student)
#     assert len(classroom.students) == 2

# @pytest.mark.parametrize("num_students", [1, 5, 10])
# def test_add_multiple_students(classroom, num_students):
#     """Test adding multiple students to the classroom"""
#     for _ in range(num_students):
#         classroom.add_student(Student(f"Student {_}"))
#     assert len(classroom.students) == num_students + 1

# def test_add_too_many_students(classroom):
#     """Test adding too many students to the classroom"""
#     for _ in range(10):
#         classroom.add_student(Student(f"Student {_}"))
#     with pytest.raises(TooManyStudents):
#         classroom.add_student(Student("Too Many Students"))

# def test_remove_student(classroom, student):
#     """Test removing a student from the classroom"""
#     classroom.remove_student(student.name)
#     assert len(classroom.students) == 0

# def test_change_teacher(classroom, teacher):
#     """Test changing the teacher of the classroom"""
#     new_teacher = Teacher("Professor Snape")
#     classroom.change_teacher(new_teacher)
#     assert classroom.teacher.name == "Professor Snape"

# pytest test/test_school.py

@pytest.fixture
def harry_potter():
    return Teacher("Harry Potter")

@pytest.fixture
def hermione_granger():
    return Student("Hermione Granger")

@pytest.fixture
def ron_weasley():
    return Student("Ron Weasley")

@pytest.fixture
def hogwarts_classroom(harry_potter):
    students = []
    return Classroom(harry_potter, students, "Defense Against the Dark Arts.")

# Тест-кейсы для класса Classroom
def test_classroom_creation(hogwarts_classroom):
    assert hogwarts_classroom.teacher.name == "Harry Potter"
    assert hogwarts_classroom.course_title == "Defense Against the Dark Arts."
    assert len(hogwarts_classroom.students) == 0


def test_add_student(hogwarts_classroom, hermione_granger, ron_weasley):
    hogwarts_classroom.add_student(hermione_granger)
    hogwarts_classroom.add_student(ron_weasley)
    assert len(hogwarts_classroom.students) == 2


def test_add_too_many_students(hogwarts_classroom, hermione_granger, ron_weasley):
    for _ in range(11):
        hogwarts_classroom.add_student(Student("Student"))

    with pytest.raises(TooManyStudents):
        hogwarts_classroom.add_student(hermione_granger)


def test_remove_student(hogwarts_classroom, hermione_granger, ron_weasley):
    hogwarts_classroom.add_student(hermione_granger)
    hogwarts_classroom.add_student(ron_weasley)

    hogwarts_classroom.remove_student("Hermione Granger")
    assert len(hogwarts_classroom.students) == 1
    assert hogwarts_classroom.students[0].name == "Ron Weasley"


def test_change_teacher(hogwarts_classroom, hermione_granger):
    new_teacher = Teacher("Severus Snape")
    hogwarts_classroom.change_teacher(new_teacher)
    assert hogwarts_classroom.teacher.name == "Severus Snape"


