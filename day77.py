# Differentiate between list and tuple
# a list is mutable whereas a tuple is immutable
# list is defined using [] whereas tuple is defined using ()
# list consumes more memory as compared to tuple
# Write the syntax of list comprehension.
list = [i for i in range(10)   if i%2==0]
print(list)
# Write a Python Program Get Two Set From User To Find Intersection Of That Set.
set1 = set()
set2 = set()
for i in range(3):
    set1.add(int(input("Enter element for set 1: ")))
for i in range(3):
    set2.add(int(input("Enter element for set 2: ")))
print("Intersection is: ", set1.intersection(set2))
#Write a Python Program Create a Dictionary From a List Which Display Length Of Each Word As Value.
list1 = [1,2,3,4,5]
dict1 = {i:i**2 for i in list1}
print(dict1)
# Write a Python program in which user able to modify any item of list
list2 = [1,2,3,4,5]
index = int(input("Enter index to modify: "))
value = int(input("Enter new value: "))
list2[index] = value
print(list2)