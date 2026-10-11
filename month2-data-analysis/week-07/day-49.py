#20th September 2026


#Python Practice — Day 49 (CS50P Week 8 — Dataset Profiler with Frames)

#Build count_by_sign, count_by_signer, total_frames, average_frames, most_common_sign over a 5-record dataset. Test: normal dataset, empty dataset, multiple signers, repeated sign, different frame counts, average calculation.
#Critical bug found — see grading notes in the reply. count_by_sign() has mismatched indentation between its first two lines — the same class of IndentationError flagged on Day 47's count_signers(). This would prevent the entire module from being imported, meaning none of the tests could even run.
#project_bridge_profile.py
records = [
    {"video_id": "V001", "signer": "S01", "sign": "HELLO", "frames": 30},
    {"video_id": "V002", "signer": "S01", "sign": "HELLO", "frames": 25},
    {"video_id": "V003", "signer": "S02", "sign": "FOOD", "frames": 40},
    {"video_id": "V004", "signer": "S02", "sign": "MEDICINE", "frames": 35},
    {"video_id": "V005", "signer": "S03", "sign": "HELP", "frames": 30},
]

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

def total_frames(records):
    total = 0
    for record in records:
        total += record["frames"]
    return total

def average_frames(records):
    if not records:
        return 0.0
    return total_frames(records) / len(records)

def most_common_sign(records):
    if not records:
        return None

    sign_counts = count_by_sign(records)
    most_common = None
    highest_count = 0

    for sign, count in sign_counts.items():
        if count > highest_count:
            highest_count = count
            most_common = sign

    return most_common


test_project_bridge_profile.py
import pytest
from project_bridge_profile import (
    average_frames,
    count_by_sign,
    count_by_signer,
    most_common_sign,
    total_frames,
)

@pytest.fixture
def sample_records():
    return [
        {"video_id": "V001", "signer": "S01", "sign": "HELLO", "frames": 30},
        {"video_id": "V002", "signer": "S01", "sign": "HELLO", "frames": 25},
        {"video_id": "V003", "signer": "S02", "sign": "FOOD", "frames": 40},
        {"video_id": "V004", "signer": "S02", "sign": "MEDICINE", "frames": 35},
        {"video_id": "V005", "signer": "S03", "sign": "HELP", "frames": 30},
    ]

def test_normal_dataset(sample_records):
    assert count_by_sign(sample_records) == {
        "HELLO": 2,
        "FOOD": 1,
        "MEDICINE": 1,
        "HELP": 1,
    }

def test_empty_dataset():
    empty_records = []
    assert count_by_sign(empty_records) == {}
    assert count_by_signer(empty_records) == {}
    assert total_frames(empty_records) == 0
    assert average_frames(empty_records) == 0.0  # Prevents division by zero
    assert most_common_sign(empty_records) is None

def test_multiple_signers(sample_records):
    signer_counts = count_by_signer(sample_records)
    assert signer_counts == {"S01": 2, "S02": 2, "S03": 1}

def test_repeated_sign(sample_records):
    assert most_common_sign(sample_records) == "HELLO"

def test_different_frame_counts(sample_records):
    assert total_frames(sample_records) == 160

def test_average_calculation(sample_records):
    assert average_frames(sample_records) == 32.0


