# Program to Reverse Array
import numpy as np
ar = np.array([12,3,4,6,78,4])
print(ar)
r_ar = np.flip(ar)
print(r_ar)
float_array = np.array([1.2, 3.8, -0.5, 4.0])
print(float_array)
int_array = float_array.astype(int) # Result: array([1, 3, 0, 4])
print(int_array)
# Convert given array into list
ar1 = np.array([1,2,3,4,6,654])
print(ar1)
print(type(ar1))
lst = ar1.tolist()
print(lst)
print(type(lst))

from array import array
my_list = [1, 2, 3, 4, 5]
print(my_list)
print(type(my_list))
# Convert to an array of signed integers ('i' type code)
my_array = array('i', my_list) 
print(my_array)
print(type(my_array))

# Numpy program to convert array element into Boolean Value
ar2 = np.array([0,1,0,1,0,1,0,1])
print(ar2)
bool_arr = ar2.astype('bool')
print(bool_arr)

import numpy as np
# Create a NumPy array
original_array = np.array([1, 2, 3, 4, 5], dtype=np.int32)
# Convert the array to bytes
array_as_bytes = original_array.tobytes()
print(f"Original array: {original_array}")
print(f"Array as bytes: {array_as_bytes}")