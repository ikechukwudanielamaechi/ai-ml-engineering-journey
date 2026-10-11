#23rd September 2026

"""Python Practice
Create:
day52_numpy_vectorization.py
Stay within what you’ve actually learned.

#Part 1
import numpy as np

scores = np.array([10, 20, 30, 40, 50])
Create and print:
scores + 10
scores - 5
scores * 2
scores / 10

Part 2 — Array-to-array operations
Create:
a = np.array([10, 20, 30, 40])
b = np.array([1, 2, 3, 4])
Print:
a + b
a - b
a * b

Part 3 — Project Bridge
Create:
landmarks = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
Treat each row as:
[x, y, z]
Then create:
shifted = landmarks + 5
Print:
original landmarks
shifted landmarks
original shape
shifted shape

Assertions
Add assertions to verify some of your results.
For example:
assert (scores + 10)[0] == 20
You should also test that vectorized operations preserve the expected shape.
For example, if:
landmarks.shape == (3,3)
then verify:
(landmarks + 5).shape == (3,3)
Add at least four useful assertions.
Don’t just assert things because the exercise asks for four. Each assertion should test something meaningful.

"""

#PYTHON ANSWERS 
import numpy as np
#Part one (1)
score=np.array([10,20,30,40,50])
print(f"Addition : {score+10}")
print(f"Subtraction : {score-5}")
print(f"Multiplication : {score*2}")
print(f"Division : {score/10}")

#Part two (2) Array to Array Operations

a=np.array([10,20,30,40])
b=np.array([1,2,3,4])
print(f"\nAddition : {a+b}")
print(f"Subtraction : {a-b}")
print(f"Multiplication : {a*b}")


#Part three (3) Project bridge
landmarks=np.array([
             [10,20,30],
             [40,50,60],
             [70,80,90]
             ])
shifted=landmarks + 5
print(f"\nOriginal Landmark : {landmarks}")
print(f"Shifted Landmark : {shifted}")
print(f"Original Shape : {landmarks.shape}")
print(f"Shifted Shape : {shifted.shape}")


#Assertions
assert shifted.shape == landmarks.shape
assert shifted[0,0] == landmarks[0,0] + 5
assert landmarks[0,0] == 10
assert np.array_equal(shifted - landmarks,np.full_like(landmarks,5))


