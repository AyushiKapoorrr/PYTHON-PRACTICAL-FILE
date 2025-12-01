#Write a Python program that takes a text file as input and returns the number of words of a given text file.
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

filename = input("Enter file name: ")
try:
    with open(filename, "r") as f:
        content = f.read()
        words = content.split() 
        print("Number of words in the file:", len(words))

except FileNotFoundError:
    print("File not found! Please check the file name.")
