#23rd August 2026

#Python Practice — Day 21
#Q (Challenge): Create a sign_predictions dictionary and a predict_sign() function that receives a sign, searches the dictionary, and returns the prediction or "Unknown sign." Bonus: make it case-insensitive.
#A (see grading note — function takes no parameter, reads input directly inside itself instead):
sign_predictions = {
    "hello": "HELLO",
    "food": "FOOD",
    "medicine": "MEDICINE",
    "thank_you": "THANK_YOU"
}

def predict_sign():
    sign = input("Enter Sign :").strip().lower().replace(" ", "_")

    if sign in sign_predictions:
        return sign_predictions[sign]
    else:
        return "Unknown Sign"

print(predict_sign())


