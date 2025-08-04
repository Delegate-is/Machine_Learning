list = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))  # Input numbers from the user
    list.append(num)  # Append each number to the list
print("List of numbers:", list)  # Display the list of numbers
new_list = [i*i*i for i in list]  # Create a new list with squares of the original numbers
print("New list with cubes of the numbers:", new_list)  # Display the new list
# Add all number to each other using list comprehension
sum_of_numbers = sum(list)  # Calculate the sum of all numbers in the list
print(f"Sum of all numbers in the list: {sum_of_numbers}")  # Display the sum
