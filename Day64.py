# Prob 1: create 10 numbers and find addition and multiplication
numbers = (1, 2, 3, 4, 5, 6, 78, 9, 9, 45, 12)
add = 0
mul = 1
for i in numbers:
    add += i
    mul *= i
print("Addition:", add)
print("Multiplication:", mul)
for i in numbers:
    if i%2 ==0 and i%3 ==0:
        print(f"Numbers in tuple divisible by 2 and 3 are {i}")
# convert tuple into a string
str_tuple = str(numbers)
print(numbers)
print(type(numbers))
print(str_tuple)
print(type(str_tuple))
# Access specific items
item = int(input("Enter a element: "))
result = numbers.count(item)
print(str(result) + " times present")

fruits = ("Apple", "Orange", "Banana", "Mango", "Pineapple")
n = input("Enter name of fruit: ")
if n in fruits:
    print(f"{n} is present {fruits.count(n)} times")
else:
    print("Not Present")