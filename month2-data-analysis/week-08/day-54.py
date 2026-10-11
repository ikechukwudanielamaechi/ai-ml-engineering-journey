#25th September 2026
"""
🐍 Python Practice
Stay within your current NumPy level.
Create:
import numpy as np
Then complete these.
Task 1 — vectors
a = np.array([2, 4, 6])
b = np.array([1, 3, 5])
Calculate:
a + b
a - b
2 * a
np.dot(a, b)
a @ b

Task 2 — matrices
Create:
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])
Calculate:
A * B
and:
A @ B
Then explain why the answers differ.

Task 3 — shape investigation
Create:
A = np.zeros((3, 4))
B = np.zeros((4, 2))
Calculate:
C = A @ B
Print:
A.shape
B.shape
C.shape
Then explain why the result has that shape.

Task 4 — Project Bridge
Create:
landmarks = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

scale = 2
Create a new array where every coordinate is multiplied by scale.
Then verify:
assert scaled.shape == landmarks.shape
Add at least two more assertions that test something meaningful about your result.
"""
#PYTHON ANSWERS 
import numpy as np
# Task 1 vector
a = np.array([2, 4, 6])
b = np.array([1, 3, 5])
print("Summing: ", a + b)
print("Subtracting: ", a - b)
print("Multiplying: ", a * b)
print("Dot: ", np.dot(a, b))
print("Matrix Mult: ", a @ b)


# Task 2 Matrices
A = np.array([
     [1, 2],
     [3, 4]
 ])
B = np.array([
     [5, 6],
     [7, 8]
 ])
print("\nMultiplying: ", A * B)
print("Matrix Mult: ", A @ B)


# Task 3 Shape investigation
A = np.zeros((3, 4))
B = np.zeros((4, 2))
C = A @ B
print("\nShape A: ", A.shape)
print("Shape B: ", B.shape)
print("Shape C: ", C.shape)


# Task 4 Project Bridge
landmarks = np.array([
     [10, 20, 30],
     [40, 50, 60],
     [70, 80, 90]
 ])
scale = 2
scaled = landmarks * scale
print("\n Scaled\n", scaled)
print("\nScaled shape", scaled.shape)
print("\nLandmarks shape", landmarks.shape)
assert scaled.shape == landmarks.shape
assert scaled.dtype == landmarks.dtype
assert np.array_equal(scaled, np.array([
     [20, 40, 60],
     [80, 100, 120],
     [140, 160, 180]
 ]))
print("Test Successfully Passed")



