# Create 2D array and multiply with an no
import numpy as np
ar = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print(ar)
item = int(input("Enter a number: "))
new_ar = item*ar
print(new_ar)
import numpy as np

# Create a sample one-dimensional array
original_array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Use boolean indexing to filter for even numbers
# The modulo operator (%) returns the remainder of a division.
# If a number divided by 2 has a remainder of 0, it is even.
even_numbers_array = original_array[original_array % 2 == 0]

# Print the resulting array
print("Original array:", original_array)
print("Array with only even numbers:", even_numbers_array)