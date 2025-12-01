#Write a python program to insert data into CSV file and display it.
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

import csv
filename = "students.csv"
n = int(input("How many records do you want to insert? "))
with open(filename, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Age", "City"])
    for i in range(n):
        print(f"\nRecord {i+1}")
        name = input("Enter name: ")
        age = input("Enter age: ")
        city = input("Enter city: ")
        writer.writerow([name, age, city])

print("\nData inserted successfully into students.csv\n")
print("Displaying CSV file contents:\n")
with open(filename, "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)