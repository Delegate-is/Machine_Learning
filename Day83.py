# Python Exception and Exception Handling
# Exception -- error 
import math

name = input("Enter your name: ")
age = int(input("Enter your age: "))
try:
    print("name"+age)
except TypeError and ValueError:
    print("Type error and value error raised")

try:
    #print(3/0)
    lst = [2,3,4,52,4]
    print(list(9))
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except IndexError and TypeError:
    print("Exception of Index Error and Type Error is raised")
else:
    print("Division successful.")

a = 3 
try:
    print(a)
except:
    print("There is an exception")
else:
    print("Ther is no error because a is defined")
finally:
    print("Code is completed")
    
try:
    print(math.sqrt(-4))
except ValueError:
    print("There is a value error")