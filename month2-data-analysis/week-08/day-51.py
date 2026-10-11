#22nd September 2026

#Python Practice — CS50P + NumPy Only
#Create:
#Plain text
#day51_numpy_indexing.py
#Use only concepts you have actually learned.
#Part 1 — 1D array
#Create:
#Python
"""scores = np.array([10, 20, 30, 40, 50])
Print:
 * first value
 * third value
 * last value
 * values from index 1 through 3
"""
#PYTHON ANSWERS

import numpy as np

# 1D Array Questions and Answers
score = np.array(
     [10, 20, 30, 40, 50]
 )
print(f"First Value: {score[0]}")
print(f"Third Value: {score[2]}")
print(f"Last Value: {score[-1]}")
print(f"Index Value: {score[1:4]}")



#Part 2 — 2D array QUESTION 
#Create:
"""Python
matrix = np.array([
[10, 20, 30],
[40, 50, 60],
[70, 80, 90]
])
Print:
 * 10
 * 50
 * 90
 * the second row
 * the first column
 * the last two columns"""
# 2D Array Questions and Answers

matrix = np.array([
     [10, 20, 30],
     [40, 50, 60],
     [70, 80, 90]
 ])
print(matrix[0, 0])
print(matrix[1, 1])
print(matrix[2, 2])
print(f"Printing The entire second Row: {matrix[1]}")
print(f"Printing The entire first Column: {matrix[:,0]}")
print(f"Printing The last two Columns: {matrix[:,1:]}")


"""Part 3 — Project Bridge
Create:
Python
project_bridge = np.zeros((4, 21, 3))
Then access:
 * frame 0
 * frame 0, keypoint 5
 * frame 0, keypoint 5, coordinate 2
 * frames 1–3
Print their shapes.
Don't worry about assigning real landmark coordinates yet. We're learning how to navigate the structure.
Tests / Assertions
Use simple assertions like yesterday.
Verify that:
Python
scores[0] == 10
scores[2] == 30
scores[-1] == 50
Verify the relevant shapes for your 2D and 3D selections.
"""
# project Bridge Questions and Answers
project_bridge = np.zeros((4, 21, 3))
frame_0 = project_bridge[0]
print(f"Shape of frame zero : {frame_0.shape}")
kp_5 = project_bridge[0, 5]
print(f"Shape of keypoint five : {kp_5.shape}")
crd_2 = project_bridge[0, 5, 2]
print(f"Shape of coordinate 2: {crd_2.shape}")
frame_1_3 = project_bridge[1:4]
print(f"Shape of frame 1-3: {frame_1_3.shape}")

assert frame_0.shape == (21, 3)
assert kp_5.shape == (3,)
assert frame_1_3.shape == (3, 21, 3)
print("All assertion Passed")

