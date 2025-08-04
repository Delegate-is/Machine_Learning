# Access multiple elements in a nested list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9], ["Max", "Codeweb"], [True, False]]
# Accessing elements in a nested list
print(nested_list[0])  # Access the first list: [1, 2, 3]
print(nested_list[1][0])  # Access the first element of the second list
list = [1, 2, 3, 4, 5]
print(list)
s = int(input("Enter a starting item position: "))
e = int(input("Enter ending item position: "))# Input starting position
print(f"Starting item position: {s}")  # Display the starting position
ending = e+1
print(list[s:ending])  # Display the range of items
# Acessing multiple elements from a tuple
nested_tuple = ((1, 2, 3), (4, 5), (6, 7, 8, 9), ("Max", "Codeweb"), (True, False))
print(nested_tuple[0])  # Access the first tuple: (1, 2, 3)
print(nested_tuple[1][0])  # Access the first element of the second tuple
tuple = (1, 2, 3, 4, 5)
print(tuple)
print(tuple[s:e])  # Display the range of items from the tuple