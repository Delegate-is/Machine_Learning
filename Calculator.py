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