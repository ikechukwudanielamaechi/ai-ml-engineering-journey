#13th August 2026
#Python Practice — Day 11
#Q (Challenge): Write a program that asks how many participants are in the dataset, collects their ages into a list, then determines how many participants are 18 or older and how many are under 18, and prints both numbers.
#
# A:
i = int(input("How many participants are in your dataset? "))
ages = []

for i in range(1, i + 1):
    x = int(input(f"Enter age of participant {i}: "))
    ages.append(x)

minor = 0
adult = 0

for age in ages:
    if age < 18:
        minor += 1
    else:
        adult += 1

print("Minors: ", minor)
print("Adults: ", adult)


