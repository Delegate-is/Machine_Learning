# Inheritance in Python OOP
# Process of creating a class from main class

class Test1:
    def test_method(self):
        print("This is the parent class")
        
class Test2(Test1):
    def test_func(self):
        print("This is the child class")
        
obj = Test2()
obj.test_method()
obj1 = Test1()
#obj1.test_func()
obj.test_func()

class A:
    id = 234
    def _show(self):
        print("ID: ",self.id)
class B(A):
    def ShowDetails(self):
        self._show()
        
obj = B()
obj.ShowDetails()
print(obj.id)

# Inheritance
class A:
    name = "Max"
    age = 243
    contact = 3456543
    
    def meth1(self, course):
        print(course)
        print("This is the method of Class A")

class B(A):
    city = "Paharpur"
    
    def meth2(self, a, b):
        print(a+b)
        print("This is the method of class B")
        
obj = B()
obj.meth1("Python")
obj.meth2(15, 20)


# Create class to find area of circle
class Radius:
    r = None
    
    def getRad(self):
        self.r = float(input("Enter radius of circle: "))
        
class FindArea(Radius):
    
    def show_area(self):
        circle_area = self.r *self.r * 3.14
        print(circle_area)
        
obj = FindArea()
obj.getRad()
obj.show_area()

class Animal:
    def make_sound(self):
        print("Animal makes a sound")
        
class Dog(Animal):
    def make_sound(self):
        print("Dog Barks")
        
obj = Dog()
obj.make_sound()

# Get string from user with start char as f and ending char as z
import re
s = input("Enter a string: ")

x = re.search('^f(z*)$' ,s)
if x:
    print("Matching....")
else:
    print("Not Matching....")
    
import re

s1 = input("Enter a string: ")

x1 = re.search(r"^f.*z$", s)
if x1:
    print("Matching....")
else:
    print("Not Matching....")


# program to get sent and char to check at last of sent
import re
sent = input("Enter a sentence: ")
char = input("Enter a char or set of char: ")

x3 = re.search(char+'$', sent)
if x3:
    print("Matching....")
else:
    print("Not Matching....")
x4 = re.search('^'+char, sent)
if x4:
    print("Matching....")
else:
    print("Not Matching....")