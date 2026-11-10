# Name: Ihsan Ul Haq
# Roll No: TRN-2026-000951
# Date: 10-11-2026

"""
PART 3: LOOPS (for / while)
This script demonstrates:
- for loops and range()
- while loops
- Flow controls: break and continue
- Warm-up: Times Table & Counting
- Build: ATM PIN Authentication (3 attempts)
- Challenge: Number Guessing Game (Too high / Too low)
- Extra: Triangle of stars and Sum 1 to N
"""

import random

print("=" * 60)
print("PART 3: LOOPS AND FLOW CONTROL")
print("=" * 60)


def safe_input(prompt: str, default: str) -> str:
    """Helper to safely read user input with a fallback default."""
    try:
        user_val = input(f"{prompt} [Default: {default}]: ").strip()
        return user_val if user_val else default
    except EOFError:
        return default


# =========================================================================
# 1. WARM-UP — Times Table & Number Counting
# =========================================================================
print("\n" + "=" * 40)
print("1. WARM-UP: TIMES TABLE (for loop)")
print("=" * 40)

table_str = safe_input("Enter table number", "7")
table_num = int(table_str)

for i in range(1, 11):
    print(f"  {table_num} x {i:>2} = {table_num * i:>3}")

# Sum of numbers from 1 to 100
total_sum = sum(range(1, 101))
print(f"\nSum of numbers from 1 to 100 = {total_sum}")

# Nested loop: Triangle of stars
print("\nTriangle of Stars:")
for row in range(1, 6):
    print("  " + "* " * row)

# =========================================================================
# 2. BUILD — ATM PIN Check (while loop with break/continue)
# =========================================================================
print("\n" + "=" * 40)
print("2. BUILD: ATM PIN VERIFICATION (while loop)")
print("=" * 40)

CORRECT_PIN = "4321"
attempts_left = 3
authenticated = False

# Automated demonstration showing attempt tracking
test_inputs = ["1111", "2222", "4321"]
print(f"Correct PIN is configured as: {CORRECT_PIN}")
print(f"Simulating user entries: {test_inputs}")

while attempts_left > 0:
    # Use simulated input for headless test or interactive prompt
    simulated_pin = test_inputs[3 - attempts_left]
    print(f"\nAttempt entered: '{simulated_pin}'")

    if simulated_pin == CORRECT_PIN:
        print("Welcome! PIN accepted.")
        authenticated = True
        break  # Terminate loop on success
    else:
        attempts_left -= 1
        if attempts_left > 0:
            print(f"Wrong PIN! Tries left: {attempts_left}")
        else:
            print("Card blocked! 3 incorrect attempts recorded.")

# =========================================================================
# 3. CHALLENGE — Number Guessing Game (Simulation Mode)
# =========================================================================
print("\n" + "=" * 40)
print("3. CHALLENGE: NUMBER GUESSING GAME")
print("=" * 40)

# Demonstrates random secret target with feedback loop
secret_number = random.randint(1, 50)
print(f"(Random target chosen between 1 and 50)")

simulated_guesses = [25, 37, secret_number]
guess_count = 0

for guess in simulated_guesses:
    guess_count += 1
    print(f"Guessed: {guess}")
    if guess < secret_number:
        print("  -> Too low!")
    elif guess > secret_number:
        print("  -> Too high!")
    else:
        print(f"  -> Got it in {guess_count} guesses! Secret was {secret_number}.")
        break
