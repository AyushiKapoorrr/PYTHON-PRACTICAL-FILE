#From the module import only two functions
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

from mymath import add, sub  
print("1. Addition")
print("2. Subtraction")
choice = int(input("Enter choice (1-2): "))
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
if choice == 1:
    print("Result:", add(a, b))
elif choice == 2:
    print("Result:", sub(a, b))
else:
    print("Invalid choice!")