# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
Persistence layer for School Manager.
Safely saves and loads student records to and from JSON files with error handling.
"""

import json
import logging
from pathlib import Path
from typing import Union

from school.models import Student

logger = logging.getLogger(__name__)


def save_students(students: list[Student], filepath: Union[str, Path] = "data/students.json") -> bool:
    """Save a list of Student objects to a JSON file.

    Creates parent directories if they do not exist.
    Returns True upon success, False upon failure.
    """
    path = Path(filepath)
    try:
        # Ensure target directory exists
        path.parent.mkdir(parents=True, exist_ok=True)

        # Convert student models to list of dictionaries
        serializable_data = [student.to_dict() for student in students]

        with open(path, "w", encoding="utf-8") as file:
            json.dump(serializable_data, file, indent=4)
        return True

    except (OSError, TypeError) as err:
        logger.error(f"Failed to save student data to '{path}': {err}")
        return False


def load_students(filepath: Union[str, Path] = "data/students.json") -> list[Student]:
    """Load Student objects from a JSON file.

    Handles:
    - Missing files (returns empty list)
    - Corrupted or invalid JSON (returns empty list)
    - Empty files (returns empty list)
    - Invalid student entries (skips corrupted records safely)
    """
    path = Path(filepath)

    if not path.exists():
        logger.warning(f"Storage file '{path}' does not exist. Returning empty list.")
        return []

    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read().strip()
            if not content:
                logger.warning(f"Storage file '{path}' is empty.")
                return []
            raw_data = json.loads(content)

        if not isinstance(raw_data, list):
            logger.error(f"Expected a list of students in '{path}', got {type(raw_data).__name__}.")
            return []

        loaded_students: list[Student] = []
        for index, item in enumerate(raw_data):
            try:
                if isinstance(item, dict):
                    student = Student.from_dict(item)
                    loaded_students.append(student)
                else:
                    logger.warning(f"Skipping record #{index}: entry is not a dictionary.")
            except (ValueError, TypeError, KeyError) as err:
                logger.warning(f"Skipping corrupted student record #{index}: {err}")

        return loaded_students

    except json.JSONDecodeError as err:
        logger.error(f"JSON decode error in '{path}': {err}. Returning empty list.")
        return []
    except OSError as err:
        logger.error(f"OS error reading file '{path}': {err}.")
        return []

