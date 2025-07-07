# Python Operators Precedence
print("PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction")
a = 2
b = 1
x = a + b * (3-1) /  2*a
print(f"x = {x}")  # Output: x = 4.0

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
# Calculate the average
y = num1 + num2 * num3
print(f"y = {y}")  # Output: y = num1 + num2 * num3
g = (num1-num2) + 3 * num3
print(f"g = {g}")  # Output: g = (num1 - num2) + 3 * num3

num4 = int(input("Enter fourth number: "))
z = (num3*num2) + num4**num1 #PEMDAS
print(f"z = {z}")  # Output: z = (num1 + num

print("PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction")
result = 10 + 5 * 2 - 3 / 3
print(f"Result = {result}")  # Output: Result = 19.0
# 10 + 5 * 2 - 3 / 3 = 10 + 10 - 1 = 19.0
num5 = int(input("Enter fifth number: "))
num6 = int(input("Enter sixth number: "))
e= num1-num4/(num2+num3)+num5*num6
print("e = " + str(e))  # Output: e = num1 - num4 / 9 * (num2 + num3) + num5 * num6
print("PEMDAS - Parentheses, Exponents, Multiplication/Division, Addition/Subtraction")
result2 = (num1 + num2) * (num3 - num4) / num5 + num6
print(f"Result2 = {result2}")  # Output: Result2 = (num1 + num2) * (num3 - num4) / num5 + num6

# How to check python version
# python --version
# Mention some advantages of Python
#Easy to read and write, large community support, extensive libraries, cross-platform compatibility, and dynamic typing.
# Write a python program to get 2 number from user to find their sum.
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
sum_result = n1 + n2
print(f"The sum of {n1} and {n2} is: {sum_result}")
# Write a python program to get 3 numbers from users to find their subtraction.
n3 = int(input("Enter first number: "))
sub_result = n3-n2-n1
print("The subtraction of num3, num2, and num1 is: " +str(sub_result))
# Identity operators in Python
a = [1, 2, 3]
b = a
c = a[:]
print(a is b)  # True, because b is the same object as a
print(a is c)  # False, because c is a copy of a
print(a == c)  # True, because c has the same content as a
