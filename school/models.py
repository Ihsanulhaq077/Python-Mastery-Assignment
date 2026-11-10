# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
Data models for the School Management System.
Defines the Student dataclass with type hints and validation.
"""

from dataclasses import dataclass, field
from typing import Any


@dataclass
class Student:
    """Represents a student enrolled in the school."""

    student_id: int
    name: str
    age: int
    class_name: str
    marks: dict[str, float] = field(default_factory=dict)

    def __post_init__(self) -> None:
        """Validate student fields upon instantiation."""
        if not isinstance(self.student_id, int) or self.student_id <= 0:
            raise ValueError(f"Student ID must be a positive integer, got: {self.student_id}")

        clean_name = str(self.name).strip()
        if not clean_name:
            raise ValueError("Student name cannot be empty.")
        self.name = clean_name

        if not isinstance(self.age, int) or not (5 <= self.age <= 100):
            raise ValueError(f"Student age must be between 5 and 100, got: {self.age}")

        clean_class = str(self.class_name).strip()
        if not clean_class:
            raise ValueError("Class name cannot be empty.")
        self.class_name = clean_class

        # Validate marks dictionary
        if not isinstance(self.marks, dict):
            raise TypeError("Marks must be a dictionary of subject -> score.")

        validated_marks: dict[str, float] = {}
        for subject, score in self.marks.items():
            sub_name = str(subject).strip()
            if not sub_name:
                raise ValueError("Subject name cannot be empty.")
            try:
                num_score = float(score)
            except (ValueError, TypeError):
                raise ValueError(f"Mark for '{sub_name}' must be numeric, got: {score}")

            if not (0.0 <= num_score <= 100.0):
                raise ValueError(f"Mark for '{sub_name}' must be between 0 and 100, got: {num_score}")
            validated_marks[sub_name] = num_score

        self.marks = validated_marks

    @property
    def total_marks(self) -> float:
        """Calculate and return the sum of all subject marks."""
        return sum(self.marks.values())

    @property
    def average(self) -> float:
        """Calculate and return arithmetic average score."""
        if not self.marks:
            return 0.0
        return self.total_marks / len(self.marks)

    @property
    def percentage(self) -> float:
        """Calculate overall percentage (equivalent to average on 100 scale)."""
        return self.average

    @property
    def grade(self) -> str:
        """Determine letter grade according to the official school grading scale:

        90 - 100 : A+
        80 - 89  : A
        70 - 79  : B
        60 - 69  : C
        50 - 59  : D
        Below 50 : F
        """
        avg = self.average
        if avg >= 90.0:
            return "A+"
        elif avg >= 80.0:
            return "A"
        elif avg >= 70.0:
            return "B"
        elif avg >= 60.0:
            return "C"
        elif avg >= 50.0:
            return "D"
        return "F"

    @property
    def is_passed(self) -> bool:
        """Returns True if the student passes overall (average >= 50.0)."""
        return self.average >= 50.0

    def to_dict(self) -> dict[str, Any]:
        """Convert Student object into a JSON-serializable dictionary."""
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "class_name": self.class_name,
            "marks": self.marks,
        }

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> "Student":
        """Instantiate a Student object from a dictionary."""
        return cls(
            student_id=int(data["student_id"]),
            name=str(data["name"]),
            age=int(data["age"]),
            class_name=str(data.get("class_name", "General")),
            marks={str(k): float(v) for k, v in data.get("marks", {}).items()},
        )

