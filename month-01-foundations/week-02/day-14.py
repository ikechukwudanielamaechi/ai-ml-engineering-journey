#16th August 2026

#Python Practice — Day 14
#Q (Challenge): Write a program that calculates total predictions, number correct, number wrong, and accuracy percentage.
#A (submitted — see grading notes for a syntax issue with curly quotes):

i = int(input("How many predictions? "))
prediction = []
for i in range(1, i + 1):
    x = (input("Predict: ")).lower()
    prediction.append(x)
m = 0
a = 0
for c in prediction:
    if c == "correct":
        m += 1
    elif c == "wrong":
        a += 1
accuracy = (m / len(prediction)) * 100
print("Total prediction:", len(prediction))
print("Number Correct:", m)
print("Number Wrong:", a)
print(f"Accuracy: {accuracy}%")


