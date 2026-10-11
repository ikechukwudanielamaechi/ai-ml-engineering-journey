#25th August 2026

#Python Practice — Day 23
#Q (Challenge): Write a program that receives a sign prediction and confidence level. Print the prediction. If confidence ≥ 0.90, print "High confidence". If 0.70–0.89, print "Medium confidence". If below 0.70, print "Low confidence - confirmation required". Bonus: store prediction and confidence in a dictionary.
#A (see grading note — the "Low confidence" message is missing the "confirmation required" part):
prediction = input("Prediction: ")
confidence = float(input("Confidence: "))

prediction_data = {
    "prediction": prediction,
    "confidence": confidence
}

def sign():
    print(f"Prediction :{prediction_data['prediction']}")
    if confidence >= 0.90:
        print("High Confidence")
    elif 0.70 <= confidence <= 0.89:
        print("Medium confidence")
    elif confidence < 0.70:
        print("Low confidence")

sign()



