# Python Decision Making Structure
# if statement in python
a = 10
b = 20
if a < b:
    print("a is less than b")  # This will be printed since 10 is less than 20  
else:
    print("a is not less than b")
print(a is b)
marks = 87
if marks > 80:
    print("You have passed.....")
name = "John"
if name == "John":
    print("Hello John") 
print("\n")
# Progran to get no from user and display a message number is even : use if
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(f"The number, {number} is even.")
    
# Progran to get no from user and display a message number is odd : use if
number = int(input("Enter a number: "))
if number % 2 != 0:
    print(f"The number, {number} is odd.")
    

age = int(input("Enter your age: "))
if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")