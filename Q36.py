#Write a program to perform Transpose using NumPy.
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

import numpy as np
matrix = np.array([[1, 2, 3],
                   [4, 5, 6]])
print("Original Matrix:")
print(matrix)
transpose_matrix = np.transpose(matrix)
print("\nTranspose of the Matrix:")
print(transpose_matrix)
