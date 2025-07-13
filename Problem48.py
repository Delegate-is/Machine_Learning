# Get 2 no from user, store value and swap
num1 = int(input("Enter 1st Number: "))
num2 = int(input("Enter 2nd Number: "))
print("Values before swapping")
print("num1 = "+str(num1))
print("num2 ="+str(num2))
temp = num1
num1 = num2
num2 = temp
print("Values before swapping")
print("num1 = "+str(num1))
print("num2 ="+str(num2))

def swap_numbers_without_temp():
    """
    Gets two numbers from the user and swaps their values without
    using a temporary variable. Demonstrates two methods:
    1. Using arithmetic operations.
    2. Using Python's tuple assignment (the most Pythonic way).
    """
    print("--- Number Swapper (Without Temporary Variable) ---")

    # --- Get the first number ---
    while True:
        try:
            num1_str = input("Enter the first number: ")
            num1 = float(num1_str) # Use float to handle both integers and decimals
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    # --- Get the second number ---
    while True:
        try:
            num2_str = input("Enter the second number: ")
            num2 = float(num2_str)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"\nOriginal values: First number = {num1}, Second number = {num2}")

    print("\n--- Method 1: Using Arithmetic Operations ---")
    # This method works for numbers.
    # It might have issues with very large numbers due to overflow in some languages,
    # but Python handles large integers automatically.
    # It also works for floats.

    # Example: num1 = 10, num2 = 5
    # Step 1: Add both numbers and store in num1
    # num1 = 10 + 5 = 15
    num1 = num1 + num2

    # Step 2: Subtract the original num2 from the new num1 (which is sum)
    # This effectively gives us the original num1
    # num2 = 15 - 5 = 10 (num2 now holds original num1)
    num2 = num1 - num2

    # Step 3: Subtract the new num2 (which is original num1) from the new num1 (which is sum)
    # This effectively gives us the original num2
    # num1 = 15 - 10 = 5 (num1 now holds original num2)
    num1 = num1 - num2

    print(f"After swapping (Arithmetic): First number = {num1}, Second number = {num2}")

    # To demonstrate Method 2, we need to re-get the numbers or reset them.
    # For clarity, let's just show the Pythonic way separately.
    # In a real scenario, you'd pick one method.

    print("\n--- Method 2: Using Python's Tuple Assignment (Most Pythonic) ---")
    # This method is concise, readable, and generally preferred in Python.
    # It works for any data type, not just numbers.

    # Re-get numbers for this demonstration method
    while True:
        try:
            num_a_str = input("Enter first number for Pythonic swap: ")
            num_a = float(num_a_str)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    while True:
        try:
            num_b_str = input("Enter second number for Pythonic swap: ")
            num_b = float(num_b_str)
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    print(f"Original values (Pythonic): First number = {num_a}, Second number = {num_b}")

    # The magic happens here:
    # Python evaluates the right side (num_b, num_a) first, creating a temporary tuple.
    # Then it unpacks this tuple into num_a and num_b on the left side.
    num_a, num_b = num_b, num_a

    print(f"After swapping (Pythonic): First number = {num_a}, Second number = {num_b}")

# Call the function to run the program
if __name__ == "__main__":
    swap_numbers_without_temp()
