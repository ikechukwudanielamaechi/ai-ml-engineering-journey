#12th September 2026

#Python Practice — Day 41 (CS50P Week 6, File I/O)
#Task: Create schema.txt with sample records, read the file, store records in a list, print the total number of records, and write find_sign(records, sign) that returns True if the sign appears in the records and False otherwise. Write pytest tests for: sign exists, sign doesn't exist, sign appears later in the list, empty list, different capitalization.
"""schema.txt
Sample ID | Sign | Signer | Environment
V001 | HELLO | S01 | Studio
V002 | FOOD | S02 | Outdoor
V003 | MEDICINE | S01 | Studio
V004 | HELP | S03 | Outdoor"""




#schema.py
schema=[]
with open("schema.txt","r") as file:
    for line in file:
        schema.append(line)
    print(*schema)

def find_sign(records, sign):
    for record in records:
        fields = [field.strip() for field in record.split("|")]
        if len(fields) > 1 and fields[1] == sign.strip():
            return True
    return False




#test_schema.py
from schema import find_sign

@pytest.fixture
def sample_records():
    return[
        "V001 | HELLO | S01 | Studio",
        "V002 | FOOD | S02 |Outdoor",
        "V003 | MEDICINE | S01 |Studio",
        "V004 | HELP | S03 |Outdoor"
    ]

def test_sign_exist(sample_records):
    assert find_sign(sample_records,"FOOD")==True

def test_sign_absent(sample_records):
    assert find_sign(sample_records,"HEY")==False

def test_sign_later_in_list(sample_records):
    assert find_sign(sample_records,"HELP")==True

def test_sign_empty():
    assert find_sign([],"FOOD")==False

def test_diff_cap(sample_records):
    assert find_sign(sample_records,"FooD")==False


