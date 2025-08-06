# Numpy program to create a 2*2 identity matrix
import numpy as np
ar = np.identity(2)
print(ar)
# Create a 1D array from a list
my_list = [1, 2, 3, 4, 5]
one_d_array_from_list = np.array(my_list)
print(one_d_array_from_list)

# Create a 1D array from a tuple
my_tuple = (6, 7, 8, 9, 10)
one_d_array_from_tuple = np.array(my_tuple)
print(one_d_array_from_tuple)
# Create a 1D array using arange (start, stop, step)
one_d_array_arange = np.arange(0, 10, 2) # Generates [0, 2, 4, 6, 8]
print(one_d_array_arange)