# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""School App multi-file modular entry point (Part 8 package demo)."""

from school.grades import average, grade
from school.attendance import attendance_percentage

if __name__ == "__main__":
    print("=" * 45)
    print("  SCHOOL APP (PART 8 MODULAR PACKAGE)")
    print("=" * 45)

    sample_marks = [80.0, 75.0, 90.0]
    avg = average(sample_marks)

    print(f"Sample Marks  : {sample_marks}")
    print(f"Average Score : {avg:.2f}")
    print(f"Letter Grade  : {grade(avg)}")
    print(f"Attendance    : {attendance_percentage(42, 50):.1f}%")
    print("=" * 45)

