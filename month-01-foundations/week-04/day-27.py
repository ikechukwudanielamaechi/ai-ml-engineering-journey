#29th August 2026

#Python Practice — Day 27 (CS50P Practical)
#Q (Challenge): Calculate total predictions, correct, wrong, overall accuracy, and MEDICINE's True Positive, False Positive, False Negative, Precision, and Recall — using only CS50P Week 1–4 concepts.
#A:
actual = [
    "hello",
    "food",
    "medicine",
    "medicine",
    "food",
    "hello",
    "medicine",
    "food",
    "hello",
    "medicine"
]
predicted = [
    "hello",
    "medicine",
    "medicine",
    "food",
    "food",
    "hello",
    "food",
    "food",
    "medicine",
    "medicine"
]

total_prediction = len(predicted)
correct = 0
wrong = 0
for a, p in zip(actual, predicted):
    if a == p:
        correct += 1
    else:
        wrong += 1

overall_accuracy = (correct / total_prediction) * 100

true_positive = 0
false_positive = 0
false_negative = 0
for a, p in zip(actual, predicted):
    if p == "medicine" and a == "medicine":
        true_positive += 1
    elif p == "medicine" and a != "medicine":
        false_positive += 1
    elif a == "medicine" and p != "medicine":
        false_negative += 1

precision = true_positive / (true_positive + false_positive) * 100
recall = true_positive / (true_positive + false_negative) * 100

print(f"Total predicted: {total_prediction}")
print(f"Correct predictions: {correct}")
print(f"Wrong predictions: {wrong}")
print(f"Overall accuracy: {overall_accuracy:.1f}%")
print(f"True positive: {true_positive}")
print(f"False positive: {false_positive}")
print(f"False negative: {false_negative}")
print(f"Precision: {precision:.1f}%")
print(f"Recall: {recall:.1f}%")


