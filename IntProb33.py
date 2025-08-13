# create an array of only zeros
import numpy as np
z = int(input("Enter a number: "))
ar = np.zeros(z)
print(ar)
num = input("Enter two numbers separated by space: ")
num1, num2 = map(float, num.split())
print(f"Sum = {num1+num2}")
print(f"difference : {num1-num2}")
print(f"product : {num1*num2}")

if num2 != 0:
    print(f"quotient: {num1/num2}")
else:
    print("not divided zero")