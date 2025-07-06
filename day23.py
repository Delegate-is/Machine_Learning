# Identity Operators in Python
print("Identity Operators in Python")
# Identity operators are used to compare the memory locations of two objects.
# They check whether two variables point to the same object in memory.
x = 10
y = 10
print(x is y)  # True, because both x and y point to the same object in memory
print(x is not y)  # False, because x and y point to the same object
print(id(x))  # Memory address of x
print(id(y))  # Memory address of y
print("x is y:", x is y)  # True
print("x is not y:", x is not y)  # False
a = 30 
b = 21
print("a is b:", a is b)  # False, because a and b point to different objects
print("a is not b:", a is not b)  # True, because a and b point to different objects
print("Memory address of a:", id(a))  # Memory address of a
print("Memory address of b:", id(b))  # Memory address of b

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1 is num2:
    print("num1 and num2 are the same object in memory.")
else:
    print(f"{num1} and {num2} are different objects in memory.")

list = [3, 2, 1]
if list[0] is list[1]:
    print("The first and second elements of the list are the same object in memory.")
elif list[1] is list[2]:
    print("The second and third elements of the list are the same object in memory.")
else:
    print("The first and second elements of the list are different objects in memory.")
print(id(list[0]))
print(id(list[1]))
print(id(list[2]))