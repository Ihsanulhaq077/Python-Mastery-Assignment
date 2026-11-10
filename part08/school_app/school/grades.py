# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""Grades helper module for school_app."""


def average(marks: list[float]) -> float:
    """Calculate average of marks."""
    return sum(marks) / len(marks) if marks else 0.0


def grade(avg: float) -> str:
    """Determine letter grade."""
    if avg < 0 or avg > 100:
        raise ValueError("Average must be between 0 and 100.")
    if avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 33:
        return "D"
    return "Fail"
