# Prob37- pass array with shape(4,3) filled with 0s
import numpy as np
num_str = input("Enter two numbers separated by a space: ")
num1, num2 = map(int, num_str.split())
ar = np.zeros((num1, num2), dtype=np.int64)  # change np.ones to np.zeros to have 0s
print(ar)
ar1 = np.zeros((1, 2), dtype=np.int64) 
print(ar1)
# Prob 38 -- 1D array using for loop