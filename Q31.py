#Write a program to perform Linear Search
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")


lst = list(map(int, input("Enter list elements: ").split()))
key = int(input("Enter number to search: "))
found = False
for i in range(len(lst)):
    if lst[i] == key:
        print(f"Element found at index {i}")
        found = True
        break
if not found:
    print("Element not found in the list.")