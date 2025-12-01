#Perform the following operations on Dictionaries:
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

#(a)Create a dictionary from two lists.
keys = input("Enter list of keys: ").split()
values = input("Enter list of values: ").split()
d = {}
for i in range(len(keys)):
    d[keys[i]] = values[i]
print("Created dictionary:", d)

#(b)Update the value of an existing key.
d = eval(input("Enter a dictionary: "))
key = input("Enter key to update: ")
new_value = input("Enter new value: ")
if key in d:
    d[key] = new_value
    print("Updated dictionary:", d)
else:
    print("Key not found.")

#(c)Count occurrences of each character in a string using a dictionary.
s = input("Enter a string: ")
freq = {}
for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1
print("Character count:", freq)

#(d)Merge two dictionaries into one.
d1 = eval(input("Enter dictionary 1: "))
d2 = eval(input("Enter dictionary 2: "))
merged = d1.copy()
merged.update(d2)
print("Merged dictionary:", merged)

#(e)Find the key with the maximum value in a dictionary.
d = eval(input("Enter a dictionary: "))
max_key = max(d, key=d.get)
print("Key with maximum value:", max_key)

#(f)Remove a key from the dictionary safely without error.
d = eval(input("Enter a dictionary: "))
key = input("Enter key to remove: ")
removed = d.pop(key, "Key not found")
print("After removal:", d)

#(g)Check if a key exists in a dictionary.
d = eval(input("Enter a dictionary: "))
key = input("Enter key to search: ")
print("Key exists:", key in d)

#(h)Create a dictionary from a tuple.
t = eval(input("Enter an even-length tuple: "))
d = {}
for i in range(0, len(t), 2):
    d[t[i]] = t[i+1]
print("Created dictionary:", d)

#(i)Create a dictionary having 3 keys: name, age &amp; subject. Update the age byadding 2 years to the current age. Add a new key email to the existing dictionary.
d = {
    "name": input("Enter name: "),
    "age": int(input("Enter age: ")),
    "subject": input("Enter subject: ")
}
d["age"] = d["age"] + 2
d["email"] = input("Enter email: ")
print("Updated dictionary:", d)

#(j)Remove the data stored in email.
d = eval(input("Enter dictionary: "))
if "email" in d:
    del d["email"]
print("Dictionary after removing email:", d)

#(k)Remove the latest inserted item.
d = eval(input("Enter dictionary: "))
d.popitem()
print("After removing latest item:", d)

#(l)Delete the key age
d = eval(input("Enter dictionary: "))
if "age" in d:
    del d["age"]
print("After deleting age:", d)

#(m)Delete the entire dictionary.
d = eval(input("Enter dictionary: "))
d.clear()
print("Dictionary deleted:", d)
