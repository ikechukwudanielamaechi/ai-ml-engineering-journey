#20th August 2026

#Python Practice — Day 18
#Q (Challenge): Create the list [12, 15, 18, 21, 25, 30, 35, 40], set batch_size = 2, use a loop to process the participants in groups of 2, and print each batch.
#ANSWER:
ages = [12, 15, 18, 21, 25, 30, 35, 40]
batch_size = 2
for age in range(1, 5):
    start = (age - 1) * batch_size
    end = start + batch_size
    print(f"Batch {age}: {ages[start:end]}")



#Minor Python note: Your batch-processing code works correctly and produces the right output, but it hardcodes range(1, 5) instead of calculating the number of batches from len(ages) and batch_size. It works fine for exactly 8 items in batches of 2, but if you changed the list size, you’d have to manually recalculate the range every time. 

#A more robust version would be 

#for i in range(0, len(ages), batch_size),

#which adapts automatically — worth knowing since real training loops always calculate batch counts dynamically rather than hardcoding them.
