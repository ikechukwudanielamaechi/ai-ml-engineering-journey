#14th August 2026

#Python Practice — Day 12
#Q (Challenge): Extend yesterday's participant dataset analyzer to calculate and print the average age, the oldest participant, and the youngest participant.
#A (as submitted — see grading notes in the daily journal chat, this code has a bug):

i = int(input("How many participants are in your dataset? "))
ages = []
for i in range(1, i + 1):
    x = int(input(f"Enter age of participants {i}: "))
    ages.append(x)
average = sum(ages) / len(ages)
print("Average age is", average)
m = 0
a = 0
for age in ages:
    if age < 18:
        m += 1
    else:
        a += 1
print("Youngest participant: ", min(ages))
print("Oldest participant: ", max(ages))


