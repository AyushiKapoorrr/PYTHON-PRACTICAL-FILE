#Create a date in the format `YYYY-MM-dd`
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

from datetime import date
today = date.today()
formatted_date = today.strftime("%Y-%m-%d")
print("Date in YYYY-MM-dd format:", formatted_date)
