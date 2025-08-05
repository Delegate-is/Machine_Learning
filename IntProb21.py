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
list_1 = [ [1, 2, 3], [4, 5], [6, 7, 8, 9], ["Max", "Codeweb"], [True, False]]
total = 0
for i in list_1:
    if type(i) == list:
        total += 1
print(f"Total number of lists in the nested list: {total}")  # Display the count of lists