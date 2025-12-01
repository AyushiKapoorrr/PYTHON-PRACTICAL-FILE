#Using the anonymous function print the cube of a number
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

num = int(input("Enter a number: "))
cube = lambda x: x ** 3
print("Cube of", num, "is:", cube(num))