#Write a program to demonstrate the use of different operators in python.
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

m = int(input("Enter first number(m): "))
n = int(input("Enter second number(n): "))
#Arithmetic Operators
print("\n---Arithmetic Operators---")
print("Addition (m + n):", m + n)
print("Subtraction (m - n):", m - n)
print("Multiplication (m * n):", m * n)
print("Division (m / n):", m / n)
print("Floor Division (m // n):", m // n)
print("Modulus (m % n):", m % n)
print("Exponentiation (m ** n):", m ** n)
# Comparison Operators
print("\n---Comparison Operators---")
print("Equal to (m == n):", m == n)
print("Not equal to (m != n):", m != n)
print("Greater than (m > n):", m > n)
print("Less than (m < n):", m < n)
print("Greater than or equal to (m >= n):", m >= n)
print("Less than or equal to (m <= n):", m <= n)
# Logical Operators
print("\n---Logical Operators ---")
x = True
y = False
print("Logical AND (x and y):", x and y)
print("Logical OR (x or y):", x or y)
print("Logical NOT (not x):", not x)
# Assignment Operators
print("\n--- Assignment Operators ---")
a = m
print("Initial value of a:", a)
a += n
print("Add and assign (a += n):", a)
a -= n
print("Subtract and assign (a -= n):", a)
a *= n
print("Multiply and assign (a *= n):", a)
a /= n
print("Divide and assign (a /= n):", a)
# Bitwise Operators
print("\n--- Bitwise Operators ---")
print("Bitwise AND (m & n):", m & n)
print("Bitwise OR (m | n):", m | n)
print("Bitwise XOR (m ^ n):", m ^ n)
print("Bitwise NOT (~m):", ~m)
print("Bitwise Left Shift (m << 1):", m << 1)
print("Bitwise Right Shift (m >> 1):", m >> 1)