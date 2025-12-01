#Perform the following operations on list:
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")
# a. Combine two user input lists and remove duplicates
list1 = list(map(int, input("Enter elements of list 1 : ").split()))
list2 = list(map(int, input("Enter elements of list 2 : ").split()))
combined = list1 + list2
result = []
for x in combined:
    if x not in result:
        result.append(x)
print("Combined list without duplicates:", result)
# b. Find the second largest number
numbers = list(map(int, input("Enter new list: ").split()))
unique_nums = list(set(numbers))
if len(unique_nums) < 2:
    print("Second largest does not exist (not enough unique numbers).")
else:
    unique_nums.remove(max(unique_nums))
    second_largest = max(unique_nums)
    print("Second largest number:", second_largest)
# c. Reverse a list without slicing
lst = list(map(int, input("Enter new list: ").split()))
rev = []
for i in range(len(lst)-1, -1, -1):
    rev.append(lst[i])
print("Reversed list:", rev)
# d. Linear search
lst = list(map(int, input("Enter list elements : ").split()))
key = int(input("Enter number to search: "))
found = False
for x in lst:
    if x == key:
        found = True
        break
if found:
    print("Number found in the list.")
else:
    print("Number not found.")
# e & f. Flatten a nested list entered by user
import ast
nested = ast.literal_eval(input("Enter a nested list: "))
flat = []
def flatten(lst):
    for item in lst:
        if type(item) == list:
            flatten(item)
        else:
            flat.append(item)
flatten(nested)
print("Flattened list:", flat)
