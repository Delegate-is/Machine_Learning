# Prob37- pass array with shape(4,3) filled with 0s
import numpy as np
num_str = input("Enter two numbers separated by a space: ")
num1, num2 = map(int, num_str.split())
ar = np.zeros((num1, num2), dtype=np.int64)  # change np.ones to np.zeros to have 0s
print(ar)
ar1 = np.zeros((1, 2), dtype=np.int64) 
print(ar1)
# Prob 38 -- 1D array using for loop
n = int(input("Enter a number: "))
ar2 = np.zeros((n), dtype=np.int64)
for i in range(len(ar2)):
    element= int(input("Enter array element"))
    ar2[i] = element
print(ar2)
import numpy as np

# Initialize an empty list to store user inputs
elements = []

# Loop to get elements from the user
while True:
    user_input = input("Enter an element (or 'done' to finish): ")
    if user_input.lower() == 'done':
        break
    try:
        # Attempt to convert input to a float (or int if preferred)
        elements.append(float(user_input))
    except ValueError:
        print("Invalid input. Please enter a number or 'done'.")

# Convert the list of elements to a NumPy array
one_d_array = np.array(elements)

print("\nYour one-dimensional NumPy array:")
print(one_d_array)