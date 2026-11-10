# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
PART 10: ITERATORS, GENERATORS & DECORATORS
This script demonstrates:
- iter() and next()
- Generators and the 'yield' keyword
- Decorators with functools.wraps
- Warm-up: countdown(n) & evens(limit)
- Build: Big File Line Reader & only_errors generator
- Challenge: @timer and @log_calls decorators
"""

import functools
import time
from pathlib import Path

print("=" * 60)
print("PART 10: ITERATORS, GENERATORS & DECORATORS")
print("=" * 60)

# =========================================================================
# 1. WARM-UP — Countdown & Evens Generators
# =========================================================================
print("\n" + "=" * 40)
print("1. WARM-UP: GENERATORS WITH 'yield'")
print("=" * 40)


def countdown(n: int):
    """Yield countdown values from n down to 1."""
    while n > 0:
        yield n
        n -= 1


def evens(limit: int):
    """Yield even numbers from 0 up to limit."""
    num = 0
    while num <= limit:
        yield num
        num += 2


print("Countdown from 5:")
for count in countdown(5):
    print(f"  {count}...", end=" ")
print("Done!")

print(f"\nEvens up to 10: {list(evens(10))}")

# iter() and next() demonstration
items = ["Python", "AI", "Data"]
it = iter(items)
print(f"next(it) -> {next(it)}")
print(f"next(it) -> {next(it)}")
print(f"next(it) -> {next(it)}")

# =========================================================================
# 2. BUILD — Big File Reader & Filter Generators
# =========================================================================
print("\n" + "=" * 40)
print("2. BUILD: STREAMING FILE GENERATORS")
print("=" * 40)

# Generate a sample log file
log_path = Path("server.log")
with open(log_path, "w", encoding="utf-8") as f:
    for i in range(1, 60):
        if i % 7 == 0:
            f.write(f"Line {i}: ERROR Database connection timeout\n")
        else:
            f.write(f"Line {i}: INFO Server operating nominally\n")


def read_lines(path: Path):
    """Streams file line by line without loading the whole file into memory."""
    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            yield line.strip()


def only_errors(lines):
    """Streams only lines containing 'ERROR'."""
    for line in lines:
        if "ERROR" in line:
            yield line


# Count error lines without building a list in memory
error_count = sum(1 for _ in only_errors(read_lines(log_path)))
print(f"Total error lines counted lazily from '{log_path}': {error_count}")

# =========================================================================
# 3. CHALLENGE — Custom Decorators (@timer and @log_calls)
# =========================================================================
print("\n" + "=" * 40)
print("3. CHALLENGE: CUSTOM DECORATORS")
print("=" * 40)


def timer(func):
    """Measures the elapsed execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        elapsed = time.perf_counter() - start
        print(f"  [@timer] '{func.__name__}' took {elapsed:.5f}s")
        return result
    return wrapper


def log_calls(func):
    """Logs function name, arguments, and return value."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"  [@log_calls] Calling '{func.__name__}' with args={args}, kwargs={kwargs}")
        result = func(*args, **kwargs)
        print(f"  [@log_calls] '{func.__name__}' returned {result}")
        return result
    return wrapper


@timer
@log_calls
def sum_to_n(limit: int) -> int:
    """Calculates sum of numbers from 1 to limit."""
    return sum(range(1, limit + 1))


print("Executing decorated sum function:")
result = sum_to_n(1_000_000)
print(f"Sum of 1 to 1,000,000 = {result}")
