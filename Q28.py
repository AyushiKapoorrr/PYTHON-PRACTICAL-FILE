#Write a program illustrating load() and dump() in binary file
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

import pickle

data = ["Apple", "Banana", "Mango", "Orange"]
with open("fruits.dat", "wb") as f:
    pickle.dump(data, f)
print("Data has been written to fruits.dat")
with open("fruits.dat", "rb") as f:
    loaded_data = pickle.load(f)

print("Data loaded from file:", loaded_data)