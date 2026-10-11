#4th September 2026

#Python Practice — Day 33 (CS50P Week 5 — Label Check)
#Q (Challenge): Write check_label(actual, predicted) that determines whether two labels agree ("correct"/"incorrect"). Write unit tests covering: same labels, different labels, HELLO vs HELLO, FOOD vs MEDICINE, and one additional test case.
#A (files submitted as accuracy.py / test_accuracy.py rather than label_check.py / test_label_check.py — see grading notes):
#accuracy.py
def main():
    print(check_label("Hello", "hello"))

def check_label(actual, predicted):
    if actual.upper() == predicted.upper():
        return "correct"
    else:
        return "incorrect"

if __name__ == "__main__":
    main()


#test_accuracy.py
from accuracy import check_label
import pytest

def test_same_label():
    assert check_label("HELLO", "HELLO") == "correct"
    assert check_label("MEDICINE", "MEDICINE") == "correct"

def test_diff_label():
    assert check_label("HELLO", "MEDICINE") == "incorrect"
    assert check_label("MEDICINE", "HELLO") == "incorrect"

def test_edge_case():
    pytest.raises(ValueError)
    check_label("HELLO", "hello")



