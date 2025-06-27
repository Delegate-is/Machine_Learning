# Get no from user and check if its even or odd
# num = int(input("Enter a number: "))
""" if(num/2):
    print("It is an even number")
else:
    print("It is an odd number")"""

num1 = int(input("Enter a number: "))
if(num1%2 == 0):
    print("It is an even number")
else:
    print("It is an odd number")
print(num1**2)

def check_even_odd_and_square():
    """
    Prompts the user to enter a number, checks if it's even or odd,
    and then calculates and displays its square.
    """
    print("--- Even/Odd and Number Square Checker ---")

    while True:
        try:
            # Get the number from the user
            num_str = input("Enter an integer number: ").strip()
            number = int(num_str) # Ensure it's an integer for even/odd check

            # Check if the number is even or odd
            if number % 2 == 0:
                even_odd_status = "Even"
            else:
                even_odd_status = "Odd"

            # Calculate the square of the number
            number_square = number ** 2

            print(f"\nThe number entered is: {number}")
            print(f"Status: {number} is an {even_odd_status} number.")
            print(f"The square of {number} is: {number_square}")

        except ValueError:
            print("Invalid input. Please enter a whole number (integer).")
        except Exception as e:
            print(f"An unexpected error occurred: {e}.")

        # Ask if the user wants to check another number
        another_check = input("\nDo you want to check another number? (yes/no): ").strip().lower()
        if another_check != 'yes':
            print("Exiting program. Goodbye!")
            break # Exit the loop

if __name__ == "__main__":
    check_even_odd_and_square()
