#15th August 2026

#Python Practice — Day 13
#Q (Challenge): Extend the dataset analyzer to calculate average age, youngest participant, oldest participant, number of minors, number of adults, and number of participants. Bonus: calculate the percentage of participants who are adults.
#A (bonus percentage-of-adults calculation not included — see grading notes):

i = int(input("How many participants are in your dataset? "))
ages = []
for i in range(1, i + 1):
    x = int(input(f"Enter age of participants {i}: "))
    ages.append(x)
average = sum(ages) / len(ages)
print("Average age is ", average)
m = 0
a = 0
for age in ages:
    if age < 18:
        m += 1
    else:
        a += 1
print("Youngest Participant: ", min(ages))
print("Oldest Participant: ", max(ages))
print("Number of minor:", m)
print("Number of adult:", a)
print("Number of Participant:", len(ages))


