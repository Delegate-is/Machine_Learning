# Membership Operators in Python
# Membership operators are used to test if a value or variable is found in a sequence (such
# as strings, lists, tuples, sets, or dictionaries). The two membership operators in Python are:
# 1. `in`: Returns True if the value is found in the sequence.
# 2. `not in`: Returns True if the value is not found in the sequence
print("We are Learning Membership Operators in Python")
# Example of `in` operator
my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("3 is in the list")
else:
    print("3 is not in the list")
    
# Example of `not in` operator
my_string = "Hello, World!"
if "Python" not in my_string:
    print("Python is not in the string")
# Example with a dictionary
my_dict = {"name": "Alice", "age": 30}
if "name" in my_dict:
    print("Key 'name' is in the dictionary")

lst = [1,2,3,4,5,7,8,9,10]
tp = (1,3,45,3,6,7,8,9)
print(3 in lst)  # Output: True
print(6 not in tp)  # Output: True
print(10 in lst)  # Output: True
print(11 not in tp)  # Output: True
# Example with a set
my_set = {1, 2, 3, 4, 5}
if 6 not in my_set:
    print("6 is not in the set")

# Write program to check occurence of a specific color in a list
colors = ["red", "blue", "green", "yellow", "blue"]
color_name = input("Enter a color to check its occurrence: ")
if color_name in colors:
    count = colors.count(color_name)
    print(f"{color_name} occurs {count} times in the list.")
else:
    print(f"{color_name} is not in the list.")

my_list = [1,2,3,4,5]
num = int(input("Enter a number to check if it's in the list: "))
if num in my_list:
    print(f"{num} is in the list.")
else:
    print(f"{num} is not in the list.")

# Create a tuple and check if a name is in the tuple
names_tuple = ("Alice", "Bob", "Charlie", "David")
name_to_check = input("Enter a name to check if it's in the tuple: ")
if name_to_check in names_tuple:
    print(f"{name_to_check} is in the tuple.")
else:
    print(f"{name_to_check} is not in the tuple.")
    