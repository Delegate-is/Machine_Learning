# Update any value on dict on user request
dict1 = {1:"Uno",2:"Dooh", 3:"Euros", 14:"Ends"}
print(dict1)
key = int(input("Enter a key you wish to update: "))
val = input("Enter a value you wish to update: ")
dict1[key] = val
print(dict1)
dict = {1:"Uno",2:"Dooh", 3:"Euros", 14:"Ends"}
print(dict)
val = input("Enter a value you wish to update: ")
key = int(input("Enter a key you wish to update: "))
val = dict[key]
print(dict1)

def update_dictionary_key(data_dict):
    """
    Allows the user to update an existing key's value or add a new key-value pair
    to a dictionary.

    Args:
        data_dict (dict): The dictionary to be updated.
    """
    while True:
        print("\nCurrent Dictionary:", data_dict)
        key_to_update = input("Enter the key you want to update (or type 'quit' to exit): ").strip()

        if key_to_update.lower() == 'quit':
            break

        new_value = input(f"Enter the new value for '{key_to_update}': ").strip()

        # Update the dictionary
        data_dict[key_to_update] = new_value
        print(f"Dictionary updated: {key_to_update} now has value '{new_value}'")

# Example usage:
my_dict = {"name": "Alice", "age": "30", "city": "New York"}
update_dictionary_key(my_dict)
print("\nFinal Dictionary:", my_dict)