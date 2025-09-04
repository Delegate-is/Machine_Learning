# Set Intersection
set1 = set()
set2 = set()
for i in range(3):
    set1.add(input(f"Enter element {i+1} for set1: "))
    set2.add(input(f"Enter element {i+1} for set2: "))
print(f"Set1: {set1}")
print(f"Set2: {set2}")
print(f"Intersection of Set1 and Set2: {set1.intersection(set2)}")
# Checking subset
is_subset = set1.issubset(set2)
print(f"Is Set1 a subset of Set2? {is_subset}")
item = input("Enter an element to remove from Set1: ")
set1.remove(item)
print(f"Set1 after removing {item}: {set1}")
set1.add(item)
print(f"Set1 after adding {item} back: {set1}")
list2 = []
for i in range(5):
    list2.append(input(f"Enter element {i+1} for list2: "))
print(f"List2: {list2}")
set6 = set(list2)
for i in set6:
    print(str(i)+" " + " having size of " + str(len(str(i))) +" "+" characters")
    
def unique_characters(input_string):
    return set(input_string)
input_string = input("Enter a string: ")
print(f"Unique characters in the string: {unique_characters(input_string)}")