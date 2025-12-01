#Based on the marks of a student grade them as:
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")
marks = int(input("Enter the marks of the student: "))
if marks >= 90:
    grade = "A+"
elif marks >= 75:
    grade = "A"
elif marks >= 60:
    grade = "B"
elif marks >= 50:
    grade = "C"
else:
    grade = "F"

print("Marks Obtained:", marks)
print("Grade Awarded:", grade)
