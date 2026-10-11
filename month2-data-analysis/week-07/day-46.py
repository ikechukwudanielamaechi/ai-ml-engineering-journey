#17th September 2026


#Python Practice — Day 46 (CS50P Week 8 — Find & Count by Sign/Signer)

#Extend DatasetRecord with find_by_sign, find_by_signer, count_by_sign, and count_by_signer, operating over a list of at least 6 records. Test: sign exists, sign doesn't exist, signer exists, signer doesn't exist, one sign appearing multiple times, one signer appearing multiple times, empty dataset, mixed dataset.
#Note: hand-traced all 8 tests against the fixture data — every one checks out. Fourth consecutive day of fully correct Python logic.
#dataset.py
class DatasetRecord:
    def __init__(self, video_id, signer, sign, environment):
        self.video_id = video_id
        self.signer = signer
        self.sign = sign
        self.environment = environment

def find_by_sign(records, target_sign):
    results = []
    for record in records:
        if record.sign == target_sign:
            results.append(record)
    return results

def find_by_signer(records, target_signer):
    results = []
    for record in records:
        if record.signer == target_signer:
            results.append(record)
    return results

def count_by_sign(records):
    counts = {}
    for record in records:
        if record.sign in counts:
            counts[record.sign] += 1
        else:
            counts[record.sign] = 1
    return counts

def count_by_signer(records):
    counts = {}
    for record in records:
        if record.signer in counts:
            counts[record.signer] += 1
        else:
            counts[record.signer] = 1
    return counts


#test_dataset.py
import pytest
from dataset import (
    DatasetRecord,
    find_by_sign,
    find_by_signer,
    count_by_sign,
    count_by_signer,
)

@pytest.fixture
def mixed_dataset():
    return [
        DatasetRecord("V001", "S01", "HELLO", "Studio"),
        DatasetRecord("V002", "S02", "FOOD", "Outdoor"),
        DatasetRecord("V003", "S01", "MEDICINE", "Studio"),
        DatasetRecord("V004", "S03", "HELP", "Outdoor"),
        DatasetRecord("V005", "S01", "HELLO", "Indoor"),
        DatasetRecord("V006", "S04", "FOOD", "Studio"),
    ]

def test_sign_exists(mixed_dataset):
    results = find_by_sign(mixed_dataset, "MEDICINE")
    assert len(results) == 1
    assert results[0].video_id == "V003"

def test_sign_does_not_exist(mixed_dataset):
    results = find_by_sign(mixed_dataset, "WATER")
    assert len(results) == 0

def test_signer_exists(mixed_dataset):
    results = find_by_signer(mixed_dataset, "S02")
    assert len(results) == 1
    assert results[0].signer == "S02"

def test_signer_does_not_exist(mixed_dataset):
    results = find_by_signer(mixed_dataset, "S99")
    assert len(results) == 0

def test_one_sign_appearing_multiple_times(mixed_dataset):
    results = find_by_sign(mixed_dataset, "HELLO")
    assert len(results) == 2

def test_one_signer_appearing_multiple_times(mixed_dataset):
    results = find_by_signer(mixed_dataset, "S01")
    assert len(results) == 3

def test_empty_dataset():
    empty_records = []
    assert find_by_sign(empty_records, "HELLO") == []
    assert find_by_signer(empty_records, "S01") == []
    assert count_by_sign(empty_records) == {}
    assert count_by_signer(empty_records) == {}

def test_mixed_dataset(mixed_dataset):
    expected_sign_counts = {
        "HELLO": 2,
        "FOOD": 2,
        "MEDICINE": 1,
        "HELP": 1,
    }
    assert count_by_sign(mixed_dataset) == expected_sign_counts

    expected_signer_counts = {
        "S01": 3,
        "S02": 1,
        "S03": 1,
        "S04": 1,
    }
    assert count_by_signer(mixed_dataset) == expected_signer_counts


