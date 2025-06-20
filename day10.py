my_dict = {"name":"Max", "age":32, "Course":"Python", "School":"Udemy"}
print(my_dict["School"])
print(my_dict["age"])
print(my_dict)

# Set data type
my_set = {1,2,3,13,4,5,6}
set1 = {3,4,12,5,3,56,7}
print(my_set.intersection(set1))
print(my_set)
print(len(my_set))
print(min(my_set))

# Boolean Data Type in Python
a = ""
x = 0
y = []
print(bool(a))
print(bool(x))
print(bool(y))
b = "Hi"
c = {"name":"Faisal"}
print(bool(b))
print(bool(c))

# Binary Data Types
# Convert String to object
site_string = "Jafricode.com"
byte = bytes(site_string, 'utf-8')
print(byte)
# Convet int to object
num = 3
ans = bytes([num])
print(ans)
# Byte method have no parameter
# print(bytes())
# Working with iterable object
tple = (3,12,23,14,15)
print(bytes(tple))

site = "Maxcode.com"
byte = bytes(site, 'utf-16')
print(byte)
# Convert list to byte object that will be immutable you cannot modify
lst = [1,2,3,4]
byte1 = bytes(lst)
print(byte1)

# Bite Array- mutable
# String to array of bytes
str_site = "Maxcode.com"
arr1 = bytearray(str_site, 'utf-8')
arr2 = bytearray(str_site, 'utf-16')
m_view = memoryview(arr1)
print(list(m_view[0:]))
print(arr1)
print(arr2)
#Number to array of given size
size = 2
arr = bytearray(size)
print(arr)
size = 4
arr1 = bytearray(size)
print(arr1)

# Memoryview- safe way to expose the buffer protocol in Python
# byte_array = bytearray('Jafricode', 'utf-8')
# m_view = memoryview(byte_array)
# print(m_view[0])
# print(list(m_view[0:]))

# Create two sets named set1 and set2 containing integer values.
set1 = {}
set2 = {}
# Prompt the user to enter six numbers separated by space and store them in set1.
for i in range(6):
    num1 = int(input(f"Number {i+1} :" ))
    set1.add(num1)
# Prompt the user to enter six more numbers separated by space and store them in set2.
for i in range(6):
    num2 = int(input(f"Number {i+1} :"))
    set2.add(num2)
# Print both sets.
print(set1)
print(set2)
# The union of set1 and set2.
print(set1.union(set2))
# The intersection of set1 and set2.
print(set1.intersection(set2))
# The difference between set1 and set2.
print(set1.difference(set2))
# The symmetric difference between set1 and set2.
print(set1.symmetric_difference(set2))