#Using F-Strings print the date in Full Weekday, Abbreviated month and 4d year
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

from datetime import date
today = date.today()
day = today.strftime("%A")    
month = today.strftime("%b")    
year = today.strftime("%Y")     
print(f"Today is: {day}, {month} {year}")
