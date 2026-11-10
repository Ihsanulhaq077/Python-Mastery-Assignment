# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
School Package Initialization
Exposes the primary classes and utilities for the School Manager application.
"""

from school.models import Student
from school.manager import SchoolManager
from school.storage import save_students, load_students
from school.utils import calculate_grade, format_report_card

__all__ = [
    "Student",
    "SchoolManager",
    "save_students",
    "load_students",
    "calculate_grade",
    "format_report_card",
]

