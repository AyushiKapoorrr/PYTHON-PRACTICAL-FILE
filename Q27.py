#Write a Python program to copy the contents of a file to another file in a text file
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

src = input("Enter source file name: ")
dest = input("Enter destination file name: ")

with open(src, "r") as f1:
    content = f1.read()
with open(dest, "w") as f2:
    f2.write(content)
print("File copied successfully!")
