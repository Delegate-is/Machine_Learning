import numpy as np
ar = np.array([1,2,3,4,5,6])
file = open("file.txt", "w+")
file.write(str(ar))
file.close()
r_file = open("file.txt","r")
con = r_file.read
print(con)
r_file.close()
import numpy as np

# 1. Define the array to be saved
original_array = np.array([[1, 2, 3],
                           [4, 5, 6],
                           [7, 8, 9]])

# 2. Save the array to a text file
file_name = "my_array_data.txt"
np.savetxt(file_name, original_array, fmt='%d') # fmt='%d' for integer formatting

print(f"Array saved to '{file_name}':")
print(original_array)

# 3. Load the array from the text file into a new array
loaded_array = np.loadtxt(file_name, dtype=int) # dtype=int to load as integers

print(f"\nArray loaded from '{file_name}':")
print(loaded_array)

# Verify if the loaded array is identical to the original
if np.array_equal(original_array, loaded_array):
    print("\nOriginal and loaded arrays are identical.")
else:
    print("\nOriginal and loaded arrays are different.")

# Numpy program to get 4x4 and other zeros
arr = np.diag([6,7,8,9])
print(arr)
arr_1 = np.zeros((4,4))
print(arr_1)
# isidentifier method
identifier = input("Enter an identifier")

if identifier.isidentifier():
    print("This is a valid identifier")
else:
    print("Not a valid")
te = 2
if str(te).isdigit():
    print(True)
else:
    print(False)