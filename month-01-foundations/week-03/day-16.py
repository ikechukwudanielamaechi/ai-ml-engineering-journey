#18th August 2026


#Python Practice — Day 16
#Q (Challenge): Write a program that asks for the correct answer and the AI's prediction, checks if they match, prints "Correct prediction" or "Wrong prediction," and counts the result. Bonus: run 10 predictions and calculate overall accuracy.
#A:
prediction = int(input("How many predictions do you want to make? : "))
prediction_lists = []
a = 0

for pdt in range(1, prediction + 1):
    answer = input(f"Correct Answer: {pdt}: ")
    ai_answer = input(f"AI Prediction {pdt}: ")
    prediction_lists.append([answer, ai_answer])

    if answer.lower() == ai_answer.lower():
        print("Correct Prediction ")
        a += 1
    else:
        print("Wrong Prediction")

accuracy = (a / prediction) * 100
print(f"\nOverall Accuracy: {accuracy:.2f}% ")
print(f"Overall Score: ({a}/{prediction})")


