#Generate a 6 digit OTP using random module
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

import random
otp = random.randint(100000, 999999)
print("Your 6-digit OTP is:", otp)
