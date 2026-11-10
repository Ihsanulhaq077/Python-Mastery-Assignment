# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
PART 2: CONDITIONS (if / elif / else)
This script demonstrates:
- if, elif, else branch execution
- Comparison operators (==, !=, <, >, <=, >=)
- Logical operators (and, or, not)
- Nested conditions
- Warm-up: Even, Odd, and Sign Detector
- Build: Student Grade Calculator with Input Validation
- Challenge: Tiered Electricity Bill Calculator with Boundary Testing
"""

print("=" * 60)
print("PART 2: CONDITIONAL STATEMENTS & DECISION MAKING")
print("=" * 60)


def safe_input(prompt: str, default: str) -> str:
    """Helper to safely read user input with a fallback default."""
    try:
        user_val = input(f"{prompt} [Default: {default}]: ").strip()
        return user_val if user_val else default
    except EOFError:
        return default


# =========================================================================
# 1. WARM-UP — Even, Odd and Sign Detector
# =========================================================================
print("\n" + "=" * 40)
print("1. WARM-UP: NUMBER SIGN & PARITY")
print("=" * 40)

number_str = safe_input("Enter a whole number to analyze", "14")
number = int(number_str)

# Checking sign (positive, negative, or zero)
if number > 0:
    sign_msg = "Positive"
elif number < 0:
    sign_msg = "Negative"
else:
    sign_msg = "Zero"

# Nested condition for even or odd
if number != 0:
    if number % 2 == 0:
        parity_msg = "Even"
    else:
        parity_msg = "Odd"
else:
    parity_msg = "Neither Even nor Odd (Zero)"

print(f"Analysis for {number}: {sign_msg} and {parity_msg}")

# =========================================================================
# 2. BUILD — Grade Calculator with Validation
# =========================================================================
print("\n" + "=" * 40)
print("2. BUILD: GRADE CALCULATOR")
print("=" * 40)


def calculate_grade(marks: float) -> str:
    """Determine letter grade according to the academic scale:
    90-100 = A+
    80-89  = A
    70-79  = B
    60-69  = C
    50-59  = D
    Below 50 = F
    """
    if marks < 0 or marks > 100:
        return "Invalid marks (Must be 0 - 100)"

    if marks >= 90:
        return "A+"
    elif marks >= 80:
        return "A"
    elif marks >= 70:
        return "B"
    elif marks >= 60:
        return "C"
    elif marks >= 50:
        return "D"
    else:
        return "F"


marks_input = safe_input("Enter student marks out of 100", "88.5")
try:
    marks = float(marks_input)
    print(f"Marks: {marks:.1f} -> Official Grade: {calculate_grade(marks)}")
except ValueError:
    print("Error: Invalid numeric input entered.")

# =========================================================================
# 3. CHALLENGE — Tiered Electricity Bill Calculator
# =========================================================================
print("\n" + "=" * 40)
print("3. CHALLENGE: ELECTRICITY BILL CALCULATOR")
print("=" * 40)


def calculate_electricity_bill(units: int) -> float:
    """Calculates electricity bill based on tiered tariff rates:
    - First 100 units: Rs 10 per unit
    - Next 100 units (101-200): Rs 15 per unit
    - Above 200 units: Rs 20 per unit
    - Fixed charges: Rs 50
    """
    if units < 0:
        raise ValueError("Units cannot be negative.")

    fixed_charges = 50.0
    energy_charges = 0.0

    if units <= 100:
        energy_charges = units * 10.0
    elif units <= 200:
        # First 100 at 10, remaining at 15
        energy_charges = (100 * 10.0) + ((units - 100) * 15.0)
    else:
        # First 100 at 10, next 100 at 15, remaining at 20
        energy_charges = (100 * 10.0) + (100 * 15.0) + ((units - 200) * 20.0)

    return energy_charges + fixed_charges


units_input = safe_input("Enter units consumed", "250")
try:
    units = int(units_input)
    bill = calculate_electricity_bill(units)
    print(f"Electricity Bill for {units} units: Rs {bill:,.2f}")
except ValueError as e:
    print(f"Error: {e}")

# Boundary Verification (Testing edge values: 0, 100, 101, 200, 201)
print("\nBoundary Testing (Edge Verification):")
for test_unit in [0, 100, 101, 200, 201, 250]:
    b = calculate_electricity_bill(test_unit)
    print(f"  {test_unit:>3} units -> Rs {b:>7.2f}")
