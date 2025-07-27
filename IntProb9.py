# Program to sort dictionary by key
dict = {"Name":"Max", "Age":"24","Course":"Python","City":"Kagio"}
print(dict)
print(sorted(dict.items()))

def sort_dictionary_by_value(input_dict, reverse=False):
    """
    Sorts a dictionary by its values and returns a new sorted list of (key, value) tuples.

    Args:
        input_dict (dict): The dictionary to be sorted.
        reverse (bool, optional): If True, the dictionary will be sorted in descending order
                                  by value. Defaults to False (ascending order).

    Returns:
        list: A list of (key, value) tuples, sorted by the values.
    """
    if not isinstance(input_dict, dict):
        print("Error: Input must be a dictionary.")
        return []

    print(f"\n--- Sorting Dictionary by Value ---")
    print(f"Original Dictionary: {input_dict}")

    # Use the sorted() function with a custom key for sorting by value.
    # dict.items() returns a list of (key, value) tuples.
    # The lambda function `lambda item: item[1]` specifies that the sorting
    # should be based on the second element of each tuple (which is the value).
    sorted_items = sorted(input_dict.items(), key=lambda item: item[1], reverse=reverse)

    print(f"Sorted by Value (Reverse={reverse}): {sorted_items}")
    return sorted_items

# --- Example Usage ---
if __name__ == "__main__":
    my_data = {
        "apple": 50,
        "banana": 10,
        "cherry": 80,
        "date": 30,
        "elderberry": 10
    }

    # Sort in ascending order by value
    print("\n--- Example 1: Ascending Order ---")
    sorted_ascending = sort_dictionary_by_value(my_data)

    # Sort in descending order by value
    print("\n--- Example 2: Descending Order ---")
    sorted_descending = sort_dictionary_by_value(my_data, reverse=True)

    # Example with string values
    string_data = {
        "cat": "fluffy",
        "dog": "loyal",
        "bird": "singing",
        "fish": "swimming"
    }
    print("\n--- Example 3: Sorting with String Values (Ascending) ---")
    sorted_strings = sort_dictionary_by_value(string_data)

    # Example with mixed value types (will cause TypeError if values are not comparable)
    mixed_data = {
        "item1": 10,
        "item2": "abc", # This would cause an error if directly compared with numbers
        "item3": 5
    }
    # Uncomment the line below to see the TypeError if values are not comparable
    # print("\n--- Example 4: Sorting with Mixed Value Types (will error) ---")
    # sort_dictionary_by_value(mixed_data)

    # Example with an empty dictionary
    empty_dict = {}
    print("\n--- Example 5: Empty Dictionary ---")
    sort_dictionary_by_value(empty_dict)

    # Example with non-dictionary input
    print("\n--- Example 6: Non-dictionary Input ---")
    sort_dictionary_by_value([1, 2, 3])
