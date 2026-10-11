#19th September 2026


#Python Practice — Day 48 (CS50P Week 8 — Distribution Profiling)

#Build count_by_sign, count_by_signer, count_by_environment, percentage_by_sign, most_common_sign, and least_common_sign. Test: balanced dataset, imbalanced dataset, one signer multiple times, multiple signers, one sign appearing once, empty dataset, all records one sign, mixed environments, and a case where the least common sign is deliberately not the last record (checking for early-return bugs).
#Note: hand-traced all 9 tests — every one checks out correctly, including the deliberate early-return check. No indentation issues this time either.
#project_bridge_distribution.py
def count_by_sign(records):
    counts = {}
    for record in records:
        sign = record["sign"]
        if sign in counts:
            counts[sign] += 1
        else:
            counts[sign] = 1
    return counts

def count_by_signer(records):
    counts = {}
    for record in records:
        signer = record["signer"]
        if signer in counts:
            counts[signer] += 1
        else:
            counts[signer] = 1
    return counts

def count_by_environment(records):
    counts = {}
    for record in records:
        env = record["environment"]
        if env in counts:
            counts[env] += 1
        else:
            counts[env] = 1
    return counts

def percentage_by_sign(records):
    if not records:
        return {}

    counts = count_by_sign(records)
    total_records = len(records)
    percentages = {}

    for sign, count in counts.items():
        percentages[sign] = round((count / total_records) * 100, 1)

    return percentages

def most_common_sign(records):
    if not records:
        return None

    counts = count_by_sign(records)
    most_common = None
    highest_count = -1

    for sign, count in counts.items():
        if count > highest_count:
            highest_count = count
            most_common = sign

    return most_common

def least_common_sign(records):
    if not records:
        return None

    counts = count_by_sign(records)
    least_common = None
    lowest_count = float("inf")

    for sign, count in counts.items():
        if count < lowest_count:
            lowest_count = count
            least_common = sign

    return least_common


#test_project_bridge_distribution.py
import pytest
from project_bridge_distribution import (
    count_by_environment,
    count_by_sign,
    count_by_signer,
    least_common_sign,
    most_common_sign,
    percentage_by_sign,
)

def test_balanced_dataset():
    records = [
        {"video_id": "V001", "signer": "S01", "sign": "HELLO", "environment": "Indoor"},
        {"video_id": "V002", "signer": "S02", "sign": "FOOD", "environment": "Outdoor"},
    ]
    assert count_by_sign(records) == {"HELLO": 1, "FOOD": 1}
    assert percentage_by_sign(records) == {"HELLO": 50.0, "FOOD": 50.0}

def test_imbalanced_dataset():
    records = [
        {"video_id": "V001", "signer": "S01", "sign": "HELLO", "environment": "Indoor"},
        {"video_id": "V002", "signer": "S01", "sign": "FOOD", "environment": "Indoor"},
        {"video_id": "V003", "signer": "S02", "sign": "FOOD", "environment": "Outdoor"},
        {"video_id": "V004", "signer": "S03", "sign": "MEDICINE", "environment": "Indoor"},
    ]
    assert count_by_sign(records) == {"HELLO": 1, "FOOD": 2, "MEDICINE": 1}
    assert percentage_by_sign(records) == {"HELLO": 25.0, "FOOD": 50.0, "MEDICINE": 25.0}

def test_one_signer_multiple_times():
    records = [
        {"video_id": "V001", "signer": "S01", "sign": "HELLO", "environment": "Indoor"},
        {"video_id": "V002", "signer": "S01", "sign": "FOOD", "environment": "Outdoor"},
        {"video_id": "V003", "signer": "S01", "sign": "HELP", "environment": "Indoor"},
    ]
    assert count_by_signer(records) == {"S01": 3}

def test_multiple_signers():
    records = [
        {"video_id": "V001", "signer": "S01", "sign": "HELLO", "environment": "Indoor"},
        {"video_id": "V002", "signer": "S02", "sign": "FOOD", "environment": "Outdoor"},
        {"video_id": "V003", "signer": "S03", "sign": "HELP", "environment": "Indoor"},
    ]
    assert count_by_signer(records) == {"S01": 1, "S02": 1, "S03": 1}

def test_one_sign_appearing_once():
    records = [
        {"video_id": "V001", "signer": "S01", "sign": "HELLO", "environment": "Indoor"},
        {"video_id": "V002", "signer": "S02", "sign": "HELLO", "environment": "Outdoor"},
        {"video_id": "V003", "signer": "S03", "sign": "HELP", "environment": "Indoor"},
    ]
    assert least_common_sign(records) == "HELP"
    assert count_by_sign(records)["HELP"] == 1

def test_empty_dataset():
    records = []
    assert count_by_sign(records) == {}
    assert count_by_signer(records) == {}
    assert count_by_environment(records) == {}
    assert percentage_by_sign(records) == {}
    assert most_common_sign(records) is None
    assert least_common_sign(records) is None

def test_all_records_one_sign():
    records = [
        {"video_id": "V001", "signer": "S01", "sign": "HELLO", "environment": "Indoor"},
        {"video_id": "V002", "signer": "S02", "sign": "HELLO", "environment": "Outdoor"},
    ]
    assert count_by_sign(records) == {"HELLO": 2}
    assert most_common_sign(records) == "HELLO"
    assert least_common_sign(records) == "HELLO"
    assert percentage_by_sign(records) == {"HELLO": 100.0}

def test_mixed_environments():
    records = [
        {"video_id": "V001", "signer": "S01", "sign": "HELLO", "environment": "Indoor"},
        {"video_id": "V002", "signer": "S02", "sign": "FOOD", "environment": "Outdoor"},
        {"video_id": "V003", "signer": "S03", "sign": "HELP", "environment": "Indoor"},
    ]
    assert count_by_environment(records) == {"Indoor": 2, "Outdoor": 1}

def test_least_common_sign_not_at_the_end():
    records = [
        {"video_id": "V001", "signer": "S01", "sign": "HELLO", "environment": "Indoor"},
        {"video_id": "V002", "signer": "S02", "sign": "FOOD", "environment": "Outdoor"},  # Least common
        {"video_id": "V003", "signer": "S03", "sign": "HELLO", "environment": "Indoor"},
        {"video_id": "V004", "signer": "S04", "sign": "HELLO", "environment": "Outdoor"},
    ]
    assert least_common_sign(records) == "FOOD"


