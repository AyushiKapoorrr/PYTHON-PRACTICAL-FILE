#Create a package that contains two modules one for mathematical operations and the other for string operations. perform the following based on user choice:

print("----------------------------------------")
print("Name:Ayushi Kapoor")
print("Enrollment No:02417702024")
print("----------------------------------------")

#(a)adding two strings or numbers
#(b)multiplication of two strings or numbers
#(c)finding palindrome of a string or number
#(d)reversing a string or a number
#(e)Create a subpackage `combine`, it should have a submodule to combine the integers and strings into list or tuple or dictionary based on user choice.from mypackage.math_ops import *

# main.py
from mypackage import mathsop, stringop
from mypackage.combine import combiner

def main():
    print("Choose data type:")
    print("1. Numbers")
    print("2. Strings")
    data_type = input("Enter choice (1 or 2): ")

    if data_type == '1':
        a = int(input("Enter first number: "))
        b = int(input("Enter second number: "))
        print("Choose operation:")
        print("1. Add")
        print("2. Multiply")
        print("3. Palindrome check")
        print("4. Reverse")
        print("5. Combine")
        op = input("Enter choice: ")

        if op == '1':
            print("Result:", mathsop.add(a, b))
        elif op == '2':
            print("Result:", mathsop.multiply(a, b))
        elif op == '3':
            print("Palindrome?", mathsop.is_palindrome(a))
        elif op == '4':
            print("Reversed:", mathsop.reverse(a))
        elif op == '5':
            print("Combine as:")
            print("1. List  2. Tuple  3. Dict")
            choice = input("Enter choice: ")
            if choice == '1':
                print(combiner.combine_to_list(a, b))
            elif choice == '2':
                print(combiner.combine_to_tuple(a, b))
            elif choice == '3':
                print(combiner.combine_to_dict(a, b))

    elif data_type == '2':
        s1 = input("Enter first string: ")
        s2 = input("Enter second string: ")
        print("Choose operation:")
        print("1. Add (concatenate)")
        print("2. Multiply (repeat first string by length of second)")
        print("3. Palindrome check (first string)")
        print("4. Reverse (first string)")
        print("5. Combine")
        op = input("Enter choice: ")

        if op == '1':
            print("Result:", stringop.add_strings(s1, s2))
        elif op == '2':
            print("Result:", stringop.multiply_strings(s1, len(s2)))
        elif op == '3':
            print("Palindrome?", stringop.is_palindrome_string(s1))
        elif op == '4':
            print("Reversed:", stringop.reverse_string(s1))
        elif op == '5':
            print("Combine as:")
            print("1. List  2. Tuple  3. Dict")
            choice = input("Enter choice: ")
            if choice == '1':
                print(combiner.combine_to_list(s1, s2))
            elif choice == '2':
                print(combiner.combine_to_tuple(s1, s2))
            elif choice == '3':
                print(combiner.combine_to_dict(s1, s2))
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()
