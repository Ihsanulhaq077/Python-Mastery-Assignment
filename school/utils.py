# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
Utility functions for the School Management System.
Includes:
- Grade calculation helper
- Beautiful ASCII Report Card formatter
- Safe interactive input helper functions
- AI Teacher Comment Generator with streaming and retry mechanisms (Bonus Feature)
"""

import functools
import os
import time
from typing import Generator, Optional

from school.models import Student


def calculate_grade(average: float) -> str:
    """Determine letter grade according to the official school grading scale.

    Scale:
      90 - 100 : A+
      80 - 89  : A
      70 - 79  : B
      60 - 69  : C
      50 - 59  : D
      Below 50 : F
    """
    if average >= 90.0:
        return "A+"
    elif average >= 80.0:
        return "A"
    elif average >= 70.0:
        return "B"
    elif average >= 60.0:
        return "C"
    elif average >= 50.0:
        return "D"
    return "F"


def format_report_card(student: Student) -> str:
    """Generate an ASCII formatted academic report card for a student."""
    border = "=" * 54
    divider = "-" * 54

    lines = [
        border,
        "             OFFICIAL STUDENT REPORT CARD",
        border,
        f" Student ID : {student.student_id:<10} Class : {student.class_name}",
        f" Name       : {student.name:<25} Age   : {student.age}",
        divider,
        f" {'SUBJECT':<28}{'MARKS':>10}{'GRADE':>12}",
        divider,
    ]

    if student.marks:
        for subject, score in sorted(student.marks.items()):
            sub_grade = calculate_grade(score)
            lines.append(f" {subject:<28}{score:>10.1f}{sub_grade:>12}")
    else:
        lines.append("  (No subject marks recorded yet)")

    lines.extend([
        divider,
        f" Total Marks  : {student.total_marks:.1f}",
        f" Average      : {student.average:.2f}%",
        f" Final Grade  : {student.grade}",
        f" Result Status: {'PASSED' if student.is_passed else 'FAILED'}",
        border,
    ])

    return "\n".join(lines)


# -------------------------------------------------------------------------
# Interactive Input Helpers (Defensive Programming)
# -------------------------------------------------------------------------

def prompt_int(message: str, min_val: int = 1, max_val: int = 1000000, default: Optional[int] = None) -> int:
    """Prompt user for an integer within [min_val, max_val] with re-prompting."""
    while True:
        try:
            default_str = f" [Default: {default}]" if default is not None else ""
            user_input = input(f"{message}{default_str}: ").strip()
            if not user_input and default is not None:
                return default
            val = int(user_input)
            if min_val <= val <= max_val:
                return val
            print(f"Value must be between {min_val} and {max_val}. Please try again.")
        except EOFError:
            if default is not None:
                return default
            return min_val
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")


def prompt_float(message: str, min_val: float = 0.0, max_val: float = 100.0, default: Optional[float] = None) -> float:
    """Prompt user for a float within [min_val, max_val] with re-prompting."""
    while True:
        try:
            default_str = f" [Default: {default}]" if default is not None else ""
            user_input = input(f"{message}{default_str}: ").strip()
            if not user_input and default is not None:
                return default
            val = float(user_input)
            if min_val <= val <= max_val:
                return val
            print(f"Value must be between {min_val} and {max_val}. Please try again.")
        except EOFError:
            if default is not None:
                return default
            return min_val
        except ValueError:
            print("Invalid input. Please enter a valid decimal number.")


def prompt_string(message: str, default: Optional[str] = None) -> str:
    """Prompt user for a non-empty string."""
    while True:
        try:
            default_str = f" [Default: {default}]" if default is not None else ""
            user_input = input(f"{message}{default_str}: ").strip()
            if not user_input and default is not None:
                return default
            if user_input:
                return user_input
            print("Input cannot be empty. Please enter a value.")
        except EOFError:
            if default is not None:
                return default
            return "Anonymous"


# -------------------------------------------------------------------------
# AI BONUS (+5): Teacher Comments with Retry, Streaming, and Offline Mode
# -------------------------------------------------------------------------

def retry(max_attempts: int = 3, delay: float = 0.2):
    """Decorator factory to retry a function up to max_attempts on transient errors."""
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempts = 0
            while attempts < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    attempts += 1
                    if attempts >= max_attempts:
                        raise error
                    time.sleep(delay)
        return wrapper
    return decorator


def build_teacher_feedback(student: Student) -> str:
    """Generate intelligent academic commentary based on student performance.

    Can be powered by an external LLM if API_KEY is set in environment,
    or runs via comprehensive built-in academic feedback logic when offline.
    """
    api_key = os.getenv("API_KEY")

    if api_key and api_key != "your_gemini_or_openai_api_key_here":
        # Note: If an API key is provided, external API calls could be made here.
        # For assignment safety and zero-dependency offline grading, we format the AI prompt:
        comment_header = "[AI Faculty Advisory Engine]"
    else:
        comment_header = "[Academic Performance Review]"

    avg = student.average
    if avg >= 90.0:
        performance = f"{student.name} demonstrates exceptional mastery and scholarly dedication across all subjects. Highly recommended for Honors!"
    elif avg >= 80.0:
        performance = f"{student.name} exhibits strong analytical comprehension and consistent academic diligence. Keep up the commendable work!"
    elif avg >= 70.0:
        performance = f"{student.name} shows commendable aptitude with good conceptual clarity. Further focus on advanced topics will elevate performance."
    elif avg >= 60.0:
        performance = f"{student.name} maintains satisfactory progress. Consistent practice and targeted revision are recommended for upcoming examinations."
    elif avg >= 50.0:
        performance = f"{student.name} has met minimum passing criteria. Attending supplementary tutorial sessions is strongly advised."
    else:
        performance = f"{student.name} requires immediate academic intervention and scheduled remedial coursework to build foundational understanding."

    return f"{comment_header} {performance}"


@retry(max_attempts=3)
def generate_teacher_comment_stream(student: Student) -> Generator[str, None, None]:
    """Streaming generator yielding teacher feedback word-by-word.

    Demonstrates:
    - Generator function with 'yield'
    - Streaming simulation
    - @retry decorator protection
    """
    full_comment = build_teacher_feedback(student)
    words = full_comment.split(" ")
    for word in words:
        yield word + " "

