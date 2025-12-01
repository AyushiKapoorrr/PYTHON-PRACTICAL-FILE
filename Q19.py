#Write a program illustrating various functions of mathematical library in python.
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

import math

num = float(input("Enter a number: "))

print("\n--- Mathematical Functions Demo ---")

print("Square root:", math.sqrt(num))
print("Power (num^2):", math.pow(num, 2))
print("Ceiling value:", math.ceil(num))
print("Floor value:", math.floor(num))
print("Factorial (only for integers):", math.factorial(int(num)))
print("Sine value:", math.sin(num))
print("Cosine value:", math.cos(num))
print("Tangent value:", math.tan(num))
print("Log base e:", math.log(num))
print("Log base 10:", math.log10(num))
print("Absolute value:", math.fabs(num))
print("Exponential (e^num):", math.exp(num))
