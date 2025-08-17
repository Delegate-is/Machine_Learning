# Create num table using OOP
class Table:
    def getNum(self):
        self.num = int(input("Enter a number: "))
        
    def showTable(self):
        for i in range(1, 11):
            print(str(i)+" * "+str(self.num)+" = "+str(i*self.num))
obj = Table()
obj.getNum()
obj.showTable()
import numpy as np

# Get dimensions from the user
rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

# Initialize an empty list to store rows
data = []

# Input elements for each row using a while loop
i = 0
while i < rows:
    row_str = input(f"Enter row {i + 1} elements separated by spaces: ")
    # Convert string input to a list of integers
    row = list(map(int, row_str.split()))

    # Basic validation for column count
    if len(row) != cols:
        print(f"Error: Row {i + 1} must have {cols} elements. Please re-enter.")
        continue # Ask for input for the same row again
    
    data.append(row)
    i += 1

# Convert the list of lists to a NumPy 2D array
arr = np.array(data)

# Display the 2D array using nested while loops
print("\n2D NumPy Array:")
row_idx = 0
while row_idx < arr.shape[0]: # arr.shape[0] gives the number of rows
    col_idx = 0
    while col_idx < arr.shape[1]: # arr.shape[1] gives the number of columns
        print(arr[row_idx, col_idx], end=" ")
        col_idx += 1
    print() # Newline after each row
    row_idx += 1