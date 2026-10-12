
import numpy as np

# Create two matrices
A = np.array([[1, 2], [3, 4]])
B = np.array([[5, 6], [7, 8]])

print("Matrix A:")
print(A)

print("\nMatrix B:")
print(B)

# Matrix Addition
print("\nAddition:")
print(A + B)

# Matrix Subtraction
print("\nSubtraction:")
print(A - B)

# Matrix Multiplication
print("\nMultiplication:")
print(np.dot(A, B))

# Matrix Transpose
print("\nTranspose of Matrix A:")
print(A.T)

# Matrix Determinant
print("\nDeterminant of Matrix A:")
print(np.linalg.det(A))

