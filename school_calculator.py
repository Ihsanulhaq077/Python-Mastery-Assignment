# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
CUSTOM HELPER MODULE: school_calculator.py
Demonstrates creating reusable custom module functions.
"""


def calculate_gpa(percentage: float) -> float:
    """Convert a percentage score to a 4.0 GPA scale."""
    if percentage >= 90:
        return 4.0
    elif percentage >= 80:
        return 3.5
    elif percentage >= 70:
        return 3.0
    elif percentage >= 60:
        return 2.5
    elif percentage >= 50:
        return 2.0
    return 0.0


def format_currency(amount: float) -> str:
    """Format a numeric value as Pakistani Rupee currency string."""
    return f"Rs {amount:,.2f}"


if __name__ == "__main__":
    # This block executes ONLY when running school_calculator.py directly,
    # NOT when imported into another file.
    print("[school_calculator] Running self-test...")
    assert calculate_gpa(88) == 3.5
    assert format_currency(1250.5) == "Rs 1,250.50"
    print("[school_calculator] All self-tests passed successfully.")

