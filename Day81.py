# Array in Python -= collectiion of items having same data type with contigous memory location
# There is no built in array in Python hence we use 3rd party library like numpy
# Array is mutable i.e we can change the value of array
# Array is faster than list
# Array is used to perform mathematical operations
# Array module is used to create array in Python
import array as array
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print(arr[2] + arr[-1])
for i in arr:
    print(i)
print(arr[::-1])  # reverse the array
print(arr[1:4])  # slicing
print(arr.dtype)  # data type of array
print(arr.shape)  # shape of array
# np.delete(arr, index) is used to delete elements from the array
# Example: delete the element at index 2
arr_deleted = np.delete(arr, 2)
print(arr_deleted)

# np.append(arr, value) is used to append values to the array
# Example: append 6 to the array
arr_appended = np.append(arr, 6)
print(arr_appended)

import numpy as np
arr = np.array([])
for i in range(10):
    num = int(input("Enter a number: "))
    arr = np.append(arr, num)
for i in arr:
    print(i*i+5)
# program to get 5 numbers from user and display them in reverse order using array
import numpy as np
arr = np.array([])
p = 1
for i in range(5):
    num = int(input("Enter a number: "))
    arr = np.append(arr, num)
print("Array in reverse order:", arr[::-1])
for i in arr:
    p = p * i
print("Product of all elements in the array:", p)
# program to get 5 numbers from user and display only even numbers using array
import numpy as np
arr = np.array([])
for i in range(5):
    num = int(input("Enter a number: "))
    arr = np.append(arr, num)
print("Even numbers in the array:")
for i in arr:
    if i % 2 == 0:
        print(i)
# convert array to list and find sum of all elements in the list
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
lst = arr.tolist()
print("List:", lst)
print("Sum of all elements in the list:", sum(lst))
u_arr  = np.array([1, 2, 3, 4, 5])
print(type(u_arr))
lst_q = u_arr.tolist()
print(type(lst_q))
print("List:", lst_q)
print("Sum of all elements in the list:", sum(lst_q))
def find_duplicates(input_list):
    """
    Finds and returns a list of duplicate elements from a given list.

    This function follows a specific algorithm:
    1. It counts the frequency of each element in the input list using a dictionary.
    2. It then identifies which elements have a frequency greater than 1.
    3. Finally, it compiles and returns a new list containing only these duplicate elements.

    Args:
        input_list (list): The list to search for duplicates.

    Returns:
        list: A new list containing the duplicate elements found in the input_list.
    """
    # Step 2: Initialize an empty dictionary to store element frequencies.
    # The dictionary will store elements as keys and their counts as values.
    frequency_dict = {}

    # Step 3: Iterate through the input list to populate the dictionary.
    for item in input_list:
        # For each item, increment its count in the dictionary.
        # The .get(item, 0) method returns the current count for the item, or 0 if it's not present.
        frequency_dict[item] = frequency_dict.get(item, 0) + 1

    # Step 4: Create a new list to store the duplicate elements.
    duplicates = []

    # Iterate through the frequency dictionary to find elements with a count > 1.
    for item, count in frequency_dict.items():
        # Step 4 continued: If an item's count is more than 1, it's a duplicate.
        if count > 1:
            duplicates.append(item)

    # Step 5: Return the list of duplicate elements.
    return duplicates

# Example usage to demonstrate the function works as expected
if __name__ == "__main__":
    test_list_1 = [1, 2, 3, 4, 2, 5, 6, 3, 1]
    result_1 = find_duplicates(test_list_1)
    print(f"Original list: {test_list_1}")
    print(f"Duplicates found: {result_1}\n")  # Expected output: [2, 3, 1] (or in a different order)

    test_list_2 = ['apple', 'banana', 'orange', 'apple', 'grape', 'banana']
    result_2 = find_duplicates(test_list_2)
    print(f"Original list: {test_list_2}")
    print(f"Duplicates found: {result_2}\n") # Expected output: ['apple', 'banana'] (or in a different order)

    test_list_3 = [10, 20, 30]
    result_3 = find_duplicates(test_list_3)
    print(f"Original list: {test_list_3}")
    print(f"Duplicates found: {result_3}") # Expected output: []
def find_duplicates(input_list):
    """
    Finds and returns a list of duplicate elements from a given list.

    This function follows a specific algorithm:
    1. It counts the frequency of each element in the input list using a dictionary.
    2. It then identifies which elements have a frequency greater than 1.
    3. Finally, it compiles and returns a new list containing only these duplicate elements.

    Args:
        input_list (list): The list to search for duplicates.

    Returns:
        list: A new list containing the duplicate elements found in the input_list.
    """
    # Step 2: Initialize an empty dictionary to store element frequencies.
    # The dictionary will store elements as keys and their counts as values.
    frequency_dict = {}

    # Step 3: Iterate through the input list to populate the dictionary.
    for item in input_list:
        # For each item, increment its count in the dictionary.
        # The .get(item, 0) method returns the current count for the item, or 0 if it's not present.
        frequency_dict[item] = frequency_dict.get(item, 0) + 1

    # Step 4: Create a new list to store the duplicate elements.
    duplicates = []

    # Iterate through the frequency dictionary to find elements with a count > 1.
    for item, count in frequency_dict.items():
        # Step 4 continued: If an item's count is more than 1, it's a duplicate.
        if count > 1:
            duplicates.append(item)

    # Step 5: Return the list of duplicate elements.
    return duplicates

# Example usage to demonstrate the function works as expected
if __name__ == "__main__":
    test_list_1 = [1, 2, 3, 4, 2, 5, 6, 3, 1]
    result_1 = find_duplicates(test_list_1)
    print(f"Original list: {test_list_1}")
    print(f"Duplicates found: {result_1}\n")  # Expected output: [2, 3, 1] (or in a different order)

    test_list_2 = ['apple', 'banana', 'orange', 'apple', 'grape', 'banana']
    result_2 = find_duplicates(test_list_2)
    print(f"Original list: {test_list_2}")
    print(f"Duplicates found: {result_2}\n") # Expected output: ['apple', 'banana'] (or in a different order)

    test_list_3 = [10, 20, 30]
    result_3 = find_duplicates(test_list_3)
    print(f"Original list: {test_list_3}")
    print(f"Duplicates found: {result_3}") # Expected output: []
def find_duplicates(input_list):
    frequency_dict = {}
    for item in input_list:
        frequency_dict[item] = frequency_dict.get(item, 0) + 1
    duplicates = []
    for item, count in frequency_dict.items():
        if count > 1:
            duplicates.append(item)
    return duplicates