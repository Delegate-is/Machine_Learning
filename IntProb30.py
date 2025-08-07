# Get a dict and find addition of all keys plus product of all values
dict = {1:332, 2:234, 3:3321, 4:123}
print(dict)
keys = []
for k in dict.keys():
    keys.append(k)
print(keys)
addition = 0
for i in keys:
    addition += i
print(addition)
values = []
for v in dict.values():
    values.append(v)
print(values)
product = 1
for i in values:
    product *= i
print(product)
def display_set_from_list(input_list):
    """
    Converts a list to a set and displays the resulting set.

    A set automatically removes duplicate elements and does not preserve order.

    Args:
        input_list (list): The list to be converted.

    Returns:
        set: A new set containing the unique elements from the input list.
    """
    # Use the built-in set() constructor to convert the list.
    # This automatically handles the removal of duplicate elements.
    unique_elements_set = set(input_list)
    return unique_elements_set

# --- Example Usage ---
if __name__ == "__main__":
    print("--- List to Set Converter ---")

    # Example 1: A list with duplicate numbers
    list_with_duplicates = [1, 2, 2, 3, 4, 4, 4, 5]
    print(f"\nOriginal List: {list_with_duplicates}")
    set_from_list_1 = display_set_from_list(list_with_duplicates)
    print(f"Set of Elements: {set_from_list_1}")

    # Example 2: A list with duplicate strings
    list_of_names = ["Alice", "Bob", "Alice", "Charlie", "Bob"]
    print(f"\nOriginal List: {list_of_names}")
    set_from_list_2 = display_set_from_list(list_of_names)
    print(f"Set of Elements: {set_from_list_2}")

    # Example 3: A list with mixed data types and duplicates
    mixed_list = [1, "a", 2, True, 1, "a"]
    print(f"\nOriginal List: {mixed_list}")
    set_from_list_3 = display_set_from_list(mixed_list)
    print(f"Set of Elements: {set_from_list_3}")

    # Example 4: An empty list
    empty_list = []
    print(f"\nOriginal Empty List: {empty_list}")
    set_from_list_4 = display_set_from_list(empty_list)
    print(f"Set of Elements: {set_from_list_4}")