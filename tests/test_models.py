# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
Unit tests for school/models.py (Student Dataclass).
Tests:
- Student instantiation and validation
- Total marks and average calculation
- Grade calculation scale (A+, A, B, C, D, F)
- Pass/Fail logic
- Serialization (to_dict, from_dict)
"""

import pytest
from school.models import Student


def test_student_creation():
    """Verify student dataclass fields and instantiation."""
    student = Student(
        student_id=1,
        name="Ihsan Ul Haq",
        age=20,
        class_name="AI-101",
        marks={"Python": 90.0, "Math": 80.0},
    )
    assert student.student_id == 1
    assert student.name == "Ihsan Ul Haq"
    assert student.age == 20
    assert student.class_name == "AI-101"
    assert student.marks == {"Python": 90.0, "Math": 80.0}


def test_student_validation_invalid_id():
    """Ensure negative or zero student ID raises ValueError."""
    with pytest.raises(ValueError):
        Student(student_id=-5, name="Ali", age=20, class_name="AI")


def test_student_validation_empty_name():
    """Ensure empty student name raises ValueError."""
    with pytest.raises(ValueError):
        Student(student_id=2, name="   ", age=20, class_name="AI")


def test_student_validation_invalid_age():
    """Ensure age outside 5-100 raises ValueError."""
    with pytest.raises(ValueError):
        Student(student_id=3, name="Sara", age=3, class_name="AI")


def test_student_validation_invalid_marks():
    """Ensure marks outside 0-100 raise ValueError."""
    with pytest.raises(ValueError):
        Student(student_id=4, name="Bilal", age=20, class_name="AI", marks={"Math": 105.0})


def test_average_calculation():
    """Verify total and average calculations."""
    student = Student(
        student_id=5,
        name="Test Student",
        age=21,
        class_name="AI",
        marks={"Subject1": 80.0, "Subject2": 90.0, "Subject3": 70.0},
    )
    assert student.total_marks == 240.0
    assert student.average == 80.0
    assert student.percentage == 80.0


def test_average_calculation_empty_marks():
    """Verify student with no marks reports 0.0 average."""
    student = Student(student_id=6, name="Newbie", age=19, class_name="AI", marks={})
    assert student.total_marks == 0.0
    assert student.average == 0.0


@pytest.mark.parametrize(
    "score,expected_grade",
    [
        (95.0, "A+"),
        (90.0, "A+"),
        (85.0, "A"),
        (80.0, "A"),
        (75.0, "B"),
        (70.0, "B"),
        (65.0, "C"),
        (60.0, "C"),
        (55.0, "D"),
        (50.0, "D"),
        (49.0, "F"),
        (0.0, "F"),
    ],
)
def test_grade_calculation(score, expected_grade):
    """Verify student grade calculation across all boundary tiers."""
    student = Student(
        student_id=7,
        name="Tier Student",
        age=20,
        class_name="AI",
        marks={"Test": score},
    )
    assert student.grade == expected_grade


def test_pass_fail():
    """Verify pass/fail boolean threshold at 50%."""
    passing_student = Student(
        student_id=8,
        name="Pass Student",
        age=20,
        class_name="AI",
        marks={"Exam": 50.0},
    )
    failing_student = Student(
        student_id=9,
        name="Fail Student",
        age=20,
        class_name="AI",
        marks={"Exam": 49.9},
    )
    assert passing_student.is_passed is True
    assert failing_student.is_passed is False


def test_serialization_to_and_from_dict():
    """Verify to_dict and from_dict symmetry."""
    student = Student(
        student_id=10,
        name="Serial Student",
        age=22,
        class_name="Data Science",
        marks={"Python": 95.0, "SQL": 88.0},
    )
    raw = student.to_dict()
    reconstructed = Student.from_dict(raw)
    assert reconstructed.student_id == student.student_id
    assert reconstructed.name == student.name
    assert reconstructed.marks == student.marks
    assert reconstructed.average == student.average

