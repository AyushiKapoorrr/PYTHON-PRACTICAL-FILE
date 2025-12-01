#Create a module that performs all arithmetic operations and wap to demonstrate the functioning of the module based on user choice.
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

import mymath   

print("Arithmetic Operations")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Modulus")
print("6. Power")

choice = int(input("Enter your choice (1-6): "))

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

if choice == 1:
    print("Result:", mymath.add(a, b))
elif choice == 2:
    print("Result:", mymath.sub(a, b))
elif choice == 3:
    print("Result:", mymath.mul(a, b))
elif choice == 4:
    print("Result:", mymath.div(a, b))
elif choice == 5:
    print("Result:", mymath.mod(a, b))
elif choice == 6:
    print("Result:", mymath.power(a, b))
else:
    print("Invalid choice!")
