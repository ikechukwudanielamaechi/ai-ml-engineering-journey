#6th September 2026

#Python Practice — Day 35 (CS50P Week 5 — Position-Sensitive Prediction Counter)
#Q (Challenge): Write count_correct_predictions(actual_labels, predicted_labels) — verify equal length (raise ValueError if not), compare corresponding labels, count and return correct predictions. Write tests for: all correct, all incorrect, mixed, case-insensitive, empty lists, different lengths, and one test proving corresponding positions matter (not just whether a label exists anywhere in the other list).
#A:
#practice.py
def main():
    print(count_correct_prediction(["HELLO", "FOOD", "MEDICINE", "HELP"], ["HELLO", "FOOD", "FOOD", "HELP"]))

def count_correct_prediction(actual_labels, predicted_labels):
    correct = 0
    if len(actual_labels) != len(predicted_labels):
        raise ValueError("Length Doesn't match")

    for i in range(len(actual_labels)):
        if actual_labels[i].lower() == predicted_labels[i].lower():
            correct += 1
    return correct

if __name__ == "__main__":
    main()


#test_practice.py
from practice import count_correct_prediction
import pytest

def test_all_correct():
    actual = ["HELLO", "HELP", "MEDICINE", "FOOD"]
    predicted = ["HELLO", "HELP", "MEDICINE", "FOOD"]
    assert count_correct_prediction(actual, predicted) == 4

def test_all_incorrect():
    actual = ["HELLO", "HELP", "MEDICINE", "FOOD"]
    predicted = ["HEY", "FOOD", "FOOD", "MEDICINE"]
    assert count_correct_prediction(actual, predicted) == 0

def test_mixed_results():
    actual = ["HELLO", "FOOD", "MEDICINE", "HELP"]
    predicted = ["HELLO", "HELP", "MEDICINE", "FOOD"]
    assert count_correct_prediction(actual, predicted) == 2

def test_case_insensitive():
    actual = ["HELLO", "HELP", "MEDICINE", "FOOD"]
    predicted = ["hello", "help", "medicine", "food"]
    assert count_correct_prediction(actual, predicted) == 4

def test_empty_list():
    actual = []
    predicted = []
    assert count_correct_prediction(actual, predicted) == 0

def test_diff_len():
    with pytest.raises(ValueError):
        count_correct_prediction(["HELLO"], ["HELLO", "HELP"])

def test_position_matters():
    actual = ["HELLO", "HELP", "MEDICINE", "FOOD"]
    predicted = ["HELP", "HELLO", "FOOD", "MEDICINE"]
    assert count_correct_prediction(actual, predicted) == 0


