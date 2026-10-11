#24th September 2026

"""Python Practice — Day 53 (NumPy Broadcasting)

Part 1: scores (3×3) + offset. Part 2: landmarks + offset, with shape assertion plus at least three more useful assertions. Part 3: compare compatible vs. incompatible shapes with np.zeros().
Two things to note — see grading notes in the reply: Part 2's landmarks array has 3 rows instead of the 4 specified in the instructions, and only 1 assertion is present where at least 4 were required (1 shape check + 3 more).
day53_numpy_broadcasting.py"""
import numpy as np

# Basic Broadcasting
scores = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
offset = np.array([1, 2, 3])

result = scores + offset
print(f"Scores: \n{scores}\n")
print(f"Offset: \n{offset}\n")
print(f"Result: \n{result}\n")
print(f"Scores Shape: {scores.shape}")
print(f"Offset Shape: {offset.shape}")
print(f"Result Shape: {result.shape}")

# Part 2 - Broadcasting with project bridge
landmarks = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [100, 110, 120]
])

offset = np.array([5, 10, 2])
shifted = landmarks + offset
print(f"\nShifted : {shifted}")

assert shifted.shape == landmarks.shape
print("**Assertion Completion**")

# Part 3 -- Compare compatible shapes

A = np.zeros((4, 3))
B = np.array([1, 2, 3])
C = A + B
print(f"\n{C}")

try:
    incompatible = np.array([2, 1])
    check_compatibility = A + incompatible
    print(check_compatibility)
except ValueError:
    print("\nCould not Broadcast")


