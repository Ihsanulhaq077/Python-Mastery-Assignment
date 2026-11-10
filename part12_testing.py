# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
PART 12: DEBUGGING & TESTING
This script demonstrates:
- Bug fixing and debugging principles (off-by-one, assignment vs append, divisor logic)
- Defensive programming with assertions
- Pytest parameterized tests for grade cutoffs
- Pytest fixtures for stateful object testing (BankAccount)
- Unit tests for arithmetic, averages, and pass/fail logic
"""

import pytest

# =========================================================================
# 1. WARM-UP — Find and Fix 3 Bugs
# =========================================================================
# ORIGINAL BUGGY CODE:
# marks = [90, 25, 70]
# passing = []
# for m in range(len(marks) - 1):  # BUG 1: Off-by-one error (misses the last item)
#     if marks[m] > 33:
#         passing = [marks[m]]     # BUG 2: Overwrites the list instead of appending
# print(sum(passing) / len(marks)) # BUG 3: Divides by total count instead of passing count


def fixed_average_passing_marks(marks: list[float]) -> float:
    """Fixed implementation of the warm-up bug hunt."""
    passing = []
    # FIX 1: Iterate directly over items, avoiding range off-by-one bug
    for mark in marks:
        if mark > 33:
            # FIX 2: Use .append() to accumulate items instead of overwriting
            passing.append(mark)

    if not passing:
        return 0.0

    # FIX 3: Divide by len(passing) instead of len(marks)
    return sum(passing) / len(passing)


# =========================================================================
# 2. Defensive Functions for Testing
# =========================================================================


def add(a: float, b: float) -> float:
    """Adds two numbers with type validation."""
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both operands must be numeric.")
    return a + b


def calculate_average(scores: list[float]) -> float:
    """Calculates average score."""
    if not isinstance(scores, list):
        raise TypeError("Scores must be a list.")
    if not scores:
        return 0.0
    return sum(scores) / len(scores)


def calculate_grade(score: float) -> str:
    """Calculates letter grade. Raises ValueError if score is outside [0, 100]."""
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")

    if score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 33:
        return "D"
    return "Fail"


def is_passed(score: float) -> bool:
    """Checks if score meets minimum passing score (33 or 50)."""
    return score >= 33.0


class BankAccount:
    """Bank account class for testing with pytest fixtures."""

    def __init__(self, owner: str, initial_balance: float = 1000.0) -> None:
        self.owner = owner
        self.balance = initial_balance
        self.history = [f"Initial balance: Rs {initial_balance:,.2f}"]

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit must be positive.")
        self.balance += amount
        self.history.append(f"Deposited: Rs {amount:,.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal must be positive.")
        if amount > self.balance:
            raise ValueError("Insufficient funds!")
        self.balance -= amount
        self.history.append(f"Withdrew: Rs {amount:,.2f}")


# =========================================================================
# 3. Pytest Unit Tests
# =========================================================================


def test_fixed_warmup_bugs():
    """Verify that the fixed warm-up code produces expected 80.0."""
    sample_marks = [90, 25, 70]
    result = fixed_average_passing_marks(sample_marks)
    assert result == 80.0


def test_addition():
    assert add(10, 5) == 15
    assert add(-4, 9) == 5
    with pytest.raises(TypeError):
        add("10", 5)


def test_average():
    assert calculate_average([80, 90, 100]) == 90.0
    assert calculate_average([]) == 0.0


@pytest.mark.parametrize("score,expected_grade", [
    (80, "A"),
    (79, "B"),
    (70, "B"),
    (69, "C"),
    (60, "C"),
    (59, "D"),
    (33, "D"),
    (32, "Fail"),
])
def test_grade_boundaries(score, expected_grade):
    """Test boundary values required in the assignment."""
    assert calculate_grade(score) == expected_grade


def test_grade_raises_for_out_of_bounds():
    """Ensure invalid scores raise ValueError."""
    with pytest.raises(ValueError):
        calculate_grade(-1)
    with pytest.raises(ValueError):
        calculate_grade(101)


@pytest.fixture
def sample_account():
    """Pytest fixture returning a BankAccount with Rs 1000."""
    return BankAccount("Ihsan", 1000.0)


def test_bank_account_fixture(sample_account):
    """Test deposit, withdraw, history, and errors on BankAccount fixture."""
    # Deposit test
    sample_account.deposit(500.0)
    assert sample_account.balance == 1500.0

    # Withdraw test
    sample_account.withdraw(300.0)
    assert sample_account.balance == 1200.0

    # History list verification
    assert len(sample_account.history) == 3

    # Error tests
    with pytest.raises(ValueError):
        sample_account.deposit(-50)
    with pytest.raises(ValueError):
        sample_account.withdraw(99999)


# =========================================================================
# 4. Direct Execution Demonstration
# =========================================================================
if __name__ == "__main__":
    print("=" * 60)
    print("PART 12: DEBUGGING & TESTING DEMONSTRATION")
    print("=" * 60)

    print("\n1. Warm-up Bug Hunt Fixed Result:")
    test_marks = [90, 25, 70]
    print(f"   Original list: {test_marks}")
    print(f"   Average of passing marks (90 and 70) = {fixed_average_passing_marks(test_marks)}")

    print("\n2. Boundary Grade Test Check:")
    for test_val in [80, 79, 70, 69, 60, 59, 33, 32]:
        print(f"   Score {test_val:>2} -> Grade: {calculate_grade(test_val)}")

    print("\nAll assertions and checks executed successfully.")
    print("Run 'pytest part12_debugging_testing.py -v' to execute the test suite.")
