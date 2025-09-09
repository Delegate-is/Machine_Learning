def format_name(first_name, last_name):
    return f"Your first name is {first_name.upper()} and last name {last_name.lower()}"
print(format_name("Juma", "Kipkemoi"))
print(format_name("Alooo", "Kipkemoi"))
# Pandas program to perform basic operations on two pandas series and dataframe
import pandas as pd
import numpy as np
# create two series
s1 = pd.Series([1, 2, 3, 4, 5])
s2 = pd.Series([10, 20, 30, 40, 50])
# perform addition
print("Addition of two series:")
print(s1 + s2)
# perform subtraction
print("Subtraction of two series:")
print(s1 - s2)
# perform multiplication
print("Multiplication of two series:")
print(s1 * s2)
# perform division
print("Division of two series:")
print(s1 / s2)
# create two dataframes
df1 = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6]})
df2 = pd.DataFrame({'A': [10, 20, 30], 'B': [40, 50, 60]})
# perform addition
print("Addition of two dataframes:")
print(df1 + df2)

lst = []
for i in range(5):
    lst.append(int(input("Enter an item: ")))
print("List is: ", lst)
for i in lst:
    if i != lst[0] and i != lst[-1] and i % 5 == 0 and i % 7 != 0:
        print(i)

# Program to check char in sent even without spaces
sent = input("Enter a sentence")
total_char_with_space = len (sent)
print("Total char with space: ", total_char_with_space)
total_char_without_space = sum(not i.isspace() for i in sent)
print("Total char without space: ", total_char_without_space)
# display even and odd in a list
list1 = [1,2,3,4,5,6,7,8,9]
even = []
odd = []
for i in list1:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("Even: ", even)
print("Odd: ", odd)
list1 = [1,2,3,4,5,6,7,8,9]
e_n0 = [i for i in list1 if i %2==0]
print(e_n0)
# Create dict 
dict1 = {'a':1, 'b':2, 'c':3}
dict2 = {v:v**2 for v in dict1.values()}
print(dict2)
dict3 = {k:v for k,v in dict1.items() if v%2!=0}
print(dict3)
# find max and min in a list
list2 = [1,2,3,4,5]
print("Max is: ", str(max(list2)))
print("Min is: ", min(list2))
print("Product of max and min is: ", max(list2)*min(list2))
import math
print("Sqrt of product of max and min is: ", math.sqrt(max(list2)*min(list2)))
# Get computer memory in GB and convert it to bytes
import psutil
mem = psutil.virtual_memory()
print(f"Total memory in GB: {mem.total / (1024 ** 3):.2f} GB")
print(f"Total memory in Bytes: {mem.total} Bytes")
gb = 3.91
byte = 1073741824
req = gb * byte
print(f"{gb} GB is equal to {req} Bytes")

# Function to count vowels in a string
def count_vowels(input_string):
    vowels = 'aeiouAEIOU'
    count = 0
    for char in input_string:
        if char in vowels:
            count += 1
    return count
print(count_vowels("Hello World"))
print(count_vowels("aeiouAEIOU"))

lst = []
for i in range(5):
    lst.append(input("Enter an item: "))
print("List is: ", lst)
for i in lst:
    if i != lst[0] and i != lst[-1] and len(i) != 5:
        print(i)