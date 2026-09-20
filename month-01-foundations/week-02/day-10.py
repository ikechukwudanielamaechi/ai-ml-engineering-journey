#12th August 2026
# Python Practice — Day 10
#Questions and Answers

"""
Topic: Working with individual items inside a list
List used: ages = [22, 35, 28, 41, 19]

Q1: How would you get the first age?
A: In Python, the index always starts with zero. So 22 is index zero, 35 is index one, 28 is index two, 41 is index three, 19 is index four. So to print the first age, we use print(ages[0]). It prints 22.

Q2: How would you get the last age?
A: You do the same thing, but the index will be four: ages[4].

Q3: If you wanted Python to print every age individually, what kind of loop could you use?
A: We will use a for loop to print it individually.

Q4 (Challenge): Write a program that loops through the list and prints only the ages that are 30 or older.
A:"""
ages = [22, 35, 28, 41, 19]
for age in ages:
    if age >= 30:
        print(age)

