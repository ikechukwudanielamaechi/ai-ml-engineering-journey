#10th September 2026


#Python Practice — Day 39 (CS50P Week 6 — Experiment Record Reader)
#Q (Challenge): Read experiment.txt, store lines in a list, print the number of lines and each line. Add find_record(records, keyword) to search for a keyword across records. Write tests for: keyword exists, doesn't exist, empty records, different capitalization.
#A (see grading notes — a duplicate function name in the tests silently overwrites one test case):
#assignment.py
saved_list = []
with open("experiment.txt", "r") as file:
    for line in file:
        saved_list.append(line.strip())

total_len = len(saved_list)
print(f"{total_len}")
print(f"{saved_list}")

def find_record(records, keywords):
    for record in records:
        if keywords.strip().lower() in record.lower():
            return True
    return False


#test_assignment.py
from assignment import find_record

def test_keyword_exist():
    records = ["Dataset metadata", "Signer 01", "Label alignment"]
    assert find_record(records, "Dataset") == True

def test_keyword_absent():
    records = ["Signer 01", "Label alignment"]
    assert find_record(records, "Dataset") == False

def test_keyword_empty():
    records = []
    assert find_record(records, "Dataset") == False

def test_keyword_diffcase():
    records = ["Signer 01", "Label alignment"]
    assert find_record(records, "sIgNER") == True


