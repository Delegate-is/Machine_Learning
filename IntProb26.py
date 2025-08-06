# Get dict keys and values into two lists, one with keys other values
my_dict = {'key1': 'apple', 'key2': 'banana', 'key3': 'orange'}
print(my_dict)
key = []
for i in my_dict.keys():
    key.append(i)
print(key)
value = []
for j in my_dict.values():
    value.append(j)
print(value)