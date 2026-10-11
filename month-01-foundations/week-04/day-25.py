#27th August 2026

#Python Practice — Day 25 (CS50P × AI Practical)
#Part 5 — Q (Challenge): Given actual and predicted lists, count total predictions, correct, wrong, calculate accuracy, and count how many times medicine/food/hello were predicted.
#A:
actual = [
    "hello",
    "food",
    "medicine",
    "medicine",
    "food",
    "hello",
    "medicine",
    "food"
]

predicted = [
    "hello",
    "medicine",
    "medicine",
    "food",
    "food",
    "hello",
    "food",
    "food"
]

correct = 0
wrong = 0
total = len(predicted)
for a, p in zip(actual, predicted):
    if a == p:
        correct += 1
    else:
        wrong += 1
accuracy = (correct / total) * 100
med = predicted.count("medicine")
food = predicted.count("food")
hello = predicted.count("hello")

print(f"Total predicted: {total}")
print(f"Correct Prediction: {correct}")
print(f"Wrong Predicted: {wrong}")
print(f"Accuracy: {accuracy:.1f}%")
print(f"Medicine predicted: {med}")
print(f"food predicted: {food}")
print(f"hello predicted: {hello}")



#Part 6 — Q (Mini Error Analysis): Find the cases where Actual = MEDICINE but Prediction ≠ MEDICINE. How many times did the model fail to recognise MEDICINE, and what did it predict instead?
#A:
actual = [
    "hello",
    "food",
    "medicine",
    "medicine",
    "food",
    "hello",
    "medicine",
    "food"
]

predicted = [
    "hello",
    "medicine",
    "medicine",
    "food",
    "food",
    "hello",
    "food",
    "food"
]

failed = 0
incorrect = []

for a, p in zip(actual, predicted):
    if a == "medicine" and p != "medicine":
        failed += 1
        incorrect.append(p)

print(f"Number of times it failed: {failed}")
print(f"What it predicted instead: {incorrect}")


