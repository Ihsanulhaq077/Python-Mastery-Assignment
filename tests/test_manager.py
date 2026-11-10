# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
Unit tests for school/manager.py (SchoolManager).
Tests:
- Adding students and preventing duplicate IDs
- Searching students by ID and by name substring
- Updating student records
- Deleting students
- Student class ranking (highest average is Rank 1)
"""

import pytest
from school.manager import SchoolManager
from school.models import Student


@pytest.fixture
def populated_manager(tmp_path):
    """Provides a fresh SchoolManager populated with 3 test students."""
    file_path = tmp_path / "test_school.json"
    manager = SchoolManager(storage_path=file_path)

    s1 = Student(101, "Ali Raza", 20, "AI", {"Math": 70.0, "Python": 80.0})     # avg 75.0
    s2 = Student(102, "Sara Khan", 19, "AI", {"Math": 95.0, "Python": 95.0})    # avg 95.0
    s3 = Student(103, "Bilal Ahmad", 21, "AI", {"Math": 50.0, "Python": 60.0})  # avg 55.0

    manager.add_student(s1)
    manager.add_student(s2)
    manager.add_student(s3)
    return manager


def test_add_student(tmp_path):
    """Test adding students and duplicate rejection."""
    manager = SchoolManager(storage_path=tmp_path / "dummy.json")
    s = Student(1, "Ihsan", 20, "AI", {"Python": 90.0})

    assert manager.add_student(s) is True
    assert manager.student_count == 1
    # Adding same student ID must return False
    assert manager.add_student(s) is False
    assert manager.student_count == 1


def test_get_and_search_students(populated_manager):
    """Test retrieving student by ID and searching by keyword."""
    # Direct get
    student = populated_manager.get_student(102)
    assert student is not None
    assert student.name == "Sara Khan"

    # Search by exact ID string
    results = populated_manager.search_students("101")
    assert len(results) == 1
    assert results[0].name == "Ali Raza"

    # Search by case-insensitive name substring
    results_name = populated_manager.search_students("sara")
    assert len(results_name) == 1
    assert results_name[0].student_id == 102

    # Search non-existent
    assert populated_manager.search_students("NonExistent") == []


def test_update_student(populated_manager):
    """Test updating student name, age, and class."""
    success = populated_manager.update_student(
        student_id=101,
        name="Ali Raza Khan",
        age=22,
        class_name="Advanced AI",
    )
    assert success is True
    updated = populated_manager.get_student(101)
    assert updated.name == "Ali Raza Khan"
    assert updated.age == 22
    assert updated.class_name == "Advanced AI"


def test_delete_student(populated_manager):
    """Test deleting existing and non-existing students."""
    assert populated_manager.delete_student(103) is True
    assert populated_manager.get_student(103) is None
    assert populated_manager.student_count == 2
    # Deleting again should return False
    assert populated_manager.delete_student(103) is False


def test_student_ranking(populated_manager):
    """Test ranking calculation where highest average is Rank 1."""
    rankings = populated_manager.get_class_ranking()

    assert len(rankings) == 3
    # Rank 1: Sara Khan (avg 95.0)
    assert rankings[0][0] == 1
    assert rankings[0][1].student_id == 102
    assert rankings[0][1].average == 95.0

    # Rank 2: Ali Raza (avg 75.0)
    assert rankings[1][0] == 2
    assert rankings[1][1].student_id == 101
    assert rankings[1][1].average == 75.0

    # Rank 3: Bilal Ahmad (avg 55.0)
    assert rankings[2][0] == 3
    assert rankings[2][1].student_id == 103
    assert rankings[2][1].average == 55.0

