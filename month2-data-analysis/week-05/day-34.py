#5th  September 2026

#Python Practice — Day 34 (CS50P Week 5 — Dataset Label Checker)
#Q (Challenge): Write check_dataset_labels(actual_labels, predicted_labels) that compares two lists and returns the count of correct predictions. Write pytest tests for: all correct, all wrong, mixed, case differences, and empty lists.
#A (submitted — see grading notes for a real syntax bug in dataset.py):
#dataset.py
def check_dataset_labels(actual_labels, predicted_labels):
    correct_count = 0

    if len(actual_labels) != len(predicted_labels):
        raise ValueError("List lengths do not match")

    for i in range(len(actual_labels)):
            if actual_labels[i].lower() == predicted_labels[i].lower():
                correct_count += 1

    return correct_count


#test_dataset.py
import pytest
from dataset import check_dataset_labels

def test_all_correct():
    actual = ["HELLO", "FOOD", "MEDICINE"]
    predicted = ["HELLO", "FOOD", "MEDICINE"]
    assert check_dataset_labels(actual, predicted) == 3

def test_all_wrong():
    actual = ["HELLO", "FOOD", "HELP"]
    predicted = ["BYE", "MEDICINE", "FOOD"]
    assert check_dataset_labels(actual, predicted) == 0

def test_mixed_predictions():
    actual = ["HELLO", "FOOD", "MEDICINE", "HELP"]
    predicted = ["HELLO", "FOOD", "FOOD", "HELP"]
    assert check_dataset_labels(actual, predicted) == 3

def test_case_insensitivity():
    actual = ["hello", "Food", "MEDICINE"]
    predicted = ["HELLO", "food", "medicine"]
    assert check_dataset_labels(actual, predicted) == 3

def test_empty_lists():
    actual = []
    predicted = []
    assert check_dataset_labels(actual, predicted) == 0

def test_mismatched_lengths():
    with pytest.raises(ValueError):
        check_dataset_labels(["HELLO"], ["HELLO", "FOOD"])


