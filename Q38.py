#Create a subfolder `subpackage` in `package-1` create module `submodule` in thesub folder this should have a function to print the name of submodule
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

from package_1.module_1 import show_module_name as mod1
from package_1.module_2 import show_module_name as mod2
from package_1.subpackage.submodule import show_submodule_name as submod

print("Running functions from package_1 and its subpackage:\n")

mod1()
mod2()
submod()
