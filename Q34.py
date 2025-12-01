#Write a program to read a binary file having employee data in the form of list and search for the record of a particular employee entered by user.
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

import pickle
with open("employees.dat", "rb") as f:
    emp_list = pickle.load(f)
search_id = int(input("Enter Employee ID to search: "))
found = False
for emp in emp_list:
    if emp["id"] == search_id:
        print("\nEmployee Record Found:")
        print("ID:", emp["id"])
        print("Name:", emp["name"])
        print("Department:", emp["dept"])
        found = True
        break
if not found:
    print("Employee not found in the file.")
