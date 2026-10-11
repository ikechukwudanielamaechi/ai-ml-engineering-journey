#19th August 2026

#Python Practice — Day 17
#Q (Challenge): Simulate gradient descent — start with weight = 10, target = 0, learning rate = 0.2. Calculate the error, update the weight, repeat 10 times, printing the weight after every update.
#A (submitted — see grading note: the print statement runs before the update, so it shows the weight before each step rather than after):
weight = 10
target = 0
learning_rate = 0.2

for step in range(10):
    print(f"How far am i from the target? {weight}")
    error = weight - target
    weight = weight - (learning_rate * error)


