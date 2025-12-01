#Demonstrate the scope of variables, create a global variable and local variable to reflect the changes
print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

x = 10

def show_scope():
    x = 5
    print("Inside the function, local x =", x)

def change_global():
    global x 
    x = x + 20
    print("Inside the function after modifying global x =", x)
    
print("Initial global x =", x)
show_scope()         
print("Global x after calling show_scope() =", x)
change_global() 
print("Global x after calling change_global() =", x)
