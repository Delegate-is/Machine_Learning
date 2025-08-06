# List - Mutable, ordered collection of items, works like array
list_example = [1, 2, 3, 4, 5]
print(list_example)  # Output: [1, 2, 3, 4, 5]
list_example.append(6)  # Add an item to the end of the list
print(list_example)  # Output: [1, 2, 3, 4, 5, 6]
list_example.remove(3)  # Remove an item from the list
print(list_example)  # Output: [1, 2, 4, 5, 6]
list_example.sort()  # Sort the list in ascending order
print(list_example)  # Output: [1, 2, 4, 5, 6]
list_example.reverse()  # Reverse the order of the list
print(list_example)  # Output: [6, 5, 4, 2, 1]
list_example.insert(2, 3)  # Insert an item at a specific index
print(list_example)  # Output: [6, 5, 3, 4, 2, 1]
list_example.pop()  # Remove the last item from the list
print(list_example)  # Output: [6, 5, 3, 4, 2]
for i in list_example:
    print(i)  # Output: 6, 5, 3, 4, 2 (each on a new line)
list_example[1]= "Max"  # Change the second item in the list
print(list_example)  # Output: [6, 'Max', 3, 4, 2]
list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]
list_combined = list_1 + list_2  # Combine two lists
print(list_combined)  # Output: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list_3 = list_1 * 2  # Repeat the first list
print(list_3)  # Output: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(3 in list_example)  # Check if an item is in the list, Output: True
print(len(list_example))  # Output: Length of the list, Output: 5
num = []
for i in range(3):
    num.append(input(f"Enter student name {i + 1}: "))
    i += 1
    print(num)
for i in num:
    print(i.upper())  # Output: Each student name on a new line
num_1 = []
for i in range(3):
    num_1.append(int(input(f"Enter student name {i + 1}: ")))
    i += 1
    print(num_1)
for i in num_1:
    if i % 2 == 0:
        print("Invalid")
    else:
        print(f"{i} is odd")
num_2 = []
for i in range(10):
    num_1.append(int(input(f"Enter number {i + 1}: ")))
    i += 1
    print(num_2)
# append number 11 to num_2
num_2.append(11)
print(num_2)  # Output: List with 11 appended
# Remove the fifth occurrence
num_2.remove(5)
print(num_2)  # Output: List with 5 removed