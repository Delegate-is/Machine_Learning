# Get length of all keys in dictionary and add them in 1 variable
dict = {"col1": "Red", "col1": "Red", "col2": "Yellow", "col3": "Black","col4": "Blue","col5": "Green"}
print(dict)
a = 0
for i in dict.keys():
    a += len(i)
print(a)
# Get total length of all values of a dictionary with string values
my_dict = {'key1': 'apple', 'key2': 'banana', 'key3': 'orange'}
total_length = 0
for value in my_dict.values():
    total_length += len(value)
print(total_length)