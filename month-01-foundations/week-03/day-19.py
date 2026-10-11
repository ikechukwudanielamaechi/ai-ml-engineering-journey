#21st August 2026

#Python Practice — Day 19
#Q (Challenge): Given scores = [92, 88, 95, 90, 85], calculate the average, highest, and lowest score, and print all three. Bonus: calculate the difference between highest and lowest.
#A:
scores = (92, 88, 95, 90, 85)
difference = (max(scores) - min(scores))
average = sum(scores) / len(scores)
print(f"Average : {average}")
print(f"Highest : {max(scores)}")
print(f"Lowest : {min(scores)}")
print(f"Difference : {difference}")


