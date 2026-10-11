#30th August 2026

#Python Practice — Day 28 (CS50P Practical)
#Q (Challenge): Print each model's name, accuracy, and latency; find the model with the highest accuracy and the model with the lowest latency.
#A:
models = ["Model A", "Model B", "Model C"]
accuracy = [97, 94, 91]
latency = [2.5, 0.4, 0.08]

for name, acc, lat in zip(models, accuracy, latency):
    print(f"{name} - Accuracy: {acc}% - Latency: {lat} seconds")

print()

highest_accuracy = accuracy.index(max(accuracy))
print(f"Highest accuracy {models[highest_accuracy]}")

lowest_latency = latency.index(min(latency))
print(f"Lowest latency: {models[lowest_latency]}")


