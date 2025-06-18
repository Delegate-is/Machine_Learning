print("Hello, World!")
a = 4 # Giving a value to a variable
b = 5 # Giving b a value
c = a + b # Adding a and b
print(c)
if c == 9:
    print(True)
else:
    print(False)
    
"""_Simple Python code to demontrate comments and basic variable assignnment.
    __summary__:
"""
print(2 + 3)
print(5 / 2)
print(4 ** 3)

print("How are you?") # This is a statement that prints a string
print(3+4); print(3-2) # This demostrates usage of separators in form of semicolons

"""Indentation is used to define blocks of code in Python
"""
def prime(num):
    if num > 1:
        for i in range(2, num// 2):
            if (num % i) == 0:
                print(num, "is not a prime number")
                break
            else:
                print(num, "is a prime number")
                break
    else:
        print(num, "is not a prime number")

num = int(input("Enter a number: "))  # You can change this value to test other numbers
prime(num)   

print("Hello, \n World!")

name = input("Enter your name: ")

age = int(input("Enter your age: "))

print(f"Hello, I am {name} and {age} years old")

# This is a comment in Python 2
# print "Hello, World!"  # This is a print statement
# This is a comment in Python 3
print("Hello, World!")  # This is a print function call