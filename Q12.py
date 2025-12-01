#Find Common Elements in Multiple Lists
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

n = int(input("Enter Number Of lists "))

all_lists = []
for i in range(n):
    lst = list(map(int, input(f"Enter elements of list {i+1}: ").split()))
    all_lists.append(lst)
common = set(all_lists[0])
for lst in all_lists[1:]:
    common = common.intersection(lst)

print("Common elements:", list(common))