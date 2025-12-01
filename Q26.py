#Write a python program to create Class and Object.
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

class Student:
    def __init__(self, name, enroll):
        self.name = name
        self.enroll = enroll
    def display(self):
        print("Student Name:", self.name)
        print("Enrollment No:", self.enroll)
name = input("Enter student name: ")
enroll = input("Enter enrollment number: ")
s1 = Student(name, enroll)
s1.display()
