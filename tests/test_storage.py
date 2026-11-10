# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
Unit tests for school/storage.py and bonus utility features.
Tests:
- JSON save and load round-trip
- Missing file handling
- Empty file handling
- Corrupted JSON graceful handling
- AI comment generation and streaming generator (Bonus Feature)
"""

from school.models import Student
from school.storage import load_students, save_students
from school.utils import build_teacher_feedback, format_report_card, generate_teacher_comment_stream


def test_json_save_load(tmp_path):
    """Verify students can be saved to JSON and accurately reloaded."""
    test_file = tmp_path / "students_test.json"

    students_to_save = [
        Student(101, "Ihsan Ul Haq", 20, "AI-101", {"Math": 95.0, "Python": 98.0}),
        Student(102, "Sara Khan", 19, "AI-101", {"Math": 88.0, "Python": 92.0}),
    ]

    # Save to disk
    save_success = save_students(students_to_save, test_file)
    assert save_success is True
    assert test_file.exists()

    # Load from disk
    loaded = load_students(test_file)
    assert len(loaded) == 2
    assert loaded[0].student_id == 101
    assert loaded[0].name == "Ihsan Ul Haq"
    assert loaded[0].average == 96.5
    assert loaded[1].student_id == 102
    assert loaded[1].name == "Sara Khan"


def test_storage_missing_file(tmp_path):
    """Ensure missing file returns an empty list without raising an unhandled exception."""
    missing_path = tmp_path / "does_not_exist.json"
    result = load_students(missing_path)
    assert result == []


def test_storage_empty_file(tmp_path):
    """Ensure an empty file returns an empty list cleanly."""
    empty_path = tmp_path / "empty.json"
    empty_path.write_text("", encoding="utf-8")
    result = load_students(empty_path)
    assert result == []


def test_storage_corrupted_json(tmp_path):
    """Ensure invalid JSON content returns empty list and does not crash."""
    bad_json_path = tmp_path / "corrupted.json"
    bad_json_path.write_text("{ this is not valid json }", encoding="utf-8")
    result = load_students(bad_json_path)
    assert result == []


def test_report_card_formatting():
    """Verify ASCII report card string formatting."""
    student = Student(101, "Ihsan Ul Haq", 20, "AI-101", {"Math": 90.0, "Python": 100.0})
    card = format_report_card(student)
    assert "OFFICIAL STUDENT REPORT CARD" in card
    assert "Ihsan Ul Haq" in card
    assert "A+" in card
    assert "PASSED" in card


def test_ai_comment_offline_and_streaming():
    """Verify AI teacher feedback works 100% offline and streams words."""
    student = Student(101, "Ihsan Ul Haq", 20, "AI-101", {"Math": 95.0, "Python": 98.0})

    # Test feedback generator function
    comment = build_teacher_feedback(student)
    assert isinstance(comment, str)
    assert len(comment) > 10
    assert "Ihsan Ul Haq" in comment

    # Test streaming generator yielding chunks
    stream = generate_teacher_comment_stream(student)
    chunks = list(stream)
    assert len(chunks) > 5
    assembled = "".join(chunks).strip()
    assert assembled == comment.strip()

