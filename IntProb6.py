dict = {"Name":"Max", "Age":38, "cors":"Python"}
old_key = input("Enter a key you want to update: ")
new_key = input("Enter a new key: ")
dict[new_key] = dict[old_key]
del dict[old_key]
print(dict)

def calculate_total_length_of_dict_elements(my_dict):
    """
    Calculates the total length of all keys and values in a dictionary.
    For strings, length is the number of characters.
    For other iterable types (like lists, tuples), length is the number of elements.
    Non-iterable types will have a length of 1 for their value (as they are a single item).

    Args:
        my_dict (dict): The dictionary to process.

    Returns:
        int: The total calculated length.
    """
    total_length = 0

    print(f"\n--- Calculating total length for dictionary: {my_dict} ---")

    # Iterate through keys and values
    for key, value in my_dict.items():
        # Calculate length of the key
        if isinstance(key, str):
            key_length = len(key)
        else:
            # For non-string keys (e.g., numbers, tuples), consider their string representation length
            # or simply 1 if you consider them as a single item.
            # For this problem, let's assume 'length' refers to string length where applicable.
            # If a key is not a string, its 'length' is typically not defined in the same way.
            # We'll treat non-string keys as having a length of 1 for simplicity,
            # or their string representation's length if that's more appropriate for "total length".
            # Let's go with string representation for consistency with "length".
            key_length = len(str(key))
        total_length += key_length
        print(f"  Key: '{key}' (Length: {key_length})")


        # Calculate length of the value
        if isinstance(value, str):
            value_length = len(value)
        elif isinstance(value, (list, tuple, dict, set)):
            # For collections, length is the number of items
            value_length = len(value)
        else:
            # For other types (numbers, booleans, etc.), they are single items
            value_length = 1
        total_length += value_length
        print(f"  Value: '{value}' (Length: {value_length})")

    return total_length

if __name__ == "__main__":
    # Example 1: Dictionary with strings and numbers
    dict1 = {
        "name": "Alice",
        "age": 30,
        "city": "New York",
        "zip": 10001
    }
    total_len1 = calculate_total_length_of_dict_elements(dict1)
    print(f"Total length of keys and values in dict1: {total_len1}\n")

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
if n1 > n2:
    print("n1 is the max number")
else:
    print("n2 is the max number")