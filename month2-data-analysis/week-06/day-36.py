#7th September 2026

#Python Practice — Day 36 (CS50P Week 6 — File-Based Evaluation)
#Q (Challenge): Read actual labels from labels.txt and predictions from predictions.txt, compare corresponding labels, count correct predictions, and raise ValueError if the files have different numbers of labels. Write tests for: all correct, all wrong, mixed, case differences, empty data, mismatched lengths, and position mismatch.
#A:
#assignment.py
def read_label_from_file(filename):
    labels = []
    with open(filename, "r") as file:
        for line in file:
            labels.append(line.rstrip())
    return labels

def evaluate_predictions(actual_file, predicted_file):
    actual = read_label_from_file(actual_file)
    prediction = read_label_from_file(predicted_file)
    if len(actual) != len(prediction):
        raise ValueError("Length not the same")

    correct = 0
    for i in range(len(actual)):
        if actual[i].lower() == prediction[i].lower():
            correct += 1
    return correct

def main():
    try:
        correct_count = evaluate_predictions("labels.txt", "predictions.txt")
        print(correct_count)
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()


#test_assignment.py
from assignment import evaluate_predictions
import pytest

def test_all_correct(tmp_path):
    label = tmp_path/"labels.txt"
    predicted = tmp_path/"predictions.txt"
    label.write_text("HELLO\nFOOD\nMEDICINE\n")
    predicted.write_text("HELLO\nFOOD\nMEDICINE\n")
    assert evaluate_predictions(label, predicted) == 3

def test_all_incorrect(tmp_path):
    label = tmp_path/"labels.txt"
    predicted = tmp_path/"predictions.txt"
    label.write_text("HELLO\nFOOD\nMEDICINE\n")
    predicted.write_text("HEY\nHELLO\nFOOD\n")
    assert evaluate_predictions(label, predicted) == 0

def test_mixed_results(tmp_path):
    label = tmp_path/"labels.txt"
    predicted = tmp_path/"predictions.txt"
    label.write_text("HELLO\nFOOD\nMEDICINE\n")
    predicted.write_text("HELLO\nHELP\nMEDICINE\n")
    assert evaluate_predictions(label, predicted) == 2

def test_case_insensitive(tmp_path):
    label = tmp_path/"labels.txt"
    predicted = tmp_path/"predictions.txt"
    label.write_text("HELLO\nFOOD\nMEDICINE\n")
    predicted.write_text("hello\nfood\nmedicine\n")
    assert evaluate_predictions(label, predicted) == 3

def test_empty_data(tmp_path):
    label = tmp_path/"labels.txt"
    predicted = tmp_path/"predictions.txt"
    label.write_text("")
    predicted.write_text("")
    assert evaluate_predictions(label, predicted) == 0

def test_diff_length(tmp_path):
    label = tmp_path/"labels.txt"
    predicted = tmp_path/"predictions.txt"
    label.write_text("HELLO\nFOOD\nMEDICINE\nHELP")
    predicted.write_text("HELLO\nFOOD\nMEDICINE\n")
    with pytest.raises(ValueError):
        evaluate_predictions(label, predicted)

def test_position_mismatch(tmp_path):
    label = tmp_path/"labels.txt"
    predicted = tmp_path/"predictions.txt"
    label.write_text("HELLO\nFOOD\n")
    predicted.write_text("FOOD\nHELLO\n")
    assert evaluate_predictions(label, predicted) == 0


