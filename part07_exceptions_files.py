# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
PART 7: EXCEPTIONS & FILES
This script demonstrates:
- try, except, else, finally
- ValueError, ZeroDivisionError, FileNotFoundError
- Raising exceptions
- File modes: 'w', 'a', 'r', and context managers (with open)
- Warm-up: Safe Division Loop
- Build: Daily Diary App (appends date and note)
- Challenge: CSV and JSON Result Sheet Export & Read Back
"""

import csv
import datetime
import json
from pathlib import Path

print("=" * 60)
print("PART 7: EXCEPTIONS AND FILE HANDLING")
print("=" * 60)

# =========================================================================
# 1. WARM-UP — Safe Division (Handles ValueError & ZeroDivisionError)
# =========================================================================
print("\n" + "=" * 40)
print("1. WARM-UP: SAFE DIVISION")
print("=" * 40)


def safe_divide(num_str: str, den_str: str) -> float | None:
    """Safely divides two number strings with error handling."""
    try:
        n = float(num_str)
        d = float(den_str)
        result = n / d
    except ValueError as e:
        print(f"  [ValueError] Inputs must be valid numbers! ({e})")
        return None
    except ZeroDivisionError as e:
        print(f"  [ZeroDivisionError] Cannot divide by zero! ({e})")
        return None
    else:
        print(f"  Division successful: {n} / {d} = {result:.2f}")
        return result
    finally:
        print("  [Finally] Division attempt block ended.")


print("Test 1: Valid numbers (20 / 4)")
safe_divide("20", "4")

print("\nTest 2: Division by zero (15 / 0)")
safe_divide("15", "0")

print("\nTest 3: Non-numeric input ('abc' / 5)")
safe_divide("abc", "5")

# =========================================================================
# 2. BUILD — Daily Diary (Appends to diary.txt with Date)
# =========================================================================
print("\n" + "=" * 40)
print("2. BUILD: DAILY DIARY")
print("=" * 40)

diary_file = Path("diary.txt")
today_date = datetime.date.today()

# Append today's entry
new_entry = f"[{today_date}] Completed Part 7 of the Python Mastery Assignment."
with open(diary_file, "a", encoding="utf-8") as file:
    file.write(new_entry + "\n")
print(f"Appended entry to '{diary_file}'.")

# Read all past entries safely
print(f"\nPast entries in '{diary_file}':")
try:
    with open(diary_file, "r", encoding="utf-8") as file:
        entries = file.readlines()
        for idx, line in enumerate(entries, start=1):
            print(f"  Entry #{idx}: {line.strip()}")
except FileNotFoundError:
    print("No entries yet.")

# Missing file test
print("\nReading non-existent file gracefully:")
missing_path = Path("non_existent_file.txt")
try:
    with open(missing_path, "r", encoding="utf-8") as file:
        file.read()
except FileNotFoundError as err:
    print(f"  Caught expected error: '{missing_path}' not found. ({err})")

# =========================================================================
# 3. CHALLENGE — CSV & JSON Result Sheet Persistence
# =========================================================================
print("\n" + "=" * 40)
print("3. CHALLENGE: CSV & JSON RESULT SHEET")
print("=" * 40)

student_data = [
    {"Name": "Ali Raza", "Subject1": 80, "Subject2": 72, "Subject3": 91, "Average": 81.0},
    {"Name": "Sara Khan", "Subject1": 95, "Subject2": 88, "Subject3": 90, "Average": 91.0},
    {"Name": "Ihsan Ul Haq", "Subject1": 92, "Subject2": 94, "Subject3": 96, "Average": 94.0},
]

csv_file = Path("results.csv")
json_file = Path("results.json")

# 1. Write to CSV
with open(csv_file, "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["Name", "Subject1", "Subject2", "Subject3", "Average"])
    writer.writeheader()
    writer.writerows(student_data)
print(f"Saved records to '{csv_file}'.")

# 2. Write to JSON
with open(json_file, "w", encoding="utf-8") as f:
    json.dump(student_data, f, indent=4)
print(f"Saved records to '{json_file}'.")

# 3. Read back CSV and identify the topper
print("\nReading back results from CSV to find class topper:")
with open(csv_file, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    topper = None
    max_avg = -1.0
    for row in reader:
        avg = float(row["Average"])
        if avg > max_avg:
            max_avg = avg
            topper = row["Name"]

print(f"Class Topper identified from CSV: {topper} with an average of {max_avg}%")
