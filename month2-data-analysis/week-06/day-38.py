#9th September 2026

#Python Practice — Day 38 (CS50P Week 6 — Multi-Label Counter)
#Q (Challenge): Read labels.txt, print total labels plus per-sign counts (HELLO, FOOD, MEDICINE, HELP). Add check_count_label(labels, target_label) returning how many times a target appears. Write tests for: appears once, appears multiple times, doesn't appear, empty list, mixed capitalization.
#A (see grading notes — file named "labels.txt" in code rather than the instructed "dataset_labels.txt"; assumed saved as auditor.py to match the test import):
#auditor.py
def check_count_label(labels, target_label="Medicine"):
    count = 0
    for label in labels:
        if label.strip().upper() == target_label.upper():
            count += 1
    return count

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

    hello_count = 0
    for label in labels:
        if label.upper() == "HELLO":
            hello_count += 1

    food_count = 0
    for label in labels:
        if label.upper() == "FOOD":
            food_count += 1

    help_count = 0
    for label in labels:
        if label.upper() == "HELP":
            help_count += 1

    print(f"Total labels: {total_labels}")
    print(f"HELLO: {hello_count}")
    print(f"FOOD: {food_count}")
    print(f"MEDICINE: {medicine_count}")
    print(f"HELP: {help_count}")

    confirm_medicine = check_count_label(labels)
    print(f"Target Label : {confirm_medicine}")

if __name__ == "__main__":
    main()


#test_auditor.py
from auditor import check_count_label

def test_target_appears_once():
    labels = ["HELLO", "MEDICINE", "FOOD"]
    assert check_count_label(labels, "MEDICINE") == 1

def test_target_appears_multiple_times():
    labels = ["MEDICINE", "FOOD", "MEDICINE", "HELP", "MEDICINE"]
    assert check_count_label(labels, "MEDICINE") == 3

def test_target_does_not_appear():
    labels = ["HELLO", "FOOD", "HELP"]
    assert check_count_label(labels, "MEDICINE") == 0

def test_empty_list():
    labels = []
    assert check_count_label(labels, "MEDICINE") == 0

def test_mixed_capitalization():
    labels = ["Medicine", "medicine", "MEDICINE", "MeDiCiNe"]
    assert check_count_label(labels, "mEdIcInE") == 4




