#Write a program to show the working of Bar Graphs
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

import matplotlib.pyplot as plt
categories = ["A", "B", "C", "D", "E"]
values = [10, 24, 36, 18, 12]
plt.bar(categories, values)
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Graph Example")
plt.show()
