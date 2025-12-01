
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

#(a) Check if all elements of a tuple are numbers
t = eval(input("Enter a tuple: "))
all_numbers = True
for x in t:
    if not isinstance(x, (int, float)):
        all_numbers = False
        break
print("All elements are numbers:", all_numbers)

#(b)Swap two tuples without using a temporary variable.
t1 = eval(input("Enter first tuple: "))
t2 = eval(input("Enter second tuple: "))
t1, t2 = t2, t1
print("After swapping:")
print("Tuple 1:", t1)
print("Tuple 2:", t2)

#(c)Convert tuple of strings into a single string
t = eval(input("Enter a tuple of strings: "))
result = " ".join(t)
print("Single string:", result)

#(d)Find the maximum and minimum values in a tuple of numbers.
t = eval(input("Enter tuple of numbers: "))
print("Maximum:", max(t))
print("Minimum:", min(t))

#(e)Nested Tuple: Access the 3rd element of the 2nd tuple in t = (1, 2, (3, 4, 5), (6,7))
t = (1, 2, (3, 4, 5), (6, 7))
print("Required element:", t[2][1])

#(f)Create a tuple of n numbers and find out how many times, a particular number appears.
t = eval(input("Enter a tuple of numbers: "))
x = int(input("Enter number to count: "))
print("Occurrences:", t.count(x))

#(g)Create a tuple of unsorted values, and return a new sorted list.
t = eval(input("Enter an unsorted tuple: "))
sorted_list = sorted(t)
print("Sorted list:", sorted_list)

#(h)Create a heterogeneous tuple and find out the sum of all integer values.
t = eval(input("Enter a heterogeneous tuple: "))
total = 0
for x in t:
    if type(x) == int:
        total += x
print("Sum of integers:", total)

#(i)Create a tuple containing an employees record including Employee ID, Name, Designation, Project Assigned. Is the project assigned to this employee.
emp = eval(input("Enter employee record as tuple (ID, Name, Designation, Project): "))
project = input("Enter project name to check: ")
print("Project Assigned:", emp[3] == project)

#(j)Create a tuple on n numbers input by the user, copy only prime numbers in a new tuple and find out if its empty, print true if all the numbers are prime.
t = tuple(map(int, input("Enter numbers: ").split()))
prime_nums = []
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True
for x in t:
    if is_prime(x):
        prime_nums.append(x)
prime_tuple = tuple(prime_nums)
print("Prime number tuple:", prime_tuple)
print("Are all numbers prime?:", len(prime_tuple) == len(t))

#(k)Concatenate two tuples.
t1 = eval(input("Enter first tuple: "))
t2 = eval(input("Enter second tuple: "))
result = t1 + t2
print("Concatenated tuple:", result)

#(l)Repeat the elements of a tuple by 3 instances.
t = eval(input("Enter a tuple: "))
print("Repeated tuple:", t * 3)

#(m)From a tuple, create the atomic variables
t = eval(input("Enter a tuple: "))
print("Unpacked values:")
for i in range(len(t)):
    print(f"Element {i+1} =", t[i])

#(n)Find out the second largest no. from the tuple - no sorting.
t = eval(input("Enter tuple of numbers: "))
largest = max(t)
second = None
for x in t:
    if x != largest:
        if second is None or x > second:
            second = x

print("Second largest:", second)
