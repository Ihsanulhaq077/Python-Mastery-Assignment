# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
PART 9: OBJECT-ORIENTED PROGRAMMING (OOP)
This script demonstrates:
- Classes and Objects
- __init__ constructor, instance & class attributes
- Encapsulation: getters, setters, and validation
- Inheritance: Subclasses extending base classes
- Method Overriding and Polymorphism
- Warm-up: Student Class with __str__
- Build: BankAccount with Transaction History & Validation
- Challenge: Library & EBook Inheritance System
"""

print("=" * 60)
print("PART 9: OBJECT-ORIENTED PROGRAMMING")
print("=" * 60)

# =========================================================================
# 1. WARM-UP — Student Class
# =========================================================================
print("\n" + "=" * 40)
print("1. WARM-UP: STUDENT CLASS")
print("=" * 40)


class SimpleStudent:
    """Represents a student with a marks list and string representation."""

    def __init__(self, name: str, roll_number: int) -> None:
        self.name = name
        self.roll_number = roll_number
        self.marks: list[float] = []

    def add_mark(self, score: float) -> None:
        """Append a valid mark."""
        if 0 <= score <= 100:
            self.marks.append(score)
        else:
            raise ValueError("Mark must be between 0 and 100.")

    def average(self) -> float:
        """Compute average marks."""
        return sum(self.marks) / len(self.marks) if self.marks else 0.0

    def __str__(self) -> str:
        return f"{self.name} (Roll {self.roll_number}): avg {self.average():.1f}"


s1 = SimpleStudent("Ali", 12)
s1.add_mark(80.0)
s1.add_mark(82.0)
print(f"Student Object: {s1}")

# =========================================================================
# 2. BUILD — Bank Account with Encapsulation & History
# =========================================================================
print("\n" + "=" * 40)
print("2. BUILD: BANK ACCOUNT (Encapsulation)")
print("=" * 40)


class BankAccount:
    """Represents a bank account with deposit, withdraw, and transaction history."""

    def __init__(self, owner: str, initial_balance: float = 0.0) -> None:
        self.owner = owner
        self.__balance = initial_balance
        self.history: list[str] = [f"Account opened with Rs {initial_balance:,.2f}"]

    @property
    def balance(self) -> float:
        return self.__balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Deposit amount must be positive.")
        self.__balance += amount
        self.history.append(f"Deposited: Rs {amount:,.2f} | Balance: Rs {self.__balance:,.2f}")

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive.")
        if amount > self.__balance:
            raise ValueError("Insufficient funds!")
        self.__balance -= amount
        self.history.append(f"Withdrew: Rs {amount:,.2f} | Balance: Rs {self.__balance:,.2f}")


account = BankAccount("Ihsan Ul Haq", 1000.0)
account.deposit(500.0)
account.withdraw(200.0)
print(f"Current Balance for {account.owner}: Rs {account.balance:,.2f}")
print("Transaction History:")
for entry in account.history:
    print(f"  * {entry}")

# =========================================================================
# 3. CHALLENGE — Library & EBook Inheritance System (Polymorphism)
# =========================================================================
print("\n" + "=" * 40)
print("3. CHALLENGE: LIBRARY & EBOOK INHERITANCE")
print("=" * 40)


class Book:
    """Represents a physical library book."""

    def __init__(self, title: str, author: str) -> None:
        self.title = title
        self.author = author
        self.available = True

    def __str__(self) -> str:
        status = "Available" if self.available else "Borrowed"
        return f"'{self.title}' by {self.author} [{status}]"


class EBook(Book):
    """Subclass representing a digital book with file size."""

    def __init__(self, title: str, author: str, file_size_mb: float) -> None:
        super().__init__(title, author)
        self.file_size_mb = file_size_mb

    def __str__(self) -> str:
        # Method overriding
        return f"[E-Book] '{self.title}' by {self.author} ({self.file_size_mb} MB) [Instant Access]"


class Library:
    """Manages collection of physical books and ebooks (Composition)."""

    def __init__(self) -> None:
        self.books: list[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)

    def borrow(self, title: str) -> bool:
        for b in self.books:
            if b.title.lower() == title.lower() and b.available:
                b.available = False
                return True
        return False

    def available_books(self) -> list[Book]:
        return [b for b in self.books if b.available]


library = Library()
library.add_book(Book("Clean Code", "Robert C. Martin"))
library.add_book(EBook("Fluent Python", "Luciano Ramalho", 8.5))

print("All Library Books (Polymorphism Demo):")
for b in library.books:
    print(f"  {b}")
