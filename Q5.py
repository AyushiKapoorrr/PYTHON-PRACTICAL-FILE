#Write a program to print the sum of first n prime numbers.
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

n = int(input("Enter how many prime numbers to sum: "))

count = 0
num = 2       
total = 0     
while count < n:
    if is_prime(num):
        total += num
        count += 1
    num += 1
print("\nSum of first", n, "prime numbers is:", total)
