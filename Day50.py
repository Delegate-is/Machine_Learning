# Python Number Data Type - int(whole, +, -), float(fraction,pointing, e power), complex
# int
a = 10  # whole number
print(type(a))  # Display the type of a
b = -20  # negative whole number
print(f"Integer a: {a}, Integer b: {b}")
# float
c = 10.5  # positive float number
print(type(c))  # Display the type of c
d = -20.75  # negative float number
print(f"Float c: {c}, Float d: {d}")
# complex
e = 3 + 4j  # complex number with real and imaginary parts
f = 5 - 2j  # another complex number
print(type(e))  # Display the type of e
print(f"Complex e: {e}, Complex f: {f}")
# Convert One data type to another
# Convert int to float
int_to_float = float(a)  # Convert integer a to float
print(f"Converted int to float: {int_to_float}")  # Display the converted value
# Convert float to int
float_to_int = int(c)  # Convert float c to integer
print(f"Converted float to int: {float_to_int}")  # Display the converted value
# Convert complex to float (only real part)
complex_to_float = float(e.real)  # Convert the real part of complex e to float
print(f"Converted complex to float (real part): {complex_to_float}")  # Display the converted value
# Convert int to complex
int_to_complex = complex(a)  # Convert integer a to complex
print(f"Converted int to complex: {int_to_complex}")  # Display the converted value
# Convert float to complex
float_to_complex = complex(c)  # Convert float c to complex
print(f"Converted float to complex: {float_to_complex}")  # Display the converted value
# Convert complex to int (only real part)
complex_to_int = int(e.real)  # Convert the real part of complex e to integer
print(f"Converted complex to int (real part): {complex_to_int}")  # Display the converted value
"""i = 10 + 20j
print(type(i))  # Display the type of i
new_i = float(i)  # Convert i to complex type
print(type(new_i))  # Display the type of new_i"""
num = input("Enter two numbers separated by space: ")  # Input two numbers
num1, num2 = map(float, num.split())  # Split input and convert to float
print(f"Input numbers: {num1}, {num2}")  # Display the input 
print(f"Sum: {num1 + num2}")  # Display the sum of the numbers
print(f"Difference: {num1 - num2}")  # Display the difference of the numbers
print(f"Product: {num1 * num2}")  # Display the product of the numbers
print(f"Quotient: {num1 / num2}")  # Display the quotient