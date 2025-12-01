#Send a list as argument such that it cant be modified by the calling function
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

def modify_list(lst):
    print("Inside function before modification:", lst)
    lst[0] = 999
    print("Inside function after modification:", lst)

original_list = [10, 20, 30, 40, 50]
print("Original list before calling function:", original_list)
modify_list(original_list.copy())
print("\nOriginal list after passing a copy:", original_list)

modify_list(tuple(original_list))

print("\nOriginal list after passing as tuple:", original_list)

