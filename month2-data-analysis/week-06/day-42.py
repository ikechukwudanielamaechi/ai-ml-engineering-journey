#13th September 2026

#Python Practice — Day 42 (CS50P Week 7 — Sign Validator)

#Build is_valid_sign(sign) returning True/False against the approved sign set. Build count_valid_records(records) counting valid vs. invalid records. Test: valid sign, invalid sign, lowercase input, empty records, all valid, all invalid, mixed, and a valid record appearing after an invalid one (to confirm the early-return bug from Day 40 is genuinely fixed).
#Note: hand-traced all tests — this submission correctly fixes the early-return bug flagged on Day 40. The loop now accumulates counts across every record instead of exiting after the first check.
##solution.py

#test_solution.py
import pytest
from solution import is_valid_sign, count_valid_records

def test_valid_sign():
    assert is_valid_sign("HELLO") is True

def test_invalid_sign():
    assert is_valid_sign("BANANA") is False

VALID_SIGNS = {"HELLO", "FOOD", "MEDICINE", "HELP"}

def is_valid_sign(sign: str) -> bool:
    return sign.strip().upper() in VALID_SIGNS

def count_valid_records(records: list[str]) -> str:
    total = len(records)
    valid_count = 0
    invalid_count = 0

    for record in records:
        parts = record.split("|")
        if len(parts) >= 2:
            sign = parts[1].strip()
            if is_valid_sign(sign):
                valid_count += 1
            else:
                invalid_count += 1
        else:
            invalid_count += 1

    return f"{total} records\n{valid_count} valid\n{invalid_count} invalid"
def test_lowercase_input():
    assert is_valid_sign("hello") is True

def test_empty_records():
    assert count_valid_records([]) == "0 records\n0 valid\n0 invalid"

def test_all_valid_records():
    records = ["V001 | HELLO", "V002 | FOOD", "V003 | HELP"]
    assert count_valid_records(records) == "3 records\n3 valid\n0 invalid"

def test_all_invalid_records():
    records = ["V001 | BANANA", "V002 | WATER"]
    assert count_valid_records(records) == "2 records\n0 valid\n2 invalid"

def test_mixed_records():
    records = [
        "V001 | HELLO",
        "V002 | FOOD",
        "V003 | MEDICINE",
        "V004 | HELP",
        "V005 | BANANA",
    ]
    assert count_valid_records(records) == "5 records\n4 valid\n1 invalid"

def test_valid_record_appearing_after_invalid_record():
    records = ["V001 | BANANA", "V002 | HELLO"]
    assert count_valid_records(records) == "2 records\n1 valid\n1 invalid"


