#2nd September 2026

#Python Practice — Day 31 (CS50P Week 5 — Unit Testing)
#Part 1 — Research Challenge program (evaluation logic):
actual = [
    "HELLO",
    "FOOD",
    "MEDICINE",
    "MEDICINE",
    "HELLO",
    "FOOD",
    "MEDICINE",
    "HELLO",
    "FOOD",
    "MEDICINE"
]

predicted = [
    "HELLO",
    "FOOD",
    "FOOD",
    "MEDICINE",
    "HELLO",
    "MEDICINE",
    "MEDICINE",
    "FOOD",
    "FOOD",
    "HELLO"
]
correct = 0
wrong = 0
med_correct = 0
total_prediction = len(predicted)
true_positive = 0
false_negative = 0

for a, p in zip(actual, predicted):
    if a == "MEDICINE" and p == "MEDICINE":
        true_positive += 1
    if a == "MEDICINE" and p != "MEDICINE":
        false_negative += 1

    if a == p:
        correct += 1
    else:
        wrong += 1

actual_med_cases = actual.count("MEDICINE")
overall_accuracy = (correct / total_prediction) * 100
recall = true_positive / (true_positive + false_negative) * 100
print(f"Total Predictions: {total_prediction}")
print(f"Correct Predictions: {correct}")
print(f"Wrong Predictions: {wrong}")
print(f"Overall Accuracy: {overall_accuracy:.1f}%")
print(f"Actual Medicine Cases: {actual_med_cases}")
print(f"Correct Medicine Predictions: {true_positive}")
print(f"Recall: {recall:.1f}%")



#Part 2 — Q (Challenge): Write calculate_accuracy(correct, total) and unit tests covering 8/10→80, 10/10→100, 0/10→0, and one additional edge case.
#A:
#accuracy.py
def main():
    print(calculate_accuracy(8, 10))

def calculate_accuracy(correct, total):
    if total <= 0:
        raise ValueError("Total must be greater than zero.")
    return (correct / total) * 100

if __name__ == "__main__":
    main()


#test_accuracy.py
import pytest
from accuracy import calculate_accuracy

def test_standard_cases():
    assert calculate_accuracy(8, 10) == 80
    assert calculate_accuracy(10, 10) == 100
    assert calculate_accuracy(0, 10) == 0

def test_edge_case_zero_total():
    # Edge case: Division by zero should raise a ValueError
    with pytest.raises(ValueError):
        calculate_accuracy(5, 0)


