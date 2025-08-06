# Print dictionary items line by line and key value has one tab distance
dict_3 = {
    'name': 'Alice',
    'age': 25,
    'city': 'Wonderland'
}
for key, value in dict_3.items():
    print(f"{key}:\t{value}")  # Output: name: Alice, age: 25, city: Wonderland
print(f"Name: {dict_3['name']}, Age: {dict_3['age']}, City: {dict_3['city']}")  # Output: Name: Alice, Age: 25, City: Wonderland
# Create alpha string based dictionary and print in upper case
dict_alpha = {
    'a': 1,
    'b': 2,
    'c': 3
}
for key, value in dict_alpha.items():
    print(f"{key.upper()}\t:\t{value}")  # Output: A: 1, B: 2, C: 3