# Constructor in Python
class MaxCode:
    def __init__(self):
        print("This is the constructor")
        self.name = "MaxJapu"
        
    def show(self):
        print(self.name)
        
obj = MaxCode()
obj.show()

# Non Parameterized and Parameterized Constructor in Python
# Non Parameterized === does not take any parameter
class Max:
    def __init__(self):
        self.a = 10
        self.b = 20
        print("This is a non parameterized constructor")
        
    def print_values(self):
        print(self.a+self.b)
obj = Max()
obj.print_values()

#Parameterized === does take a parameter
class MaxJapuu:
    def __init__(self, n1, n2):
        self.a = n1
        self.b = n2
        print("This is a parameterized constructor")
        
    def print_values(self):
        print(self.a+self.b)
        
obj = MaxJapuu(4,5)
obj.print_values()

# Default Constructor == takes no parameter
class Defaul:
    def __init__(self):
        self.name = "Maxxis"
        print("This is a default constructor")
        
    def print_M(self):
        print(self.name)
obj = Defaul()
obj.print_M()

# Destructor in Python OOP == call when project is destroyed/ ends
class Test:
    def __del__(self):
        print("Destructor.......")
        
    def __init__(self):
        print("Constructor is called......")
obj = Test()

#   Prob1_ parameterized constructor
class Arithmetic:
    def __init__(self, n3, n4):
        print("Parameterized Constructor is called......")
        self.num1 = n3
        self.num2 = n4
    def math_op(self):
        print("Addition = "+str(self.num1 + self.num2))
        print("Subtraction = "+str(self.num1 - self.num2))
        print("Division = "+str(self.num1 / self.num2))
        print("Multiplication = "+str(self.num1 * self.num2))
        print("Mod = "+str(self.num1 % self.num2))
        
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

obj = Arithmetic(a, b)
obj.math_op()

# Prob 2__ Detsructor== grabage collector, cleans memory, automatic
class Japu:
    def show(self):
         print("This is the show function of Japu")
         
    def __del__(self):
        print("This is the destructor...")
        
obj = Japu()
obj1 = Japu()
obj.show()

class Rectangle:
    def __init__(self, width, height):
        print("Parameterized Constructor is called......")
        self.width = width
        self.height = height
    def math_op(self):
        print("Area = "+str(self.width * self.height))
        print("Perimeter = "+str((self.width + self.height)*2))
        
obj = Rectangle(14, 12)
obj.math_op()

# find sequence of lowercase and uppercase

import re
user_string = input("Enter a string: ")
x = re.search('^[A-Z]+[a-z]+$', user_string)

if x:
    print("Matching....")
else:
    print("Not Matching....")
    
import re
user_string1 = input("Enter a string: ")
x2 = re.search('[A-Z]+$', user_string1)

if x2:
    print("Matching....")
else:
    print("Not Matching....")
    
import re
# ^ maens at start
# . means any char
# * 0 or many
# $ means at end
# \w means a-z, A-Z, 0-9 and _
user_string2 = input("Enter a string: ")
x4 = re.search('^m. *0$', user_string2)

if x4:
    print("Matching....")
else:
    print("Not Matching....")
    
    
import re

# take input from user
s = input("Enter a string: ")

# regex: starts with anything, has 'm' or 'M', then anything, and ends with 0 or 1
pattern = r".*[mM].*[01]$"

if re.search(pattern, s):
    print("Matching...")
else:
    print("Not Matching...")
