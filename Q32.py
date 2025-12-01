#Demonstrate the use of inheritance.
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show_details(self):
        print("Name:", self.name)
        print("Age:", self.age)
class Student(Person):
    def __init__(self, name, age, roll):
        super().__init__(name, age)  
        self.roll = roll
    def show_student(self):
        self.show_details()           
        print("Roll Number:", self.roll)

name = input("Enter name: ")
age = int(input("Enter age: "))
roll = input("Enter roll number: ")
s = Student(name, age, roll)
s.show_student()