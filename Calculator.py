from typing import Union

def add(a: float, b: float) -> float:
    return a + b

def subtract(a: float, b: float) -> float:
    return a - b

def multiply(a: float, b: float) -> float:
    return a * b

def divide(a: float, b: float) -> Union[float, str]:
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
list = [1,2,3,4,5,6]
list2 = [x**2 for x in list]
print(list)
print(list2)