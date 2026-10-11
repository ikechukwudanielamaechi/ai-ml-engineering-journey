#18th September 2026


#Python Practice — Day 47 (CS50P Week 8 — CSV Loader & Counters)

#Load project_bridge.csv using Python's csv module. Count total records, count per sign, count per signer, find records by sign, find records by signer. Test: multiple records, sign appearing multiple times, signer appearing multiple times, nonexistent sign, nonexistent signer, empty CSV, mixed signs, mixed signers.
#Critical bug found — see grading notes in the reply. count_signers() has mismatched indentation between its two lines, which is a real IndentationError in Python. This would prevent the entire module from being imported, meaning none of the tests could even run — not just the ones touching count_signers.
#dataset_processor.py
import csv
from collections import Counter

def load_records(file_path):
    records = []
    with open(file_path, mode="r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        for row in reader:
            records.append(row)
    return records

def count_records(records):
    return len(records)

def count_signs(records):
    counts = Counter(record["sign"] for record in records)
    return dict(counts)

def count_signers(records):
    counts = Counter(record["signer"] for record in records)
    return dict(counts)




def find_records_by_sign(records, sign):
    return [r for r in records if r["sign"] == sign]

def find_records_by_signer(records, signer):
      return [r for r in records if r["signer"] == signer]

def main():
    records = load_records("project_bridge.csv")
    print(f"Total records: {count_records(records)}")
    print("\nCounts per sign:")
    for sign, count in count_signs(records).items():
        print(f"{sign}: {count}")
    print("\nCounts per signer:")
    for signer, count in count_signers(records).items():
        print(f"{signer}: {count}")

if __name__ == "__main__":
    main()


test_dataset_processor.py
import pytest
from dataset_processor import (
    count_records,
    count_signs,
    count_signers,
    find_records_by_sign,
    find_records_by_signer,
)

@pytest.fixture
def sample_records():
    return [
        {"video_id": "V001", "signer": "S01", "sign": "HELLO", "environment": "Indoor"},
        {"video_id": "V002", "signer": "S01", "sign": "FOOD", "environment": "Indoor"},
        {"video_id": "V003", "signer": "S02", "sign": "FOOD", "environment": "Outdoor"},
        {"video_id": "V004", "signer": "S03", "sign": "MEDICINE", "environment": "Indoor"},
        {"video_id": "V005", "signer": "S01", "sign": "HELP", "environment": "Outdoor"},
        {"video_id": "V006", "signer": "S02", "sign": "HELP", "environment": "Indoor"},
        {"video_id": "V007", "signer": "S03", "sign": "FOOD", "environment": "Outdoor"},
        {"video_id": "V008", "signer": "S04", "sign": "HELLO", "environment": "Indoor"},
    ]

def test_multiple_records(sample_records):
    assert count_records(sample_records) == 8

def test_sign_appearing_multiple_times(sample_records):
    results = find_records_by_sign(sample_records, "FOOD")
    assert len(results) == 3

def test_signer_appearing_multiple_times(sample_records):
    results = find_records_by_signer(sample_records, "S01")
    assert len(results) == 3

def test_nonexistent_sign(sample_records):
    assert find_records_by_sign(sample_records, "DANCE") == []

def test_nonexistent_signer(sample_records):
    assert find_records_by_signer(sample_records, "S99") == []

def test_empty_csv():
    empty_data = []
    assert count_records(empty_data) == 0
    assert count_signs(empty_data) == {}
    assert count_signers(empty_data) == {}
    assert find_records_by_sign(empty_data, "HELLO") == []
    assert find_records_by_signer(empty_data, "S01") == []

def test_mixed_signs(sample_records):
    counts = count_signs(sample_records)
    assert counts == {"HELLO": 2, "FOOD": 3, "MEDICINE": 1, "HELP": 2}

def test_mixed_signers(sample_records):
    counts = count_signers(sample_records)
    assert counts == {"S01": 3, "S02": 2, "S03": 2, "S04": 1}


