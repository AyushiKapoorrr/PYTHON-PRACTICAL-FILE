#Write a python program to create a Numpy array and perform the basic matrix operation.
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")


import numpy as np
print("Enter elements for Matrix A (space separated):")
A = np.array(list(map(int, input().split())))
rowsA = int(input("Enter number of rows in Matrix A: "))
A = A.reshape(rowsA, -1)

print("\nEnter elements for Matrix B (space separated):")
B = np.array(list(map(int, input().split())))
rowsB = int(input("Enter number of rows in Matrix B: "))
B = B.reshape(rowsB, -1)

print("\nMatrix A:\n", A)
print("\nMatrix B:\n", B)
print("\nBasic Matrix Operations")
try:
    print("\nA + B:\n", A + B)
except:
    print("\nA + B: Not possible (dimension mismatch)")

try:
    print("\nA - B:\n", A - B)
except:
    print("\nA - B: Not possible (dimension mismatch)")

try:
    print("\nA × B:\n", np.matmul(A, B))
except:
    print("\nA × B: Not possible (dimension mismatch)")

print("\nTranspose of A:\n", A.T)
print("\nTranspose of B:\n", B.T)

if A.shape[0] == A.shape[1]:
    print("\nDeterminant of A:", np.linalg.det(A))
else:
    print("\nDeterminant of A: Not possible (A is not square)")

if B.shape[0] == B.shape[1]:
    print("\nDeterminant of B:", np.linalg.det(B))
else:
    print("\nDeterminant of B: Not possible (B is not square)")
