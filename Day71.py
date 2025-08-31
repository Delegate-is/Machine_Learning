# Python SET== {unordered unindexable, no duplication, unchangeable, immutable, store unique elements}
# Set Example
set_example = {"red", "green", "red", False, 345, "yellow", "pink"}# no duplication
print(set_example)
print(type(set_example))
""" set is unchangeable
set["red"] = "blue"
print(set_example)
print(set_example[0]) ==unindexable
"""
# Set iteration and add symbol== cannot use + or *
for i in set_example:
    print(i)
# Creating empty set
st = set([12,343])# can only use mutable elements using this format
print(type(st))
print(st)

# Create a set and user able to insert new items
set_1 = {True, "Max", 23,4,5,56,6}
print(type(set_1))
print(set_1)
item = input("Enter new item to insert in set: ")
set_1.add(item)
print(set_1)

# Remove all items of a set
set_2 = set([23,344,5,43])
print(set_2)
#set_2.clear()
#print(set_2)
common_elements = set_1.intersection(set_2)
print(common_elements)

def common_elements(set1,set2):
    c = set1.intersection(set2)
    print(c)
set1 = {1,2,3,4}
set2 = {3,2,4}
common_elements(set1,set2)
def remove_duplicates(input_list):
    # Convert the list to a set to remove duplicates
    unique_set = set(input_list)
    # Convert the set back to a list
    unique_list = list(unique_set)
    return unique_list
input_list = [1, 2, 2, 3, 4, 4, 5]
result = remove_duplicates(input_list)
print("List after removing duplicates:", result)