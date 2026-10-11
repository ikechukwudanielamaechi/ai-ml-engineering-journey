#15th September 2026

#Python Practice — Day 44 (CS50P Week 7 — Valid/Invalid Sign Counters)

#Build count_valid_signs(records) and count_invalid_signs(records) against an approved vocabulary. Design decision required: should "hello" (lowercase) count as valid or invalid? Decide deliberately and explain the reasoning — don't just copy a previous day's approach.
#Note: see the strict grading notes in the reply — logic is correct (hand-verified against all 8 tests), but the design-decision explanation wasn't included, and the test file is missing its import of the two functions being tested.
#solution.py
VALID_SIGNS = {"HELLO", "FOOD", "MEDICINE", "HELP"}

def is_valid_sign(sign: str) -> bool:
    return sign.strip() in VALID_SIGNS

def count_valid_signs(records: list[str]) -> int:
    valid_count = 0
    for record in records:
        parts = record.split("|")
        if len(parts) >= 2:
            sign = parts[1].strip()
            if is_valid_sign(sign):
                valid_count += 1
    return valid_count

def count_invalid_signs(records: list[str]) -> int:
    invalid_count = 0
    for record in records:
        parts = record.split("|")
        if len(parts) >= 2:
            sign = parts[1].strip()
            if not is_valid_sign(sign):
                invalid_count += 1
        else:
            invalid_count += 1
    return invalid_count


##test_solution.py
import pytest
# NOTE: missing "from solution import count_valid_signs, count_invalid_signs"

def test_all_valid():
    records = ["V001 | HELLO", "V002 | FOOD", "V004 | HELP"]
    assert count_valid_signs(records) == 3
    assert count_invalid_signs(records) == 0

def test_all_invalid():
    records = ["V003 | BANANA", "V006 | WATER"]
    assert count_valid_signs(records) == 0
    assert count_invalid_signs(records) == 2

def test_mixed():
    records = [
        "V001 | HELLO",
        "V002 | FOOD",
        "V003 | BANANA",
        "V004 | HELP",
        "V005 | MEDICINE",
        "V006 | WATER",
        "V007 | FOOD",
        "V008 | HELLO"
    ]
    assert count_valid_signs(records) == 6
    assert count_invalid_signs(records) == 2

def test_empty_list():
    assert count_valid_signs([]) == 0
    assert count_invalid_signs([]) == 0

def test_invalid_first():
    records = ["V003 | BANANA", "V001 | HELLO", "V002 | FOOD"]
    assert count_valid_signs(records) == 2
    assert count_invalid_signs(records) == 1

def test_invalid_last():
    records = ["V001 | HELLO", "V002 | FOOD", "V003 | BANANA"]
    assert count_valid_signs(records) == 2
    assert count_invalid_signs(records) == 1

def test_lowercase_sign():
    records = ["V001 | hello"]
    assert count_valid_signs(records) == 0
    assert count_invalid_signs(records) == 1

def test_valid_after_invalid():
    records = ["V003 | BANANA", "V001 | HELLO"]
    assert count_valid_signs(records) == 1
    assert count_invalid_signs(records) == 1


