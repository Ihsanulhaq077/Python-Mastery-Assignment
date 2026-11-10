# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""Attendance module for school_app."""


def attendance_percentage(present: int, total: int) -> float:
    """Calculate percentage attendance."""
    if total <= 0:
        raise ValueError("Total days must be greater than zero.")
    if present < 0 or present > total:
        raise ValueError("Present days must be between 0 and total days.")
    return (present / total) * 100
