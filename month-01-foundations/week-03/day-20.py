#22nd August 2026

#Python Practice — Day 20
#Q (Challenge): Using the sign_predictions dictionary, ask the user to enter a sign and print the prediction. The program shouldn't crash if the user enters something not in the dictionary — no loop yet, just a single input → prediction mapping.
#A:
sign_predictions = {
    "hello": "HELLO",
    "thank_you": "THANK_YOU",
    "medicine": "MEDICINE",
    "food": "FOOD"
}

sign = input("Enter Sign: ").lower()
if sign in sign_predictions:
    print("Prediction: ", sign_predictions[sign])
else:
    print("Prediction: Unknown Sign")


