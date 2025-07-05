print("We are Learning Logical Operators in Python")
Logical_Operators = True
if Logical_Operators:
    print("Logical Operators are used to combine conditional statements.")
    print("They return True or False based on the conditions.")
    
    # Example of AND operator
    a = True
    b = False
    print(f"a and b: {a and b}")  # Output: False
    
    # Example of OR operator
    print(f"a or b: {a or b}")  # Output: True
    
    # Example of NOT operator
    print(f"not a: {not a}")  # Output: False
    
c = 10
d = 20
e = 14
f = 17
print(c>d and e<f)  # Output: False
print(c>d or e<f)   # Output: True
print(not(c<d))     # Output: False
print(not(c>d))     # Output: True
# false and true gives false
# true or false gives true
# not true gives false
# false and false gives false
# true or true gives true
# not false gives true

"""Program checking valid username and password
    The program checks if the username and password match the predefined values.
"""
User_Name = "admin"
Password = "1234"
input_username = input("Enter your username: ")
input_password = input("Enter your password: ")
if input_username == User_Name or input_password == Password:
    print("Login successful!")
else:
    print("Invalid username or password. Please try again.")
# Program to check if a number is even or odd
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"{number} is an even number.")
else:
    print(f"{number} is an odd number.")

# Program to check if a number is positive, negative, or zero
number = float(input("Enter a number: "))
if number > 0:
    print(f"{number} is a positive number.")
elif number < 0:
    print(f"{number} is a negative number.")    
else:
    print("The number is zero.")
# Program to check if a character is a vowel or consonant
char = input("Enter a character: ").lower()
if char in 'aeiou':
    print(f"{char} is a vowel.")
else:
    print(f"{char} is a consonant.")
# Program to check if a year is a leap year
year = int(input("Enter a year: "))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

usn = input("Enter your USN: ")
if usn.startswith("1") and len(usn) == 10:
    print("Valid USN")
else:
    print("Invalid USN. It should start with '1' and be 10 characters long.")

# Create two boolean variables x and y with values True and False respectively.
x = True
y = False
# Logical AND: Perform a logical AND operation between x and y and store the result in a variable named and_result.
print("x & y:", x and y)
and_result = x and y
# Logical OR: Perform a logical OR operation between x and y and store the result in a variable named or_result.
or_result = x or y 
print("x | y:", x or y) 
# Logical NOT: Perform a logical NOT operation on x and store the result in a variable named not_x.
not_x = not x
print("not x:", not x)
# Logical NOT: Perform a logical NOT operation on y and store the result in a variable named not_y.
not_y = not y
print("not y:", not y)
# Print the results of the logical operations.
print(f"Logical AND result (x and y): {and_result}")
print(f"Logical OR result (x or y): {or_result}")
# Print the results of the logical NOT operations.
print(f"Logical NOT result (not x): {not_x}")
print(f"Logical NOT result (not y): {not_y}")

User_Name1 = "maxi"
Password1 = "12345"
name2 = input("Enter your username: ")
password2 = input("Enter your password: ")
if name2 == User_Name1 and password2 == Password1:
    print("Your username and password are correct.")
else:
    print("Your username and password are incorrect. Please try again.")