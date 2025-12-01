#Split a List into Chunks of Size N
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

lst = list(map(int, input("Enter list elements: ").split()))
n = int(input("Enter chunk size N: "))
chunks = []
for i in range(0, len(lst), n):
    chunks.append(lst[i:i+n])

print("List in chunks:", chunks)