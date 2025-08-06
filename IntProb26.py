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
my_dict_1 = {'key1': 'apple', 'key2': 'banana', 'key3': 'orange'}
print(my_dict_1)
keys = ()
for i in my_dict_1.keys():
    key.append(i)
print(key)
values = ()
for j in my_dict_1.values():
    value.append(j)
print(value)
def convert_dict_to_tuples(input_dict):
    """
    Converts a dictionary's keys into one tuple and its values into another tuple.

    Args:
        input_dict (dict): The dictionary to convert.

    Returns:
        tuple: A tuple containing two tuples: (keys_tuple, values_tuple).
               Returns ((), ()) if the input is not a dictionary or is empty.
    """
    if not isinstance(input_dict, dict):
        print("Error: Input must be a dictionary.")
        return ((), ()) # Return empty tuples for invalid input

    # Get all keys from the dictionary and convert them to a tuple
    keys_tuple = tuple(input_dict.keys())

    # Get all values from the dictionary and convert them to a tuple
    values_tuple = tuple(input_dict.values())

    return (keys_tuple, values_tuple)

# --- Example Usage ---
if __name__ == "__main__":
    print("--- Dictionary to Tuples Converter ---")

    # Example 1: A simple dictionary
    my_dict_1 = {
        "name": "Alice",
        "age": 30,
        "city": "New York"
    }
    print(f"\nOriginal Dictionary 1: {my_dict_1}")
    keys_1, values_1 = convert_dict_to_tuples(my_dict_1)
    print(f"Keys Tuple 1: {keys_1}")
    print(f"Values Tuple 1: {values_1}")

    # Example 2: A dictionary with mixed data types
    my_dict_2 = {
        1: "one",
        "two": 2,
        True: "boolean",
        (3, 4): [5, 6] # Tuple key, list value
    }
    print(f"\nOriginal Dictionary 2: {my_dict_2}")
    keys_2, values_2 = convert_dict_to_tuples(my_dict_2)
    print(f"Keys Tuple 2: {keys_2}")
    print(f"Values Tuple 2: {values_2}")

    # Example 3: An empty dictionary
    empty_dict = {}
    print(f"\nOriginal Empty Dictionary: {empty_dict}")
    keys_empty, values_empty = convert_dict_to_tuples(empty_dict)
    print(f"Keys Tuple (Empty): {keys_empty}")
    print(f"Values Tuple (Empty): {values_empty}")

    # Example 4: Invalid input (not a dictionary)
    print("\n--- Testing Invalid Input ---")
    keys_invalid, values_invalid = convert_dict_to_tuples("this is a string")
    print(f"Keys Tuple (Invalid Input): {keys_invalid}")
    print(f"Values Tuple (Invalid Input): {values_invalid}")
