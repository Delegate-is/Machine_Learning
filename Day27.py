# Python code to format a name input by the user
name = input("Enter a name: ")
name.upper()  # Convert to uppercase
name = name.strip()  # Remove leading and trailing spaces
if not name.endswith('.'):
    name += '.'  # Add full stop if not present
name = name.capitalize()  # Capitalize the first letter of the name
print("Formatted name:", name.upper())  # Display the formatted name

# Program to get age from use and convert into seconds
age = float(input("Enter your age:"))
print("Your age is "+ str(age))
one_year_in_seconds = 365 * 24 * 60 * 60  # Calculate seconds in one year
age_in_seconds = age * one_year_in_seconds  # Convert age to seconds
print("Your age in seconds is:", age_in_seconds)
# Program to get 3 numbers from user and increase by 1
for i in range(3):
    number = int(input("Enter a number: "))
    print(str(number))
    number += 1  # Increase the number by 1
    print("Increased number:", number)  # Display the increased number
#Multiply 1st aand 3rd number and add 2nd & 3rd number
first_number = int(input("Enter the first number: "))
print("First number is:", str(first_number))
second_number = int(input("Enter the second number: "))
print("Second number is:", str(second_number))
third_number = int(input("Enter the third number: "))
print("Third number is:", str(third_number))
result_1 = (first_number * second_number) / third_number  # Calculate the result
result_2 = (second_number + third_number)  # Calculate the result
print("Result of first number multiplied by second number divided by third number is:", result_1)  # Display the result
print("Result of second number added to third number is:", result_2)  # Display the result
# Program to get a number from user and display its square
number = int(input("Enter a number: "))
square = number ** 2  # Calculate the square of the number
print("The square of", number, "is", square)  # Display the square of the number
print("\n")
# Create a dictionary named student with the following keys and values:
std_dict = {
"name": "John",
"age": "25",
"city": "New York"
}
print("Original dictionary:", std_dict)  # Print the original dictionary
# Add a new key-value pair to the student dictionary:
std_dict["country"] = "USA"  # Add country key with value USA
# Print the updated dictionary.
print("Updated dictionary:", std_dict)  # Print the updated dictionary

# Create a set named subjects with the following elements:
subjects = {"Math", "Science", "History", "Math", "Geography"}  # Create a set with subjects
# Print the set to see if any duplicate elements are present.
print("Subjects set:", subjects)  # Print the set of subjects
# Add a new subject to the set.
subjects.add("English")  # Add English subject to the set
# Print the updated set.
print("Updated subjects set:", subjects)  # Print the updated set of subjects
print("\n")
# Create a tuple named colors with the following elements:
colors = ("Red", "Green", "Blue", "Yellow")  # Create a tuple with colors
# Print the tuple to see its elements.
print("Colors tuple:", colors)  # Print the tuple of colors
# Add a new color to the tuple (tuples are immutable, so we need to create a new one).
colors = colors + ("Purple",)  # Create a new tuple with the added color
# Print the updated tuple.
print("Updated colors tuple:", colors)  # Print the updated tuple of colors
print("\n")
# Create a list named fruits with the following elements:
fruits = ["Apple", "Banana", "Cherry", "Date"]  # Create a list with fruits
# Print the list to see its elements
print("Fruits list:", fruits)  # Print the list of fruits
# Add a new fruit to the list.
fruits.append("Elderberry")  # Add Elderberry to the list of fruits
# Print the updated list.
print("Updated fruits list:", fruits)  # Print the updated list of fruits
