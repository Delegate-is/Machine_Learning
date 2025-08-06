# Create nested dictionary structure and access elements
nested_dict = {
    'outer_key1': {
        'inner_key1': 'value1',
        'inner_key2': 'value2'
    },
    'outer_key2': {
        'inner_key1': 'value3',
        'inner_key2': 'value4'
    }
}
nested_dict_2 = {
    'Person': {
        'name': 'John Doe',
        'age': 30,  # Example of a person dictionary
        'address': "123 Main St, Anytown, USA"
    },
    'Places': {
        'city': 'New York',
        'country': 'USA'
    }
}
print(nested_dict_2)
print(nested_dict['outer_key1']['inner_key1'])  # Output: value1
print(nested_dict_2['Person']['name'])  # Output: John Doe
# Created a nested dic and iterate dictionary items
for outer_key, inner_dict in nested_dict.items():
    print(f"{outer_key}:")
    for inner_key, value in inner_dict.items():
        print(f"  {inner_key}: {value}")
print(nested_dict_2['Places']['city'])  # Output: New York
print(nested_dict_2['Person']['address'])  # Output: 123 Main St
print(f"City: {nested_dict_2['Places']['city']}, Country: {nested_dict_2['Places']['country']}")  # Output: City: New York, Country: USA