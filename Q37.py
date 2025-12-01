#Create a package `package-1` with modules `module-1` &amp; `module-2` both modules must contain a function to print the name of the module itself. Create a python file to run these two functions.
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

from package_1.module_1 import show_module_name as mod1
from package_1.module_2 import show_module_name as mod2

print("Running functions from modules inside package_1:\n")

mod1()
mod2()
