def factorial(n):
    """Return the factorial of a non-negative integer n using recursion."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

print(factorial(5))  # Output: 120


# Get starting no and ending no to display seq

i = int(input("Enter starting number: "))
e = int(input("Enter ending number: "))

if i > e:
    print("Start no should be less than end no")
else:
    for i in range(i, e+1):
        print(i)
# search student name in tuple
tup = ("Joante", "Max", "Ali", "Delegate")
std = input("Enter student name: ")
if std in tup:
    print("Student "+std+" is existing")
else:
    print("Not Found")

# two lists
even_list = [i for i in range(1, 101) if i%2 == 0]
print(even_list)
odd_list = [i for i in range(1, 101) if i%2 != 0]
print(odd_list)
even_sum = 0
for i in even_list:
    even_sum += i
print(even_sum)
odd_sum = 0
for i in even_list:
    odd_sum += i
print(odd_sum)
even_product = 1
for i in even_list:
    even_product *= i
print(even_product)
odd_product = 1
for i in even_list:
    odd_sum *= i
print(odd_product)

# find sum and average of digits in a string
st = input("Enter a string: ")
print("You Entered = "+st)
num_list = []
sum = 0
for i in st:
    if i.isdigit():
        int_i = int(i)
        sum += int_i
        num_list.append(int_i)
        
total_of_digits = len(num_list)
print(total_of_digits)
print("Total number sum = "+str(sum))
ave = sum / total_of_digits
print("Average of number = "+str(ave))
print(num_list)

import math

# Program to find angle sin and cos value in radian
angle = float(input("Enter an angle: "))
sin_value = math.sin(angle)
cos_value = math.cos(angle)
print("You entered = "+str(angle))
print("SIN VALUE = "+str(sin_value)+ " rad")
print("COS VALUE = "+str(cos_value)+" rad")