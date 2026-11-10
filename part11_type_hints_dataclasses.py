# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
PART 11: TYPE HINTS & DATACLASSES
This script demonstrates:
- Python 3.10+ type hints (list, dict, Optional, Union)
- Function parameter and return type hints
- @dataclass decorator
- field(default_factory=...) and __post_init__ validation
- order=True sortable dataclasses
- Serialization with asdict() and JSON persistence
"""

import json
from dataclasses import asdict, dataclass, field
from pathlib import Path
from typing import Optional

print("=" * 60)
print("PART 11: TYPE HINTS AND DATACLASSES")
print("=" * 60)

# =========================================================================
# 1. WARM-UP — Type Hinted Functions
# =========================================================================
print("\n" + "=" * 40)
print("1. WARM-UP: TYPE HINTED FUNCTIONS")
print("=" * 40)


def calculate_average(marks: list[float]) -> float:
    """Type-annotated average calculation function."""
    if not marks:
        return 0.0
    return sum(marks) / len(marks)


def calculate_grade(average: float) -> str:
    """Type-annotated grade determination."""
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    return "F"


scores: list[float] = [88.5, 92.0, 79.5]
avg: float = calculate_average(scores)
print(f"Scores: {scores} -> Average: {avg:.2f}% | Grade: {calculate_grade(avg)}")

# =========================================================================
# 2. BUILD — Product Dataclass with Validation
# =========================================================================
print("\n" + "=" * 40)
print("2. BUILD: PRODUCT DATACLASS WITH VALIDATION")
print("=" * 40)


@dataclass(order=True)
class Product:
    """Sortable dataclass representing an inventory product."""

    # sort_index allows sorting primarily by price when order=True
    sort_index: float = field(init=False, repr=False)
    name: str
    price: float
    stock: int
    tags: list[str] = field(default_factory=list)

    def __post_init__(self) -> None:
        """Validate non-negative price and stock, and set sort key."""
        if self.price < 0:
            raise ValueError(f"Price cannot be negative, got {self.price}")
        if self.stock < 0:
            raise ValueError(f"Stock cannot be negative, got {self.stock}")
        self.sort_index = self.price


inventory: list[Product] = [
    Product("Python Notebook", 450.0, 25, ["stationery", "school"]),
    Product("Scientific Calculator", 2200.0, 0, ["electronics", "math"]),
    Product("Ballpoint Pen Pack", 150.0, 50, ["stationery"]),
    Product("Laptop Sleeve", 1800.0, 0, ["accessories"]),
    Product("USB Flash Drive 64GB", 1200.0, 15, ["storage", "electronics"]),
]

print("Out of Stock Products:")
for item in inventory:
    if item.stock == 0:
        print(f"  * {item.name} (Price: Rs {item.price:,.2f})")

# =========================================================================
# 3. CHALLENGE — Save to JSON & Load Back into Dataclass Objects
# =========================================================================
print("\n" + "=" * 40)
print("3. CHALLENGE: DATACLASS JSON PERSISTENCE & SORTING")
print("=" * 40)

json_path = Path("products.json")

# 1. Save to JSON using asdict
product_dicts = [asdict(p) for p in inventory]
with open(json_path, "w", encoding="utf-8") as f:
    json.dump(product_dicts, f, indent=4)
print(f"Saved {len(inventory)} products to '{json_path}'.")

# 2. Load back from JSON into Product instances
with open(json_path, "r", encoding="utf-8") as f:
    loaded_raw = json.load(f)

# Reconstruct Product objects using dictionary unpacking (**d)
reconstructed_products = [
    Product(name=d["name"], price=d["price"], stock=d["stock"], tags=d["tags"])
    for d in loaded_raw
]

# 3. Sort by price (order=True uses sort_index = price)
reconstructed_products.sort()

print("\nProducts Sorted by Price (Lowest to Highest):")
for p in reconstructed_products:
    print(f"  Rs {p.price:>7.2f} | {p.name:<25} | Stock: {p.stock}")

# =========================================================================
# 4. Student Dataclass Representation
# =========================================================================
print("\n" + "=" * 40)
print("4. STUDENT DATACLASS")
print("=" * 40)


@dataclass
class Student:
    student_id: int
    name: str
    age: int
    marks: dict[str, float] = field(default_factory=dict)
    remarks: Optional[str] = None

    @property
    def average(self) -> float:
        return sum(self.marks.values()) / len(self.marks) if self.marks else 0.0


std = Student(101, "Ihsan Ul Haq", 20, {"AI": 95.0, "Python": 98.0}, "Distinction")
print(f"Student: {std.name} | Average: {std.average:.2f}% | Remarks: {std.remarks}")
