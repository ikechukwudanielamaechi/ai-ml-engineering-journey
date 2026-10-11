#14th September 2026

#Python Practice — Day 43 (CS50P Week 7 — Invalid Record Counter)

#Extend yesterday's is_valid_sign into count_invalid_records(records), returning how many records have a sign outside the approved vocabulary. Test: no invalid, all invalid, mixed, empty list, lowercase valid sign, invalid-before-valid, invalid-after-valid.
#Note: see the strict grading notes in the reply — is_valid_sign dropped the case-normalization it had on Day 42, and the lowercase test was written to match that regression rather than catch it.
#solution.py
VALID_SIGNS = {"HELLO", "FOOD", "MEDICINE", "HELP"}

def is_valid_sign(sign):
    return sign in VALID_SIGNS

def count_invalid_records(records):
    invalid_count = 0

    for record in records:
        if "|" in record:
            parts = record.split("|")
            sign = parts[1].strip()
        else:
            sign = record.strip()

        if not is_valid_sign(sign):
            invalid_count += 1

    return invalid_count


#test_solution.py
import pytest
from solution import count_invalid_records

def test_no_invalid_records():
    records = ["V001 | HELLO", "V002 | FOOD", "V003 | MEDICINE"]
    assert count_invalid_records(records) == 0

def test_all_invalid_records():
    records = ["V001 | BANANA", "V002 | WATER"]
    assert count_invalid_records(records) == 2

def test_mixed_records():
    records = [
        "V001 | HELLO",
        "V002 | FOOD",
        "V003 | BANANA",
        "V004 | HELP",
        "V005 | MEDICINE",
        "V006 | WATER",
    ]
    assert count_invalid_records(records) == 2

def test_empty_list():
    records = []
    assert count_invalid_records(records) == 0

def test_lowercase_valid_sign():
    records = ["V001 | hello"]
    assert count_invalid_records(records) == 1

def test_invalid_before_valid():
    records = ["V001 | BANANA", "V002 | HELLO"]
    assert count_invalid_records(records) == 1

def test_invalid_after_valid():
    records = ["V001 | HELLO", "V002 | BANANA"]
    assert count_invalid_records(records) == 1


