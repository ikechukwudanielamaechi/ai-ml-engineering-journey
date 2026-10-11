#24th August 2026

#Python Practice — Day 22
#Q (Challenge): Create prediction = {"prediction": "HELLO", "confidence": 0.94, "model_version": "1.0"} and print each value. Bonus: ask the user for prediction and confidence and construct the dictionary dynamically.
#A (bonus version submitted):
prediction = input("Prediction: ")
confidence = float(input("Confidence: "))

new_sign_prediction = {
    "prediction": prediction,
    "confidence": confidence
}

print(f"Prediction :{new_sign_prediction['prediction']}")
print(f"Confidence :{new_sign_prediction['confidence']}")

