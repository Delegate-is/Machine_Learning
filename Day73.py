# Set Difference Method
A = {1, 2, 3, 4, 5}
B = {4, 5, 6, 7, 8}
print("Set A:", A)
print("Set B:", B)
difference = A - B
print("Difference (A - B):", difference)  # Output: {1, 2, 3}
difference = B - A
print("Difference (B - A):", difference)  # Output: {6, 7, 8}
# Symmetric Difference Method
symmetric_difference = A ^ B
print("Symmetric Difference (A ^ B):", symmetric_difference)  # Output: {1, 2, 3, 6, 7, 8}# Union Method
union_set = A | B
print("Union (A | B):", union_set)  # Output: {1, 2, 3, 4, 5, 6, 7, 8}
# Intersection Method
intersection_set = A & B
print("Intersection (A & B):", intersection_set)  # Output: {4, 5}
# Remove item from set
my_set  = {1,2,3,4,5,"pink","black"}
print(my_set)
print(type(my_set))
item = input("Enter item to remove in set: ")
my_set.discard(item)
print(my_set)
# get item from user to get two sets and perform subtraction
set1 = set()
set2 = set()
for i in range(5):
    num = int(input("Enter number to set1: "))
    set1.add(num)
for i in range(5):
    num = int(input("Enter number to set2: "))
    set2.add(num)
print(f"Set1: {set1}")
print(f"Set2: {set2}")
def set_subtraction(set1, set2):
    result = set1.difference(set2)
    print(f"Subtraction (Set1 - Set2): {result}")

set_subtraction(set1, set2)
# symetric diiference
def symmetric_difference(set1, set2):
    result = set1.symmetric_difference(set2)
    print(f"Symmetric Difference (Set1 ^ Set2): {result}")
symmetric_difference(set1, set2)
# Set Union -- will not take duplicated elements
def set_union(set1, set2, set3):
    result = set1.union(set2).union(set3)
    print(f"Union (Set1 | Set2 | Set3): {result}")
set1 = {1,2,3,4}
set2 = {3,4,5,6}
set3 = {5,6,7,8}
set_union(set1, set2, set3)
#Define a function named remove_duplicates that takes a list, input_list, as a parameter.
#Convert the list to a set to remove duplicates.
#Convert the set back to a list to preserve the original order of elements.
#Return the new list.
def remove_duplicates(input_list):
    # Convert the list to a set to remove duplicates
    unique_set = set(input_list)
    # Convert the set back to a list
    unique_list = list(unique_set)
    return unique_list
input_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(input_list)
print("List after removing duplicates:", result)