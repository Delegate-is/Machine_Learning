# Count no of lists in a nested list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9], ["Max", "Codeweb"],[True, False]]
list_total = 0
for i in nested_list:
    if type(i) == list:
        list_total += 1
print(f"Total number of lists in the nested list: {list_total}")  # Display the count of lists
# Alternative way to count lists in a nested list
for i in nested_list:
    # Using isinstance to check if the element is a list
    if isinstance(i, list):
        list_total += 1
print(f"Total number of lists in the nested list (alternative method): {list_total}")  # Display the count of lists
# How to access elements in a nested list
nested_list = [[1, 2, 3], [4, 5], [6, 7, 8, 9], ["Max", "Codeweb"], [True, False]]
# Accessing elements in a nested list
print(nested_list[0])  # Access the first list: [1, 2, 3]
print(nested_list[1][0])  # Access the first element of the second list
print(nested_list[3][1])  # Access the second element of the fourth list: "Codeweb"