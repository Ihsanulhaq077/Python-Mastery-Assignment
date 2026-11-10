# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
FINAL PROJECT: SCHOOL MANAGER APPLICATION
Entry point for the menu-driven School Manager CLI.
Demonstrates:
- Clean modular package architecture (school/ models, manager, storage, utils)
- Loops and menu flow control
- Object-oriented design and Dataclasses
- Comprehensive input validation and defensive programming
- JSON file persistence
- Automated report cards and ranking
- AI Teacher Comment streaming (Bonus Feature)
"""

import sys
import time
from pathlib import Path

from school.manager import SchoolManager
from school.models import Student
from school.utils import (
    format_report_card,
    generate_teacher_comment_stream,
    prompt_float,
    prompt_int,
    prompt_string,
)


def print_header(title: str) -> None:
    """Print a styled section header."""
    print("\n" + "=" * 54)
    print(f"       {title.upper()}")
    print("=" * 54)


def handle_add_student(manager: SchoolManager) -> None:
    """Collects student information and registers them in the system."""
    print_header("Add New Student")

    student_id = prompt_int("Enter Student ID (e.g., 101)", min_val=1, max_val=999999)
    if manager.get_student(student_id):
        print(f"Error: A student with ID {student_id} already exists!")
        return

    name = prompt_string("Enter Student Full Name")
    age = prompt_int("Enter Student Age", min_val=5, max_val=100)
    class_name = prompt_string("Enter Class / Section (e.g., AI-1st Year)", default="AI-1st Year")

    print("\nEnter Marks for Subjects (enter blank subject name when done):")
    marks: dict[str, float] = {}

    # Prompt for subject entries
    standard_subjects = ["Programming", "Mathematics", "English"]
    for sub in standard_subjects:
        score = prompt_float(f"Enter score for '{sub}' (0 - 100)", min_val=0.0, max_val=100.0, default=75.0)
        marks[sub] = score

    # Additional custom subjects
    while True:
        try:
            extra_sub = input("Add extra subject name (or press Enter to finish): ").strip()
            if not extra_sub:
                break
            extra_score = prompt_float(f"Enter score for '{extra_sub}' (0 - 100)", min_val=0.0, max_val=100.0)
            marks[extra_sub] = extra_score
        except EOFError:
            break

    try:
        new_student = Student(
            student_id=student_id,
            name=name,
            age=age,
            class_name=class_name,
            marks=marks,
        )
        if manager.add_student(new_student):
            print(f"\nSuccess: Student '{name}' (ID: {student_id}) enrolled successfully!")
        else:
            print(f"\nError: Could not enroll student with ID {student_id}.")
    except (ValueError, TypeError) as err:
        print(f"\nEnrollment Error: {err}")


def handle_view_students(manager: SchoolManager) -> None:
    """Display tabular view of all enrolled students."""
    print_header("Enrolled Students Directory")
    students = manager.list_students()

    if not students:
        print("No student records found in memory. (Try loading data from option 9)")
        return

    print(f"{'ID':<6}{'Name':<20}{'Age':<6}{'Class':<14}{'Average':<10}{'Grade':<8}{'Status'}")
    print("-" * 72)
    for s in students:
        status = "PASSED" if s.is_passed else "FAILED"
        print(f"{s.student_id:<6}{s.name:<20}{s.age:<6}{s.class_name:<14}{s.average:<10.2f}{s.grade:<8}{status}")
    print("-" * 72)
    print(f"Total Enrolled Students: {len(students)}")


def handle_search_student(manager: SchoolManager) -> None:
    """Search for students by ID or name substring."""
    print_header("Search Student Records")
    query = prompt_string("Enter Student ID or Name to search")
    results = manager.search_students(query)

    if not results:
        print(f"No student matching '{query}' was found.")
        return

    print(f"\nFound {len(results)} matching student(s):")
    for s in results:
        print(f"  * ID: {s.student_id} | Name: {s.name} | Class: {s.class_name} | Avg: {s.average:.2f} ({s.grade})")


def handle_update_student(manager: SchoolManager) -> None:
    """Update details or marks of an existing student."""
    print_header("Update Student Information")
    student_id = prompt_int("Enter Student ID to update")
    student = manager.get_student(student_id)

    if not student:
        print(f"Student with ID {student_id} not found.")
        return

    print(f"\nCurrent Profile: {student.name}, Age {student.age}, Class: {student.class_name}")
    print("Leave field blank to keep existing value.\n")

    try:
        new_name_input = input(f"New Name [{student.name}]: ").strip()
        new_name = new_name_input if new_name_input else None

        new_age_input = input(f"New Age [{student.age}]: ").strip()
        new_age = int(new_age_input) if new_age_input else None

        new_class_input = input(f"New Class [{student.class_name}]: ").strip()
        new_class = new_class_input if new_class_input else None

        manager.update_student(
            student_id=student_id,
            name=new_name,
            age=new_age,
            class_name=new_class,
        )
        print(f"\nStudent ID {student_id} successfully updated!")
    except (ValueError, EOFError) as err:
        print(f"Update failed: {err}")


def handle_delete_student(manager: SchoolManager) -> None:
    """Safely remove a student with confirmation."""
    print_header("Delete Student Record")
    student_id = prompt_int("Enter Student ID to delete")
    student = manager.get_student(student_id)

    if not student:
        print(f"Student with ID {student_id} does not exist.")
        return

    try:
        confirm = input(f"Are you sure you want to permanently delete '{student.name}'? (y/n): ").strip().lower()
        if confirm == "y":
            manager.delete_student(student_id)
            print(f"Student ID {student_id} has been removed.")
        else:
            print("Deletion cancelled.")
    except EOFError:
        print("Cancelled.")


def handle_report_card(manager: SchoolManager) -> None:
    """Generate and display official ASCII report card."""
    print_header("Generate Official Report Card")
    student_id = prompt_int("Enter Student ID")
    student = manager.get_student(student_id)

    if not student:
        print(f"Student ID {student_id} not found.")
        return

    card = format_report_card(student)
    print("\n" + card)


def handle_class_ranking(manager: SchoolManager) -> None:
    """Display student ranking sorted descending by average marks."""
    print_header("Class Merit Ranking")
    rankings = manager.get_class_ranking()

    if not rankings:
        print("No student records available for ranking.")
        return

    print(f"{'Rank':<6}{'Student ID':<12}{'Name':<22}{'Average':<12}{'Grade'}")
    print("-" * 62)
    for rank, s in rankings:
        print(f"{rank:<6}{s.student_id:<12}{s.name:<22}{s.average:<12.2f}{s.grade}")
    print("-" * 62)


def handle_save_data(manager: SchoolManager) -> None:
    """Save records to JSON file."""
    print_header("Save Records to Storage")
    if manager.save_to_disk():
        print(f"Successfully saved {manager.student_count} student record(s) to '{manager.storage_path}'.")
    else:
        print("Error: Could not save records to disk.")


def handle_load_data(manager: SchoolManager) -> None:
    """Load records from JSON file."""
    print_header("Load Records from Storage")
    count = manager.load_from_disk()
    print(f"Successfully loaded {count} student record(s) from '{manager.storage_path}'.")


def handle_ai_comment(manager: SchoolManager) -> None:
    """Bonus Feature: Generates and streams faculty commentary."""
    print_header("AI Faculty Advisory Comment (Bonus)")
    student_id = prompt_int("Enter Student ID")
    student = manager.get_student(student_id)

    if not student:
        print(f"Student ID {student_id} not found.")
        return

    print(f"\nGenerating streaming academic review for '{student.name}' (Average: {student.average:.2f}%)...")
    print("\nAdvisory Feedback: ", end="", flush=True)

    # Demonstrate streaming generator with simulated token flow
    stream = generate_teacher_comment_stream(student)
    for word_chunk in stream:
        print(word_chunk, end="", flush=True)
        time.sleep(0.04)  # Smooth real-time token stream effect
    print("\n")


def display_menu() -> None:
    """Displays the main interactive application menu."""
    print("\n" + "=" * 32)
    print("        SCHOOL MANAGER         ")
    print("=" * 32)
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Generate Report Card")
    print("7. Show Class Ranking")
    print("8. Save Data")
    print("9. Load Data")
    print("10. AI Teacher Comment (Bonus)")
    print("0. Exit")
    print("=" * 32)


def main() -> None:
    """Main CLI entry point."""
    storage_file = Path("school.json") if Path("school.json").exists() else Path("data/students.json")
    manager = SchoolManager(storage_path=storage_file)

    # Automatically attempt to load existing records if present
    if storage_file.exists():
        manager.load_from_disk()

    while True:
        display_menu()
        try:
            choice = input("Enter your choice (0-10): ").strip()
        except EOFError:
            print("\n(EOF detected: exiting application)")
            break

        if choice == "1":
            handle_add_student(manager)
        elif choice == "2":
            handle_view_students(manager)
        elif choice == "3":
            handle_search_student(manager)
        elif choice == "4":
            handle_update_student(manager)
        elif choice == "5":
            handle_delete_student(manager)
        elif choice == "6":
            handle_report_card(manager)
        elif choice == "7":
            handle_class_ranking(manager)
        elif choice == "8":
            handle_save_data(manager)
        elif choice == "9":
            handle_load_data(manager)
        elif choice == "10":
            handle_ai_comment(manager)
        elif choice == "0":
            print("\nExiting School Manager. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid selection! Please enter a number between 0 and 10.")


if __name__ == "__main__":
    main()

