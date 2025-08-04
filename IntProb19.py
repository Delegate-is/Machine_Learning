# Nested list
list =[[1, 2, 3], [4, 5], [6, 7, 8, 9], ["Max", "Codeweb"], [True, False]]
print("Nested List:", list)  # Display the entire nested list
# Count the number of lists in a nested list
list_total = 0
for i in list:
    if type(i) == list:  # Using type to check if the element is a list
        list_total += 1
        print(f"Total number of lists in the nested list: {list_total}")  # Display the count of lists
# Display the entire nested list
print("Nested List:", list)  # Display the entire nested list
# Accessing elements in a nested list
print("First list:", list[0])  # Access the first list: [1, 2, 3]
print("First element of second list:", list[1][0])  # Access the first element of the second list
print("Second element of fourth list:", list[3][1])  # Access the second element of the fourth list: "Codeweb"
# Count the number of lists in a nested list
list_1 = [[1, 2, 3], [4, 5], [6, 7, 8, 9], ["Max", "Codeweb"], [True, False]]
list_total = 0
for i in list_1:
    if type(i) == list:  # Using type to check if the element is a list
        list_total += 1
print(f"Total number of lists in the nested list (alternative method): {list_total}")  # Display the count of lists
# Nested tuple
nested_tuple = ((1, 2, 3), (4, 5), (6, 7, 8, 9), ("Max", "Codeweb"), (True, False))
# Display the entire nested tuple
print("Nested Tuple:", nested_tuple)  # Display the entire nested tuple
# Accessing elements in a nested tuple
print("First tuple:", nested_tuple[0])  # Access the first tuple: (1, 2, 3)
print("First element of second tuple:", nested_tuple[1][0])  # Access the