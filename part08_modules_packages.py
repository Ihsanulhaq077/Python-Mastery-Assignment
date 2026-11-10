# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
PART 8: MODULES, PACKAGES & PROJECTS
This script demonstrates:
- Module import mechanisms: 'import ...' and 'from ... import ...'
- Python Standard Library modules:
    * math (sqrt, ceil, floor, pi)
    * random (choice, randint, shuffle)
    * datetime (dates, date arithmetic, days to Dec 31)
    * statistics (mean, median)
- Creating and importing custom modules (school_calculator.py)
- The 'if __name__ == "__main__":' execution guard
"""

import datetime
import math
import random
import statistics

# Custom user module import
import school_calculator
from school_calculator import calculate_gpa, format_currency

print("=" * 60)
print("PART 8: MODULES AND PACKAGES")
print("=" * 60)

# =========================================================================
# 1. WARM-UP — Standard Library Tour
# =========================================================================
print("\n" + "=" * 40)
print("1. WARM-UP: STANDARD LIBRARY TOUR")
print("=" * 40)

# math module
print(f"Square root of 144            : {math.sqrt(144)}")

# random module
candidates = ["Ali", "Sara", "Ihsan", "Zainab", "Bilal"]
print(f"Randomly chosen class monitor : {random.choice(candidates)}")

# datetime module: Days until Dec 31
today = datetime.date.today()
dec_31 = datetime.date(today.year, 12, 31)
days_remaining = (dec_31 - today).days
print(f"Days left until 31 December   : {days_remaining} days")

# statistics module: Mean and median of 5 marks
marks = [75, 88, 92, 64, 80]
print(f"Sample marks                  : {marks}")
print(f"Statistics Mean (Average)     : {statistics.mean(marks):.2f}")
print(f"Statistics Median             : {statistics.median(marks):.2f}")

# =========================================================================
# 2. BUILD — Custom Module Integration (school_calculator.py)
# =========================================================================
print("\n" + "=" * 40)
print("2. BUILD: CUSTOM MODULE USAGE")
print("=" * 40)

score = 86.5
fee = 45000.0

converted_gpa = calculate_gpa(score)
formatted_fee = format_currency(fee)

print(f"Score: {score}% -> Converted GPA: {converted_gpa} / 4.0")
print(f"Tuition Fee: {formatted_fee}")
print(f"Direct module prefix call: {school_calculator.format_currency(15000)}")

# =========================================================================
# 3. Execution Namespace Explanation
# =========================================================================
print("\n" + "=" * 40)
print("3. EXECUTION NAMESPACE (__name__)")
print("=" * 40)
print(f"Current script __name__  : '{__name__}'")
print(f"Imported module __name__ : '{school_calculator.__name__}'")
print("Note: The test block in school_calculator.py did not run upon import.")
