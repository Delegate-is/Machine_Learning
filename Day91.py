# Pandas program to get subset from existing series
import pandas as pd

s = pd.Series([1,2,3,4,5,6,6,554,6,7])
print(s)

n = 4
new_s = s[s < n]
print(new_s)

import pandas as pd
# Create a sample series
data = pd.Series([10, 20, 30, 40, 50, 60, 70])
print("Original Series:")
print(data)
# Get a subset (say elements from index 2 to 5)
subset = data[2:6]
print("\nSubset of the Series (index 2 to 5):")
print(subset)


import math
class Circle:
    def __init__(self, radius, color):
        self.radius = radius
        self.color = color

    def area(self):
        area = math.pi * (self.radius ** 2)
        print(f"Area = {area}")

    def display(self):
        print(f"Circle with radius: {self.radius}")
        print(f"Color: {self.color}")
        
obj = Circle(35, "Blue")
obj.area()
obj.display()

# Class functionality in Python
class Test:
    a = 10
    b = 30
    
    def mytest(self):
        print("This is the fuction,,,, ")
    mytest(a)
    
    def show(self):
        print(f"A = {self.a}")
        print(f"B = {self.b}")

# create object to access class
obj = Test()
obj.show()
print(obj.a)

class Calculation():
    n_1 = None
    n_2 = None
    lst = [1,2,3,5678,5677654.343]
    
    def create_list(self):
        self.list =[]
        for i in range(5):
            self.list.append(int(input(f"Enter number {i+1} ")))
            print(self.list)
        
    def getData(self):
        self.n_1 = int(input("Enter a number: "))
        self.n_2 = int(input("Enter a number: "))
        
    def showResult(self):
        print("Addition = "+str(self.n_1+self.n_2))
        print("Subtraction = "+str(self.n_1-self.n_2))
        print("Division = "+str(self.n_1/self.n_2))
        print("Multiplication = "+str(self.n_1*self.n_2))
        print("Mod = "+str(self.n_1%self.n_2))
        
    def Max_num(self):
        print(max(self.n_1, self.n_2))
        print(f"Max Num = {max(self.lst)}")
    
# Object is class name 
obj = Calculation()
obj.getData()
obj.showResult()
obj.Max_num()
obj.create_list()

# Web App to add login functionality in Django
# Web App to register user in Django