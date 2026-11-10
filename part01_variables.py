# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
PART 1: VARIABLES, DATA TYPES, INPUT & OUTPUT
This script demonstrates:
- Primitive data types: str, int, float, bool
- type() and type conversions
- Arithmetic operators (+, -, *, /, //, %, **)
- Formatted strings (f-strings)
- Warm-up: Student ID Card
- Build: Shop Bill Calculator
- Challenge: Unit Converter (Celsius/Fahrenheit, km/miles)
"""

print("=" * 60)
print("PART 1: VARIABLES, DATA TYPES, AND INPUT/OUTPUT")
print("=" * 60)


def safe_input(prompt: str, default: str) -> str:
    """Helper to safely read user input with a fallback default."""
    try:
        user_val = input(f"{prompt} [Default: {default}]: ").strip()
        return user_val if user_val else default
    except EOFError:
        return default


# =========================================================================
# 1. WARM-UP — Student ID Card & Type Inspection
# =========================================================================
print("\n" + "=" * 40)
print("1. WARM-UP: STUDENT ID CARD & TYPES")
print("=" * 40)

student_name = safe_input("Enter Student Name", "Ihsan Ul Haq")
student_age = int(safe_input("Enter Student Age", "20"))
student_class = safe_input("Enter Class/Cohort", "AI 1st Year")
student_city = safe_input("Enter City", "Peshawar")
is_active = True

print("\n======== STUDENT CARD ========")
print(f"Name : {student_name}")
print(f"Age  : {student_age}")
print(f"Class: {student_class}")
print(f"City : {student_city}")
print("==============================")
print(f"Type of student_name  : {type(student_name).__name__}")
print(f"Type of student_age   : {type(student_age).__name__}")
print(f"Type of student_class : {type(student_class).__name__}")
print(f"Type of is_active     : {type(is_active).__name__}")

# =========================================================================
# 2. BUILD — Shop Bill Calculator
# =========================================================================
print("\n" + "=" * 40)
print("2. BUILD: SHOP BILL CALCULATOR")
print("=" * 40)

item_name = safe_input("Enter Item Name", "Python Programming Textbook")
item_price = float(safe_input("Enter Unit Price (Rs)", "1200.0"))
item_qty = int(safe_input("Enter Quantity", "2"))

subtotal = item_price * item_qty
discount = subtotal * 0.05                 # 5% discount
discounted_amount = subtotal - discount
tax = discounted_amount * 0.17              # 17% tax on discounted amount
final_total = discounted_amount + tax

print("\n========= SHOP BILL =========")
print(f"Item      : {item_name}")
print(f"Price/Qty : Rs {item_price:.2f} x {item_qty}")
print(f"Subtotal  : Rs {subtotal:.2f}")
print(f"Discount  : Rs {discount:.2f} (5%)")
print(f"Tax (17%) : Rs {tax:.2f}")
print(f"Final     : Rs {final_total:.2f}")
print("==============================")

# =========================================================================
# 3. CHALLENGE — Unit Converter
# =========================================================================
print("\n" + "=" * 40)
print("3. CHALLENGE: UNIT CONVERTER")
print("=" * 40)

celsius = float(safe_input("Enter Temperature in Celsius", "25.0"))
km = float(safe_input("Enter Distance in Kilometres", "10.0"))

fahrenheit = (celsius * 9 / 5) + 32
kelvin = celsius + 273.15
miles = km * 0.621371
metres = km * 1000

print("\n--- Converted Results ---")
print(f"Temperature: {celsius:.1f} °C = {fahrenheit:.1f} °F | {kelvin:.1f} K")
print(f"Distance   : {km:.1f} km  = {miles:.1f} miles | {metres:.1f} m")

# =========================================================================
# 4. Interactive Student Portal & Calculations
# =========================================================================
print("\n" + "=" * 40)
print("4. STUDENT MARKS & PERCENTAGE SUMMARY")
print("=" * 40)

obtained_marks = float(safe_input("Enter Obtained Marks (out of 500)", "435.0"))
total_marks = 500.0
percentage = (obtained_marks / total_marks) * 100
has_passed = percentage >= 50.0

print("\n======== RESULT CARD ========")
print(f"Student Name   : {student_name}")
print(f"Marks Obtained : {obtained_marks:.1f} / {total_marks:.1f}")
print(f"Percentage     : {percentage:.2f}%")
print(f"Status         : {'PASSED' if has_passed else 'FAILED'}")
print("=============================")
