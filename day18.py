a = 10
b = 10
c = 3
d = 5
print(a==b)
print(c!=d)
print(a<=b)
print(c>=d)
username = "shsgdtegdj"
print(username == "shsgdtegdj")
print("\n")
# Program Exercise 1
n1 = int(input("Enter 1st Number: "))
n2 = int(input("Enter Second Number: "))
print(max(n1, n2))
if(n1 == n2):
    print("Both are eqaul")
else:
    print("Not equal")
    
e = int(input("Enter 1st Number: "))
f = int(input("Enter Second Number: "))
if(e > f):
    print(e)
else:
    print(f)
print("\n")
# Create two variables num1 and num2 with values 10 and 5 respectively.
num1=10
num2=5
# Greater Than: Check if num1 is greater than num2 and store the result in a variable named greater_than.
greater_than = num1>num2
print(f"Num1 Greater Than Num2: {greater_than}")
#Less Than: Check if num1 is less than num2 and store the result in a variable named less_than.
less_than = num1<num2
print(f"Num1 Less Than Num2: {less_than}")
#Equal To: Check if num1 is equal to num2 and store the result in a variable named equal_to.
equal_to = num1==num2
print(f"Num1 Equal To Num2: {equal_to}")
#Not Equal To: Check if num1 is not equal to num2 and store the result in a variable named not_equal_to.
not_equal_to = num1!=num2
print(f"Num1 Not Equal To Num2: {not_equal_to}")
#Greater Than or Equal To: Check if num1 is greater than or equal to num2 and store the result in a variable named greater_than_equal_to.
greater_than_equal_to = num1>=num2
print(f"Num1 Greater Than Equal To Num2: {greater_than_equal_to}")
#Less Than or Equal To: Check if num1 is less than or equal to num2 and store the result in a variable named less_than_equal_to.
less_than_equal_to = num1<=num2
print(f"Num1 Less Than Equal To Num2: {less_than_equal_to}")

"""
What is List?
--it is a sequence data type in which different data type elements reside.
What is mutable and Immutable Data Type in Python?
--mutable types are like lists in which elements may be changed after creation
while immutable are like tuples where elements cannot be changed after creation.
What means of Logical Operator?
--logical operators are symbols or keywords that are used to combine or modify conditional 
statements (Boolean expressions) and return a Boolean result (True or False)."""
# Write a Python Program to create a dictionary.
dict = {"name": "Max", "school": "Udemy", "course": "Python", "country": "Kenya"}
print(dict["name"])