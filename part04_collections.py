# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
PART 4: COLLECTIONS (Lists, Tuples, Sets, Dictionaries)
This script demonstrates:
- Lists: mutable, ordered, indexing, slicing, enumerate()
- Tuples: immutable, ordered, unpacking
- Sets: unique elements, set operations (union, intersection, difference)
- Dictionaries: key-value pairs, get(), keys(), values(), items()
- Warm-up: Shopping list with enumerate
- Build: Phone book dictionary system
- Challenge: Class result sheet with topper & low score detection (< 40)
"""

print("=" * 60)
print("PART 4: PYTHON COLLECTIONS")
print("=" * 60)

# =========================================================================
# 1. WARM-UP — Shopping List (List with Enumerate)
# =========================================================================
print("\n" + "=" * 40)
print("1. WARM-UP: SHOPPING LIST (Lists & enumerate)")
print("=" * 40)

items = ["milk", "bread", "eggs"]
print(f"Initial list: {items}")

items.append("tea")       # Add tea
items.remove("bread")     # Remove bread
items.sort()              # Alphabetical sort

print("Numbered Shopping List:")
for index, item in enumerate(items, start=1):
    print(f"  {index}. {item}")

# Tuple Demonstration (Immutability & Unpacking)
location_coordinates = (34.0151, 71.5249)  # Latitude, Longitude of Peshawar
lat, lon = location_coordinates
print(f"\nTuple location coordinates: Latitude={lat}, Longitude={lon}")

# =========================================================================
# 2. BUILD — Phone Book (Dictionary with Safe Access)
# =========================================================================
print("\n" + "=" * 40)
print("2. BUILD: PHONE BOOK DIRECTORY (Dictionaries)")
print("=" * 40)

phone_book: dict[str, str] = {
    "Ali Raza": "0300-1234567",
    "Sara Khan": "0311-2345678",
    "Ihsan Ul Haq": "0333-3456789",
    "Bilal Ahmad": "0345-4567890",
    "Zainab Bibi": "0321-5678901",
}

# 1) Add contact
phone_book["Hamza Tariq"] = "0302-9876543"

# 2) Safe search using .get()
search_name = "Sara Khan"
print(f"Searching for '{search_name}': {phone_book.get(search_name, 'Not found')}")

missing_search = "Kamran"
print(f"Searching for '{missing_search}': {phone_book.get(missing_search, 'Not found')}")

# 3) Delete contact
deleted_num = phone_book.pop("Bilal Ahmad", None)
print(f"Deleted contact 'Bilal Ahmad' ({deleted_num})")

# 4) Show all contacts
print("\nAll Contacts Directory:")
for name, number in sorted(phone_book.items()):
    print(f"  {name:<16} : {number}")

# =========================================================================
# 3. CHALLENGE — Class Result Sheet with Topper & Weak Subject Set
# =========================================================================
print("\n" + "=" * 40)
print("3. CHALLENGE: CLASS RESULT SHEET")
print("=" * 40)

student_scores: dict[str, list[float]] = {
    "Ali": [80.0, 72.0, 91.0],
    "Sara": [95.0, 88.0, 90.0],
    "Ihsan": [92.0, 94.0, 96.0],
    "Bilal": [38.0, 45.0, 50.0],
    "Zainab": [65.0, 55.0, 70.0],
}

topper_name = ""
highest_avg = -1.0
students_below_40: set[str] = set()

print(f"{'Student':<12}{'Total':<10}{'Average':<10}{'Status'}")
print("-" * 44)

for student, scores in student_scores.items():
    tot = sum(scores)
    avg = tot / len(scores)

    # Check for scores below 40
    if any(s < 40 for s in scores):
        students_below_40.add(student)

    # Check topper
    if avg > highest_avg:
        highest_avg = avg
        topper_name = student

    status = "Review" if student in students_below_40 else "Good"
    print(f"{student:<12}{tot:<10.1f}{avg:<10.2f}{status}")

print("-" * 44)
print(f"Class Topper : {topper_name} with an average of {highest_avg:.2f}%")
print(f"Students with any score below 40 (Set): {students_below_40}")

# Set Math Demonstration
semester_1 = {"Python", "Calculus", "Logic"}
semester_2 = {"Python", "AI", "Databases"}
print(f"\nUnique courses in common (Intersection): {semester_1 & semester_2}")
print(f"All distinct courses (Union)           : {semester_1 | semester_2}")
