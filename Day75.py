# Set method add {} in python
set1 = set()
for i in range(5):
    set1.add(i)
print(f"Original set {set1}")
set1.add(5)
print(f"Updated Set {set1}")
# Set method clear
set1.clear()
print(f"Cleared Set {set1}")
# Set method copy
set1 = {1, 2, 3}
set2 = set1.copy()
print(f"Copied Set {set2}")
# Set method difference
set3 = {3, 4, 5}
diff = set1.difference(set3)
print(f"Difference between set1 and set3: {diff}")
# Set method difference_update
set1.difference_update(set3)
print(f"Set1 after difference_update with set3: {set1}")
# set method discard -- removes an element if present, does nothing if not present
set1.discard(2)
print(f"Set1 after discarding 2: {set1}")
# set method intersection
set1 = {1, 2, 3}
set3 = {2, 3, 4}
inter = set1.intersection(set3)
print(f"Intersection of set1 and set3: {inter}")
# set method isdisjoint -- all elements of both sets are different
set4 = {5, 6}
is_disjoint = set1.isdisjoint(set4)
print(f"Are set1 and set4 disjoint? {is_disjoint}")
# set method issubset -- all elements of set5 are present in set1
set5 = {1, 2}
is_subset = set5.issubset(set1)
print(f"Is set5 a subset of set1? {is_subset}")
# set method issuperset -- all elements of set1 are present in set5
is_superset = set1.issuperset(set5)
print(f"Is set1 a superset of set5? {is_superset}")
# set method pop -- removes and returns an arbitrary element from the set
popped_element = set1.pop()
print(f"Popped element: {popped_element}, Updated set1: {set1}")
# set method remove -- removes a specific element from the set and raises an error if not found
set1.remove(3)
print(f"Set1 after removing 3: {set1}")
# set method symmetric_difference -- elements in either set1 or set3 but not in both
set1 = {1, 2}
set3 = {2, 3}
sym_diff = set1.symmetric_difference(set3)
print(f"Symmetric difference between set1 and set3: {sym_diff}")
# set method update -- adds multiple elements to the set
set1.update([3, 4, 5])
print(f"Set1 after update: {set1}")
a = {"pink", "blue", "green"}
list1 = ["red", "yellow", "white"]
tple = ("black", "purple")
a.update(tple)
print(f"Set a after updating with tuple: {a}")
a.update(list1)
print(f"Set a after updating with list1: {a}")
dict1 = {"fruit": "apple", "vegetable": "carrot"}
a.update(dict1)
print(f"Set a after updating with dict1: {a}")
st = {"apple", "banana", "cherry"}
st.update("orange")
print(f"Set st after updating with string 'orange': {st}")

def common_characters(str1, str2):
    str1 = set(str1)
    str2 = set(str2)
    common_chars = str1.intersection(str2)
    return common_chars
# Example usage
string1 = input("Enter first string: ")
string2 = input("Enter second string: ")

result = common_characters(string1, string2)
print("Common characters:", result)
print(common_characters("hello", "world"))
print(common_characters("python", "java"))