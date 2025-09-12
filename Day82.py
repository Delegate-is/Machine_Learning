# get hours and convert to secs
hr = 14
sec = hr * 3600
print(sec)
# find area of triangle
b = 34
h = 45
area = (b * h) / 2
print("Area ="+ str(area))

# get dict and convert it to pandas series
import pandas as pd 
color_dict = {}
for i in range(3):
    code = input("Enter color code: ")
    color = input("Enter color value: ")
    color_dict[code] = color

ps = pd.Series(color_dict)
print(ps)


import pandas as pd
ps = pd.Series([1,2,3,4,5,6])
print(ps)
ps_up = pd.concat([ps, pd.Series([7,8,9])])
print(f"Ps Updated  = {ps_up}")

def reverse_string(input_string):
    return input_string[::-1]
print(reverse_string("Maxi254"))
# swap variable and display new value
num = input("Enter two numbers seperated by a space: ")
num1, num2 = map(float, num.split()) # 10 43
print(num1 + num2)
print(f"Value before swapping num1 = {num1}")
print(f"Value before swapping num2 = {num2}")
temp = num1 #10
num1 = num2 #43
num2 = temp #10
print(f"Value after swapping num1 = {num1}")
print(f"Value after swapping num2 = {num2}")


# Program to sort student name in ascending order
list = []
for  i in range(5):
    list.append(input(f"Enter a student name{i+1}: "))
    print(list)
list.sort()
print(f"Sorted list = {list}")
for i in list:
    if len(i) == 5:
        print(f"Student name  with 5 chars = {i}")
for i in list:
    if i.startswith('f') or i.startswith('F'):
        print("Has F as starting char")
    else:
        print(f"Student name  without f as starting chars = {i}")