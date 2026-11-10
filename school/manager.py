# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
School Manager Controller.
Coordinates student registry, ranking, CRUD operations, and file storage.
"""

from pathlib import Path
from typing import Optional, Union

from school.models import Student
from school.storage import load_students, save_students


class SchoolManager:
    """Manages school operations including enrollment, records, and rankings."""

    def __init__(self, storage_path: Union[str, Path] = "data/students.json") -> None:
        self.storage_path = Path(storage_path)
        # Internal dictionary mapping student_id -> Student object
        self._students: dict[int, Student] = {}

    @property
    def student_count(self) -> int:
        """Return the number of students currently registered."""
        return len(self._students)

    def add_student(self, student: Student) -> bool:
        """Add a new student to the registry.

        Returns True if added successfully, False if student_id already exists.
        """
        if student.student_id in self._students:
            return False
        self._students[student.student_id] = student
        return True

    def get_student(self, student_id: int) -> Optional[Student]:
        """Fetch a student by ID, or None if not found."""
        return self._students.get(student_id)

    def search_students(self, query: str) -> list[Student]:
        """Search students by ID or substring in student name (case-insensitive)."""
        clean_query = query.strip().lower()
        results: list[Student] = []

        for student in self._students.values():
            if clean_query == str(student.student_id):
                results.append(student)
            elif clean_query in student.name.lower():
                results.append(student)

        return results

    def update_student(
        self,
        student_id: int,
        name: Optional[str] = None,
        age: Optional[int] = None,
        class_name: Optional[str] = None,
        marks: Optional[dict[str, float]] = None,
    ) -> bool:
        """Update fields for an existing student.

        Returns True on success, False if student does not exist.
        """
        student = self._students.get(student_id)
        if not student:
            return False

        if name is not None:
            clean_name = name.strip()
            if not clean_name:
                raise ValueError("Updated name cannot be empty.")
            student.name = clean_name

        if age is not None:
            if not (5 <= age <= 100):
                raise ValueError("Age must be between 5 and 100.")
            student.age = age

        if class_name is not None:
            clean_class = class_name.strip()
            if not clean_class:
                raise ValueError("Class name cannot be empty.")
            student.class_name = clean_class

        if marks is not None:
            # Re-validates marks through model logic
            for sub, score in marks.items():
                if not (0 <= score <= 100):
                    raise ValueError(f"Score for {sub} must be 0-100.")
            student.marks = marks

        return True

    def delete_student(self, student_id: int) -> bool:
        """Remove a student from the system by ID.

        Returns True if deleted, False if not found.
        """
        if student_id in self._students:
            del self._students[student_id]
            return True
        return False

    def list_students(self) -> list[Student]:
        """Return a list of all students sorted by student ID."""
        return sorted(self._students.values(), key=lambda s: s.student_id)

    def get_class_ranking(self) -> list[tuple[int, Student]]:
        """Rank students based on average marks (highest average gets Rank 1).

        Returns a list of tuples: [(rank, Student), ...].
        """
        # Sort descending by average marks, tie-break by name
        sorted_students = sorted(
            self._students.values(),
            key=lambda s: (s.average, s.total_marks),
            reverse=True,
        )

        rankings: list[tuple[int, Student]] = []
        for rank, student in enumerate(sorted_students, start=1):
            rankings.append((rank, student))
        return rankings

    def save_to_disk(self) -> bool:
        """Persist current student records to the configured JSON file."""
        return save_students(list(self._students.values()), self.storage_path)

    def load_from_disk(self) -> int:
        """Load student records from the configured JSON file into memory.

        Returns the number of students loaded.
        """
        loaded = load_students(self.storage_path)
        self._students.clear()
        for s in loaded:
            self._students[s.student_id] = s
        return len(self._students)

