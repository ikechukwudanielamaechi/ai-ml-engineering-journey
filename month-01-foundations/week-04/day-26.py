#28th August 2026

#Python Practice — Day 26 (CS50P Practical)
#Q (Challenge): For the MEDICINE class only, determine True Positives, False Positives, False Negatives, Precision, and Recall from the actual/predicted lists — using only CS50P Week 4 concepts, no libraries.
#A:
actual = [
    "medicine",
    "medicine",
    "food",
    "medicine",
    "hello",
    "medicine",
    "food",
    "medicine",
    "hello",
    "medicine"
]

predicted = [
    "medicine",
    "food",
    "food",
    "medicine",
    "hello",
    "hello",
    "food",
    "medicine",
    "medicine",
    "food"
]
tp = 0
fp = 0
fn = 0

for a, p in zip(actual, predicted):
    if p == "medicine" and a == "medicine":
        tp += 1
    elif p == "medicine" and a != "medicine":
        fp += 1
    elif p != "medicine" and a == "medicine":
        fn += 1

precision = tp / (tp + fp) * 100
recall = tp / (tp + fn) * 100

print(f"True Positive: {tp}")
print(f"False Positive: {fp}")
print(f"False Negative: {fn}")
print(f"Precision: {precision:.1f}%")
print(f"Recall: {recall:.1f}%")


