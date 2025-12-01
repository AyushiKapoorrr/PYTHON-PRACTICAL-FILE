#Rotate a List by K positions
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

lst = list(map(int, input("Enter list elements: ").split()))
k = int(input("Enter K (number of rotations): "))
k = k % len(lst)
rotated = []
for i in range(len(lst) - k, len(lst)):
    rotated.append(lst[i])
for i in range(len(lst) - k):
    rotated.append(lst[i])
print("Rotated list:", rotated)