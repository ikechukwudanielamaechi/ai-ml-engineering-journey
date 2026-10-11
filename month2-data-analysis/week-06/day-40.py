#11th September 2026

#Python Practice — Day 40 (CS50P Week 6 — Audit Record Reader)

#Read audit.txt, store lines in a list, print total record count. Build find_action(records, keyword) to check whether a keyword appears in any record. Test: keyword exists, doesn't exist, empty list, different capitalization.
#Note on grading: this submission has two real bugs — an incorrect import statement and a loop that returns early — see the strict grading notes in the reply for the corrected version.
#audit.py
audit = []
with open("audit.txt", "r") as file:
    for line in file:
        audit.append(line)
print(*audit)

def find_action(records, keyword):
    for record in records:
        if keyword.strip().lower() in record.lower():
            return True
        else:
            return False


#test_audit.py
from audit import find_action

def test_keyword_exist():
    records = ["V001", "FOOD", "kept"]
    assert find_action(records, "FOOD") == True

def test_keyword_absent():
    records = ["V001", "FOOD", "kept"]
    assert find_action(records, "MEDICINE") == False

def test_keyword_empty():
    records = []
    assert find_action(records, "FOOD") == False

def test_diff_cap():
    records = ["V001", "FOOD", "kept"]
    assert find_action(records, "FooD") == True

