#26th August 2026

#Python Practice — Day 24 (CS50P × AI Project)
#Part 4 — Q (Challenge): Count how many predictions were "correct" and "wrong" in the list, calculate the accuracy percentage, and print the results.
#A:
predictions = [
    "correct",
    "correct",
    "wrong",
    "correct",
    "wrong",
    "correct",
    "correct",
    "wrong",
    "correct",
    "correct"
]
data = [items.strip() for items in predictions]
correct = data.count("correct")
wrong = data.count("wrong")
total = correct + wrong
accuracy = (correct / total) * 100
print("Total predictions: ", total)
print(f"Correct: {correct}")
print(f"Wrong: {wrong}")
print(f"Accuracy: {accuracy}%")



#Part 5 — Q (Error Analysis Challenge): Given a list of error labels, determine how many errors involved MEDICINE, FOOD, and HELLO, and print the counts.
#A:
errors = [
    "MEDICINE",
    "FOOD",
    "MEDICINE",
    "HELLO",
    "FOOD",
    "MEDICINE"
]
error = [items.strip() for items in errors]
print(f"MEDICINE errors {error.count('MEDICINE')}")
print(f"FOOD errors {error.count('FOOD')}")
print(f"HELLO errors {error.count('HELLO')}")



#BETTER VERSION 
predictions = [
    "correct",
    "correct",
    "wrong",
    "correct",
    "wrong",
    "correct",
    "correct",
    "wrong",
    "correct",
    "correct"
]

correct = predictions.count("correct")
wrong = predictions.count("wrong")
total = len(predictions)
accuracy = (correct / total) * 100

print(f"Total predictions: {total}")
print(f"Correct: {correct}")
print(f"Wrong: {wrong}")
print(f"Accuracy: {accuracy}%")


#PART 2

errors = [
    "MEDICINE",
    "FOOD",
    "MEDICINE",
    "HELLO",
    "FOOD",
    "MEDICINE"
]

print(f"MEDICINE errors: {errors.count('MEDICINE')}")
print(f"FOOD errors: {errors.count('FOOD')}")
print(f"HELLO errors: {errors.count('HELLO')}")



