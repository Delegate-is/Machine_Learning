# Nested if statement in Python
sent = input("Enter a sentence: ")
if not sent.endswith('.'):
    sent += '.'
    print(sent.upper())
    
num = 4
if(num%2==0):
    if(num%3==0):
        print("Number is divisible by both 2 and 3")
    else:
        print("Number is divisible by 2 but not by 3")
else:
    if(num%3==0):
        print("Number is divisible by 3 but not by 2")
    else:
        print("Number is not divisible by 2 or 3")

# Program to get name from user with 5 or <10 character and start with small letter
name = input("Enter your name: ")
# print(len(name))
if (len(name) == 5 or len(name) < 10):
    if(name.startswith('a')):
        print(f"Your name is {name}")
# Program get age and marks, select age >= 18 and marks >90 and <100
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))
if (age >= 18):
    if (marks > 90 and marks < 100):
        print(f"You are selected since your age is {age} with {marks} marks")
    else:
        print("marks issue")
else:
    print("Age issue")
    
age1 = int(input("Enter your age: "))
country = input("Enter your country: ")
if (age1 >= 18):
    if (country == "USA"):
        print(f"You are eligible to vote in the USA.")
    else:
        print("You are not eligible to vote in the USA.")
else:
    print("You are not eligible to vote")