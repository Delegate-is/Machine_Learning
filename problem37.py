# Program to get number and display its cube
num = int(input("Enter a number: "))
cube = num * num * num
print(f"The cube of {str(num)} is {str(cube)}")  # Display the cube of the number
# Program to get six numbers from user, display cube of first 3 and square the rest
numbers = []
for i in range(6):
    num_str = input("Enter a number " + str(i + 1) + ": ")  # Prompt user for input
    number = float(num_str)
    numbers.append(number)  # Append the number to the list 
    if i < 3:
        cube = number ** 3  # Calculate the cube of the first three numbers
        print(f"The cube of {str(number)} is {str(cube)}")  # Display the cube
    else:
        square = number ** 2  # Calculate the square of the last three numbers
        print(f"The square of {str(number)} is {str(square)}")  # Display the square

# Program to get six numbers from the user,
# display the cube of the first 3, and square the rest.

def perform_operations_on_numbers():
    """
    Prompts the user to enter six numbers, then calculates the cube
    of the first three and the square of the last three, displaying
    each result.
    """
    numbers = []
    results = []

    print("Please enter six numbers:")

    # Loop to get six numbers from the user
    for i in range(6):
        while True:
            try:
                # Prompt for each number
                num_str = input(f"Enter number {i + 1}: ")
                # Convert input to a float to handle both integers and decimals
                number = float(num_str)
                numbers.append(number)
                break  # Exit loop if input is valid
            except ValueError:
                # Handle cases where input is not a valid number
                print("Invalid input. Please enter a valid number.")

    print("\n--- Results ---")

    # Iterate through the collected numbers and perform operations
    for i, num in enumerate(numbers):
        if i < 3:
            # For the first three numbers (index 0, 1, 2), calculate the cube
            cube = num ** 3
            results.append(f"The cube of {num} is: {cube}")
        else:
            # For the remaining three numbers (index 3, 4, 5), calculate the square
            square = num ** 2
            results.append(f"The square of {num} is: {square}")

    # Display all calculated results
    for result in results:
        print(result)

# Call the function to run the program
if __name__ == "__main__":
    perform_operations_on_numbers()
