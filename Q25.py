#Write a program to show the working of Pie Chart
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

import matplotlib.pyplot as plt
labels = ["Python", "Java", "C++", "JavaScript"]
sizes = [40, 25, 20, 15]
plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=90)
plt.title("Programming Language Popularity")
plt.show()
