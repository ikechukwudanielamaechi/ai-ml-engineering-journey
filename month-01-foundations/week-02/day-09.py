#11th August 2026
#🐍 Evening Python Mission
"""
Yesterday you discovered that you need a way to store multiple participant ages.
Today we’re introducing:
Python Lists
Before I teach you the syntax, try answering:
Q1
What do you think a Python list is?
Q2
Why would a list be useful for our participant-age problem?

Q3
if you had 
23,43,12,45,22,67
how would you want python to store these five values so taht you can later store the average

"""
#Answer Python 
"""
1. In simple term, list in Python,
 lists  are made using square bracket 
 that enables a variable to store more datas in it.

2. The list helps in an order changeable collection of data.

3 The Python program can store this using a list. 
for instance, you create a variable called values. 
Values equals to square bracket. So now each of these figures, 
you end it with a comma. So it's stored in a list to be used.
"""

#challenge Questions

"""build the program
1. ask how participants are there
2. create an empty list called Ages
3. use loop
4. add each age to Ages
5. calc and print the Average

"""

user =int(input ("How many participants are in your dataset? "))
ages= [ ]
for i in range (1,user+1):
    age=int(input (f"Enter age of participants {i}: "))
    ages.append(age)

average=sum(ages)/len(ages)
print ("Average age is ", average)



