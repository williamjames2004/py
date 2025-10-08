import numpy as np

# Define two 3x3 matrices
A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

B = np.array([[9, 8, 7],
              [6, 5, 4],
              [3, 2, 1]])

# Scalar value
scalar = 2

# 1. Matrix Addition
addition = A + B
print("Matrix Addition:\n", addition)

# 2. Matrix Subtraction
subtraction = A - B
print("\nMatrix Subtraction:\n", subtraction)

# 3. Matrix Multiplication (dot product)
multiplication = np.dot(A, B)
print("\nMatrix Multiplication (dot product):\n", multiplication)

# 4. Scalar Multiplication
scalar_multiplication = scalar * A
print("\nScalar Multiplication (A * {}):\n".format(scalar), scalar_multiplication)

# 5. Scalar Division
scalar_division = A / scalar
print("\nScalar Division (A / {}):\n".format(scalar), scalar_division)
