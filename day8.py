# List is mutable
list = [1, 2, 3, 4, 5]
print(list [2])
list [2] = 10
print(list)
# Tuple is immutable
tuple = (1, 2, 3, 4, 5)
print(tuple[2])
#tuple [2] = 10 # This will raise an error
print(tuple)
#String is immutable
name = "Max Dooh"
print(name[0])
#name[0] = N # This will raise an error
print(name)

"""Sequence and Non-Sequence Types in Python"""
# List is a sequence type
list_colors = ["red", "green", "yellow", "black", "white", "pink", "grey"]
print(list_colors [-1])
# Tuple is a sequence type
tuple_colors = ("red", "green", "yellow", "black", "white", "pink", "grey")
print(tuple_colors [2])
# String is a sequence type
name = "Python Programming language"
print(name[9])
#Dictionary is a non-sequence type
dict_colors = {
    "red": "#FF0000",
    "green": "#00FFOO",
}
print(dict_colors["red"])
# Set is a non-sequence type
set_colors = {"red", "green", "yellow", "black", "white", "pink", "grey"}
# print(set_colors [1])
print("red" in set_colors) #Check if "red" is in the set

list = [1,2,3,4,5]
tuple=(1,2,3,4,5)
print(list)
print(tuple)
list[-1]=10
print(list[-1])
#tuple[1] = 2 # Raises an error
print(tuple) 
#List is mutable while tuple is immutable

# Sequence Example (List)
my_list = [1, 2, 3]
print(my_list[0])  # Accessing elements by index
# Output: 1
 
# Non-Sequence Example (Dictionary)
my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict['a'])  # Accessing elements by key
# Output: 1