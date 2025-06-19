"""
Get 6 number from user
Store to list
Display result and sum to user"""

my_list = []
for i in range(6):
    my_list.append(int(input("Enter a number: ")))
print("This is my list")
print(my_list)
print(sum(my_list))

s=0
for i in my_list:
    s += i
print("Sum of number in the list "+str(s))

"""
Get 6 number from user
Store to a tuple
Display result and sum to user"""

temp_list = []
for i in range(6):
    temp_list.append(int(input("Enter a number: ")))
Tupl = tuple(temp_list)
print(Tupl)
print("Sum: " + str(sum(Tupl)))

def calculate_tuple_sum():
    """
    Prompts the user to enter 6 numbers, stores them in a tuple,
    and then calculates and displays their sum.
    """
    print("--- Tuple Sum Calculator ---")
    numbers = []
    num_elements = 6

    print(f"Please enter {num_elements} numbers.")

    for i in range(num_elements):
        while True:
            try:
                num_input = input(f"Enter number {i + 1}: ").strip()
                # Use float to allow for decimal numbers as input
                number = float(num_input)
                numbers.append(number)
                break # Exit inner loop if valid number is entered
            except ValueError:
                print("Invalid input. Please enter a valid number.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}. Please try again.")

    # Convert the list of numbers into a tuple
    numbers_tuple = tuple(numbers)

    # Calculate the sum of the numbers in the tuple
    total_sum = sum(numbers_tuple)

    print("\n--- Results ---")
    print(f"Numbers entered (as a tuple): {numbers_tuple}")
    print(f"Sum of the numbers: {total_sum:.2f}") # Display sum with 2 decimal places

    # Ask if the user wants to run the program again
    another_round = input("\nDo you want to run this program again? (yes/no): ").strip().lower()
    if another_round != 'yes':
        print("Exiting program. Goodbye!")
        # The loop implicitly handles exiting if this is the only call to the function

if __name__ == "__main__":
    # You can loop this if you want to allow multiple runs from one execution
    while True:
        calculate_tuple_sum()
        # The 'break' in calculate_tuple_sum will handle exiting the loop
        # if the user chooses not to run again.
        break # This outer break ensures it only runs once per script execution unless manually restarted
