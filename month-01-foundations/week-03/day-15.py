#17th August 2026


#Python Practice — Day 15
#Q (Challenge): Combine everything so far into one program — print every age, count adults, count minors, calculate average age, print youngest and oldest participant — written fresh, not copied from a previous solution.
#Answer
participant = int(input("Input total number of Participants: "))
ages = []

for p in range(1, participant + 1):
    participant_age = int(input(f"whats the age of participant {p}: "))
    ages.append(participant_age)

if len(ages) > 0:
    averages = sum(ages) / len(ages)

    adult = 0
    minor = 0

    for age in ages:
        if age >= 18:
            adult += 1
        else:
            minor += 1

    print(f"Ages: {ages}")
    print("How many Adults? ", adult)
    print("How many Minors? ", minor)
    print(f"Average age: {averages}")
    print(f"Youngest Participant: {min(ages)}")
    print(f"Oldest Participant: {max(ages)}")
else:
    print("No participants")


