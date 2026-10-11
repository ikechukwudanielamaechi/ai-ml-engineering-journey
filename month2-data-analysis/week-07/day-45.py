#16th September 2026


#Python Practice — Day 45 (CS50P Week 8 — DatasetRecord Class)

#Build a DatasetRecord class (video_id, signer, sign, environment) with methods to check sign validity, environment validity, missing signer, and an overall validate() result. Process a list of records and report valid/invalid counts. Test 8 cases: fully valid, invalid sign, invalid environment, missing signer, empty dataset, multiple valid, multiple invalid, mixed.
#Note: hand-traced all 8 tests — everything checks out correctly. Third consecutive day with fully correct Python logic.
#dataset.py
ALLOWED_SIGNS = {"HELLO", "FOOD", "MEDICINE", "HELP"}
ALLOWED_ENVIRONMENTS = {"Indoor", "Outdoor"}

class DatasetRecord:
    def __init__(self, video_id, signer, sign, environment):
        self.video_id = video_id
        self.signer = signer
        self.sign = sign
        self.environment = environment

    def is_valid_sign(self):
        return self.sign in ALLOWED_SIGNS

    def is_valid_environment(self):
        return self.environment in ALLOWED_ENVIRONMENTS

    def has_missing_signer(self):
        if self.signer is None:
            return True
        if isinstance(self.signer, str) and self.signer.strip() == "":
            return True
        return False

    def validate(self):
        if self.has_missing_signer():
            return (False, f"{self.video_id} -> invalid: missing signer")
        if not self.is_valid_sign():
            return (False, f"{self.video_id} -> invalid: unknown sign")
        if not self.is_valid_environment():
            return (False, f"{self.video_id} -> invalid: unknown environment")

        return (True, f"{self.video_id} -> valid")

def process_dataset(records):
    valid_count = 0
    invalid_count = 0
    results = []

    for record in records:
        is_valid, msg = record.validate()
        results.append(msg)
        if is_valid:
            valid_count += 1
        else:
            invalid_count += 1

    return {"valid": valid_count, "invalid": invalid_count, "results": results}


#test_dataset.py
import pytest
from dataset import DatasetRecord, process_dataset

def test_completely_valid_record():
    rec = DatasetRecord("V001", "Signer1", "HELLO", "Indoor")
    is_valid, msg = rec.validate()
    assert is_valid is True
    assert msg == "V001 -> valid"

def test_invalid_sign():
    rec = DatasetRecord("V002", "Signer1", "BANANA", "Indoor")
    is_valid, msg = rec.validate()
    assert is_valid is False
    assert msg == "V002 -> invalid: unknown sign"

def test_invalid_environment():
    rec = DatasetRecord("V003", "Signer1", "FOOD", "Space")
    is_valid, msg = rec.validate()
    assert is_valid is False
    assert msg == "V003 -> invalid: unknown environment"

def test_missing_signer():
    rec = DatasetRecord("V004", "", "HELP", "Outdoor")
    is_valid, msg = rec.validate()
    assert is_valid is False
    assert msg == "V004 -> invalid: missing signer"

def test_empty_dataset():
    summary = process_dataset([])
    assert summary["valid"] == 0
    assert summary["invalid"] == 0

def test_multiple_valid_records():
    records = [
        DatasetRecord("V001", "Signer1", "HELLO", "Indoor"),
        DatasetRecord("V002", "Signer2", "HELP", "Outdoor"),
    ]
    summary = process_dataset(records)
    assert summary["valid"] == 2
    assert summary["invalid"] == 0

def test_multiple_invalid_records():
    records = [
        DatasetRecord("V001", "", "HELLO", "Indoor"),
        DatasetRecord("V002", "Signer1", "UNKNOWN", "Outdoor"),
    ]
    summary = process_dataset(records)
    assert summary["valid"] == 0
    assert summary["invalid"] == 2

def test_mixed_records():
    records = [
        DatasetRecord("V001", "Signer1", "HELLO", "Indoor"),  # valid
        DatasetRecord("V002", "Signer2", "CAR", "Outdoor"),  # invalid sign
        DatasetRecord("V003", "", "MEDICINE", "Indoor"),  # missing signer
    ]
    summary = process_dataset(records)
    assert summary["valid"] == 1
    assert summary["invalid"] == 2


