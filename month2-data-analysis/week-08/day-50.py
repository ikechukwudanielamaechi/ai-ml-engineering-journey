#21st September 2026

"""Python Practice — Day 50 (First Real NumPy Exercise)

Create a 1D array (scores), a 2×3 matrix, and a Project Bridge-style 3D array (4 frames × 21 keypoints × 3 coordinates) using NumPy. Print and assert shape, ndim, size, and dtype for each.
Note: hand-verified every assertion — all correct, including size = 252 for the 3D array (4 × 21 × 3). Clean, well-structured first NumPy submission, with no indentation issues this time.
day50_numpy_arrays.py"""
import numpy as np

# Array 1: 1D Array (scores)
scores = np.array([10, 20, 30, 40, 50])

print("--- Array 1: scores ---")
print("Array:\n", scores)
print("Shape:", scores.shape)
print("Dimensions:", scores.ndim)
print("Size:", scores.size)
print("Data Type:", scores.dtype)
print()

# Array 2: 2D Matrix (2 x 3)
matrix = np.array([[10, 20, 30], [40, 50, 60]])

print("--- Array 2: matrix ---")
print("Array:\n", matrix)
print("Shape:", matrix.shape)
print("Dimensions:", matrix.ndim)
print("Size:", matrix.size)
print("Data Type:", matrix.dtype)
print()

# Array 3: Project Bridge (4 frames x 21 keypoints x 3 coordinates)
project_bridge = np.zeros((4, 21, 3))

print("--- Array 3: Project Bridge ---")
print("Shape:", project_bridge.shape)
print("Dimensions:", project_bridge.ndim)
print("Size:", project_bridge.size)
print("Data Type:", project_bridge.dtype)
print()

# Tests (Assertions)

# Array 1 asserts
assert scores.shape == (5,)
assert scores.ndim == 1
assert scores.size == 5

# Array 2 asserts
assert matrix.shape == (2, 3)
assert matrix.ndim == 2
assert matrix.size == 6

# Array 3 asserts
assert project_bridge.shape == (4, 21, 3)
assert project_bridge.ndim == 3
assert project_bridge.size == 252

print("All assertions passed successfully!")


