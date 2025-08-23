# Create pandas series to convert to Python list
import pandas
ps = pandas.Series([11,223,43,54,5])
print(ps)
print(type(ps))
ps_list = ps.tolist()
print(ps_list)
print(type(ps_list))
print(ps_list[0:3])
def binary_to_decimal_recursive(binary_string):
    """
    Converts a binary string to its decimal equivalent using recursion.

    Args:
        binary_string (str): The binary number as a string.

    Returns:
        int: The decimal equivalent of the binary number.
    """
    # Base case: If the string is empty, the decimal value is 0
    if not binary_string:
        return 0
    else:
        # Recursive step:
        # Take the last digit (LSB) and convert it to an integer
        last_digit = int(binary_string[-1])
        # Recursively call the function with the rest of the string (excluding the last digit)
        # Multiply the result by 2 (shifting left in binary terms)
        # Add the value of the current last digit
        return binary_to_decimal_recursive(binary_string[:-1]) * 2 + last_digit

# Example usage:
binary_num1 = "1011"
decimal_num1 = binary_to_decimal_recursive(binary_num1)
print(f"The decimal equivalent of {binary_num1} is {decimal_num1}")

binary_num2 = "11110"
decimal_num2 = binary_to_decimal_recursive(binary_num2)
print(f"The decimal equivalent of {binary_num2} is {decimal_num2}")

binary_num3 = "1"
decimal_num3 = binary_to_decimal_recursive(binary_num3)
print(f"The decimal equivalent of {binary_num3} is {decimal_num3}")

binary_num4 = "0"
decimal_num4 = binary_to_decimal_recursive(binary_num4)
print(f"The decimal equivalent of {binary_num4} is {decimal_num4}")

# Generate random num and dispay if random num is matched
import random
# s = int(input("Enter a start number"))
# e = int(input("Enter an end number"))
# msg = input("Enter a message")
req_num = int(input("Enter a number to match"))
gen_n = random.randint(0,10)

if gen_n == req_num:
    print("It is matched")
else:
    print("Number did not match")
    
import random

def get_student_names(num_students=10):
    """
    Prompts the user to enter a specified number of student names and
    returns them as a list.

    Args:
        num_students (int): The number of student names to collect.
    
    Returns:
        list: A list of the entered student names.
    """
    students = []
    print(f"Please enter {num_students} student names:")
    for i in range(num_students):
        name = input(f"Enter name #{i + 1}: ")
        students.append(name)
    return students

def randomize_and_display(student_list, excluded_name):
    """
    Removes an excluded name from a list, randomizes the remaining names,
    and then displays them.

    Args:
        student_list (list): The list of student names.
        excluded_name (str): The name to exclude from the list.
    """
    # Create a copy of the list to avoid modifying the original list
    display_list = student_list[:]
    
    # Remove the excluded name if it exists in the list
    try:
        display_list.remove(excluded_name)
    except ValueError:
        print(f"Note: '{excluded_name}' was not found in the list.")
    
    # Shuffle the list in place
    random.shuffle(display_list)
    
    print("\nDisplaying randomized student names:")
    for name in display_list:
        print(name)

# --- Main part of the program ---
if __name__ == "__main__":
    # Get 10 student names from the user
    all_students = get_student_names(10)
    
    # Get the name to be excluded
    name_to_exclude = input("\nEnter the name you want to exclude: ")
    
    # Randomize and display the names
    randomize_and_display(all_students, name_to_exclude)

