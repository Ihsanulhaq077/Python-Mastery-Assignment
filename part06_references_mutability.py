# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
PART 6: REFERENCES AND MUTABILITY
This script demonstrates:
- Object references and memory addresses via id()
- Identity comparison ('is') vs Value comparison ('==')
- Mutable objects (list, dict, set) vs Immutable objects (int, str, tuple)
- Reference assignment (b = a) vs Shallow Copy (c = a.copy(), d = a[:])
- Deep copy for nested collections (copy.deepcopy)
- Tuple immutability
- The classic mutable default argument trap and its correct fix
"""

import copy

print("=" * 50)
print("PART 6: REFERENCES AND MUTABILITY IN PYTHON")
print("=" * 50)

# -------------------------------------------------------------------------
# 1. Object References and id()
# -------------------------------------------------------------------------
print("\n--- 1. Memory Addresses and Identity ---")
x = 100
y = 100
print(f"x = {x}, id(x) = {id(x)}")
print(f"y = {y}, id(y) = {id(y)}")
print(f"x is y: {x is y} (Python reuses small integer memory locations)")

# -------------------------------------------------------------------------
# 2. Reference Assignment vs Copying Lists
# -------------------------------------------------------------------------
print("\n--- 2. Assignment (Alias) vs .copy() vs Slicing ---")

# Step 1: Assignment creates an alias (both point to same memory address)
a = [1, 2, 3]
b = a  # b references the EXACT same list in memory

print(f"Initial a: {a} (id: {id(a)})")
print(f"Initial b: {b} (id: {id(b)})")
print(f"Are a and b the same object? {a is b}")

# Modifying b modifies a as well!
b.append(4)
print("\nAfter b.append(4):")
print(f"  a = {a}")
print(f"  b = {b}")
print("  Explanation: Because b is just another label for object a, changing b changes a.")

# Step 2: .copy() creates an independent shallow copy
c = a.copy()
c.append(5)
print("\nAfter c = a.copy() and c.append(5):")
print(f"  a = {a} (id: {id(a)})")
print(f"  c = {c} (id: {id(c)})")
print(f"  Are a and c the same object? {a is c}")
print(f"  Do a and c have equal content? {a == c}")
print("  Explanation: c has its own memory address; modifying c does NOT alter a.")

# Step 3: Slicing copy [:]
d = a[:]
print(f"\nSlicing copy d = a[:]: {d} (id: {id(d)})")
print(f"Are a and d same object? {a is d} | Content equal? {a == d}")

# -------------------------------------------------------------------------
# 3. Tuple Immutability
# -------------------------------------------------------------------------
print("\n--- 3. Tuple Immutability ---")
point = (10, 20)
print(f"Tuple point: {point}")
try:
    # Attempting to reassign an element of a tuple will fail
    point[0] = 99
except TypeError as e:
    print(f"Caught expected TypeError on tuple modification: {e}")
    print("Explanation: Tuples are immutable; their elements cannot be reassigned.")

# -------------------------------------------------------------------------
# 4. Shallow Copy vs Deep Copy (Nested Collections)
# -------------------------------------------------------------------------
print("\n--- 4. Nested Collections: Shallow Copy vs Deep Copy ---")
original_classes = {"Section-A": ["Ali", "Sara"]}

# Shallow copy using .copy()
shallow = original_classes.copy()

# Deep copy using copy.deepcopy()
deep = copy.deepcopy(original_classes)

# Modify the nested list inside Section-A
original_classes["Section-A"].append("Zainab")

print(f"Original: {original_classes}")
print(f"Shallow : {shallow}  <-- Affected! (Inner list was shared)")
print(f"Deep    : {deep}     <-- Protected! (Inner list was fully cloned)")

# -------------------------------------------------------------------------
# 5. The Mutable Default Argument Bug & Fix
# -------------------------------------------------------------------------
print("\n--- 5. The Mutable Default Argument Trap ---")


# BUGGY IMPLEMENTATION:
def buggy_enroll(student_name: str, roster: list = []):
    roster.append(student_name)
    return roster


print("Buggy Function Call 1:", buggy_enroll("Hamza"))
print("Buggy Function Call 2:", buggy_enroll("Ayesha"))
print("Notice how Ayesha's roster accidentally included Hamza!")


# FIXED IMPLEMENTATION:
def correct_enroll(student_name: str, roster: list = None):
    # Standard Python idiom: default to None and initialize if None
    if roster is None:
        roster = []
    roster.append(student_name)
    return roster


print("\nFixed Function Call 1:", correct_enroll("Hamza"))
print("Fixed Function Call 2:", correct_enroll("Ayesha"))
print("Notice each call without a roster gets its own brand new list!")

