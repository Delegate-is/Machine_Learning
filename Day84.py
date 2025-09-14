import test
print("This is the file which I will use user create module")
test.func()
print(test.name)

# pip install -r requirements.txt

'''
Create a Python module named calculator.

Define functions for addition, subtraction, multiplication, and division within the calculator module.

Import the calculator module into another Python script and use the functions to perform arithmetic operations.
'''
import Calculator
a = 10
b = 5

# Perform operations
print("Addition:", Calculator.add(a, b))
print("Subtraction:", Calculator.subtract(a, b))
print("Multiplication:", Calculator.multiply(a, b))
print("Division:", Calculator.divide(a, b))