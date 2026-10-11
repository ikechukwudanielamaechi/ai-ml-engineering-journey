#3rd September 2026

#Python Practice — Day 32 (CS50P Week 5 — Recall Function & Tests)
#Q (Challenge): Write calculate_recall(true_positive, false_negative) as a percentage, handling the invalid case where true_positive + false_negative == 0 without allowing invalid division. Write unit tests for TP=9/FN=1→90%, TP=5/FN=5→50%, TP=0/FN=10→0%, and one additional edge case.
#A:
#evaluation.py
def main():
    print(f"{calculate_recall(2, 1):.1f}%")

def calculate_recall(true_positive, false_negative):
    if true_positive + false_negative == 0:
        raise ValueError("Invalid Division ")
    return (true_positive / (true_positive + false_negative)) * 100

if __name__ == "__main__":
    main()


#test_evaluation.py
import pytest
from evaluation import calculate_recall

def test_normal_evaluation():
    assert calculate_recall(9, 1) == 90.0
    assert calculate_recall(5, 5) == 50.0
    assert calculate_recall(3, 7) == 30.0
    assert calculate_recall(0, 10) == 0.0

def test_edge_case():
    with pytest.raises(ValueError):
        assert calculate_recall(0, 0)




