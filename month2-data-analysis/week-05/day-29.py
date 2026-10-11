#31st August 2026

#Python Practice — Day 29 (First AI Evaluation Tool)
#Part 4 — Q (Challenge): Calculate total predictions, correct, wrong, overall accuracy, number of times "medicine" was predicted, and number of times it was correctly predicted.
#A:
actual = [
    "hello",
    "food",
    "medicine",
    "hello",
    "medicine",
    "food",
    "hello",
    "medicine",
    "food",
    "hello"
]

predicted = [
    "hello",
    "food",
    "food",
    "hello",
    "medicine",
    "medicine",
    "food",
    "medicine",
    "food",
    "hello"
]

correct = 0
wrong = 0
total_prediction = len(predicted)

for a, p in zip(actual, predicted):
    if a == p:
        correct += 1
    else:
        wrong += 1
med = predicted.count("medicine")
c_med = 0
for a, p in zip(actual, predicted):
    if p == ("medicine") and a == ("medicine"):
        c_med += 1

Overall_accuracy = (correct / total_prediction) * 100
print(f"Total predictions: {total_prediction}")
print(f"Correct predictions: {correct}")
print(f"Wrong predictions: {wrong}")
print(f"Overall accuracy: {Overall_accuracy:.1f}%")
print(f"Total Medicine predicted: {med}")
print(f"Correct Medicine predictions: {c_med}")



#Part 5 — Q (Mini Error Analysis): Modify the program to show how many times the model failed to recognize Medicine (actual, correct, missed).
#A:
correct = 0
wrong = 0

for a, p in zip(actual, predicted):
    if a == ("medicine") and p == ("medicine"):
        correct += 1
    elif a == ("medicine") and p != ("medicine"):
        wrong += 1
c_med = actual.count("medicine")

print(f"Medicine actual: {c_med}")
print(f"Correct predictions: {correct}")
print(f"Wrong predictions: {wrong}")


