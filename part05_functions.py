# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
PART 5: FUNCTIONS & COMPREHENSIONS
This script demonstrates:
- Function definitions, arguments, return values, and defaults
- *args and **kwargs
- Lambda functions
- Warm-up: Small helpers (area_of_circle, is_even, multilingual greet)
- Build: Academic Marks Toolkit (average, grade, one-line report)
- Challenge: List, Dictionary, and Set Comprehensions
"""

import math

print("=" * 60)
print("PART 5: FUNCTIONS AND COMPREHENSIONS")
print("=" * 60)

# =========================================================================
# 1. WARM-UP — Small Helpers
# =========================================================================
print("\n" + "=" * 40)
print("1. WARM-UP: SMALL HELPER FUNCTIONS")
print("=" * 40)


def area_of_circle(radius: float) -> float:
    """Calculate the area of a circle (pi * r^2)."""
    return math.pi * (radius ** 2)


def is_even(number: int) -> bool:
    """Check if a number is even."""
    return number % 2 == 0


def greet(name: str, lang: str = "en") -> str:
    """Multilingual greeting function supporting English and Urdu."""
    if lang.lower() == "ur":
        return f"Assalam-o-Alaikum, {name}!"
    return f"Hello, {name}!"


# Call each function three times
print("Testing area_of_circle:")
for r in [1.0, 3.5, 7.0]:
    print(f"  Radius {r:>3} -> Area = {area_of_circle(r):.2f}")

print("\nTesting is_even:")
for n in [4, 7, 10]:
    print(f"  Is {n} even? {is_even(n)}")

print("\nTesting greet:")
print(" ", greet("Ihsan", "en"))
print(" ", greet("Ihsan", "ur"))
print(" ", greet("Sara"))

# =========================================================================
# 2. BUILD — Marks Toolkit
# =========================================================================
print("\n" + "=" * 40)
print("2. BUILD: MARKS TOOLKIT")
print("=" * 40)


def calculate_average(marks: list[float]) -> float:
    """Returns arithmetic average score."""
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def calculate_grade(avg: float) -> str:
    """Converts average to official letter grade."""
    if avg >= 90:
        return "A+"
    elif avg >= 80:
        return "A"
    elif avg >= 70:
        return "B"
    elif avg >= 60:
        return "C"
    elif avg >= 50:
        return "D"
    return "F"


def is_passed(avg: float, passing_mark: float = 50.0) -> bool:
    """Determines passing status."""
    return avg >= passing_mark


def report(name: str, marks: list[float]) -> str:
    """Generates a clean one-line academic summary string."""
    avg = calculate_average(marks)
    grd = calculate_grade(avg)
    status = "Passed" if is_passed(avg) else "Failed"
    return f"Student: {name:<12} | Avg: {avg:>6.2f}% | Grade: {grd:<2} | Status: {status}"


# Testing on 3 students
student_batch = [
    ("Ali Raza", [85.0, 78.0, 92.0]),
    ("Sara Khan", [94.0, 91.0, 96.0]),
    ("Bilal Ahmad", [45.0, 48.0, 52.0]),
]

print("One-Line Reports:")
for s_name, s_marks in student_batch:
    print(" ", report(s_name, s_marks))

# =========================================================================
# 3. CHALLENGE — Comprehensions (In One Line Each)
# =========================================================================
print("\n" + "=" * 40)
print("3. CHALLENGE: ONE-LINE COMPREHENSIONS")
print("=" * 40)

# 1. Squares of numbers 1-10
squares = [x ** 2 for x in range(1, 11)]
print(f"Squares 1-10              : {squares}")

# 2. Names longer than 4 letters from a list
raw_names = ["Ali", "Sara", "Zainab", "Hamza", "Ihsan", "Bob"]
long_names = [name for name in raw_names if len(name) > 4]
print(f"Names > 4 letters         : {long_names}")

# 3. Dict of {name: average} from class records
class_records = {
    "Ali": [80.0, 85.0, 90.0],
    "Sara": [95.0, 92.0, 98.0],
    "Zaid": [45.0, 50.0, 48.0],
}
averages_map = {name: round(sum(scores) / len(scores), 2) for name, scores in class_records.items()}
print(f"Dict of Averages          : {averages_map}")

# 4. Filter only passing students (average >= 50)
passing_names = [name for name, avg in averages_map.items() if avg >= 50.0]
print(f"Passing Students Only     : {passing_names}")

# Extra: Lambda and *args / **kwargs demo
print("\nLambda & Variable Arguments:")
get_gpa = lambda pct: round((pct / 100) * 4.0, 2)
print(f"Percentage 85% to GPA     : {get_gpa(85)}")
