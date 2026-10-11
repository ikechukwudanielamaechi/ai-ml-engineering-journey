#1st September 2026

#Python Practice — Day 30 (CS50P — Dataset Concept)
#Q (Challenge): Store signs in a list, count how many times each sign appears, print total samples, print counts per sign, and identify which sign appears the most. No NumPy/Pandas — CS50P Weeks 1–4 only.
#A:
signs = [
    "HELLO",
    "FOOD",
    "MEDICINE",
    "FOOD",
    "MEDICINE"
]
counts = {}
hello = signs.count("HELLO")
food = signs.count("FOOD")
medicine = signs.count("MEDICINE")
counts["HELLO"] = hello
counts["FOOD"] = food
counts["MEDICINE"] = medicine
total = len(signs)
max_count = max(counts.values())
most_frequent = [sign for sign, count in counts.items() if count == max_count]

print(f"Total samples: {total}")
print(f"HELLO samples: {hello}")
print(f"FOOD samples: {food}")
print(f"MEDICINE samples: {medicine}")
print(f"Most frequent sign: {most_frequent}")


