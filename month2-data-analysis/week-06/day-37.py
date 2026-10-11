#8th September 2026

#Python Practice — Day 37 (CS50P Week 6 — Dataset Label Auditor)
#Q (Challenge): Read labels from labels.txt, count total labels and MEDICINE occurrences, print results. Add check_label_count(...) to determine whether MEDICINE appears at least 2 times. Write tests for: MEDICINE appearing 2, 3, 1, and 0 times, plus reasoning about the empty-file edge case.
#A:
#auditor.py
def check_label_count(labels, target_label="MEDICINE", min_count=2):
    count = 0
    for label in labels:
        if label.strip().upper() == target_label.upper():
            count += 1
    return count >= min_count

def main():
    labels = []

    with open("labels.txt", "r") as file:
        for line in file:
            labels.append(line.strip())

    total_labels = len(labels)

    medicine_count = 0
    for label in labels:
        if label.upper() == "MEDICINE":
            medicine_count += 1

    print(f"Total labels: {total_labels}")
    print(f"MEDICINE count: {medicine_count}")

    has_enough = check_label_count(labels)
    print(f"Meets threshold (>=2): {has_enough}")

if __name__ == "__main__":
    main()


#test_auditor.py
from auditor import check_label_count

def test_medicine_appears_twice():
    labels = ["HELLO", "MEDICINE", "FOOD", "MEDICINE"]
    assert check_label_count(labels) == True

def test_medicine_appears_thrice():
    labels = ["MEDICINE", "FOOD", "MEDICINE", "HELP", "MEDICINE"]
    assert check_label_count(labels) == True

def test_medicine_appears_once():
    labels = ["HELLO", "FOOD", "MEDICINE", "HELP"]
    assert check_label_count(labels) == False

def test_medicine_absent():
    labels = ["HELLO", "FOOD", "HELP"]
    assert check_label_count(labels) == False

def test_empty_labels():
    labels = []
    assert check_label_count(labels) == False





