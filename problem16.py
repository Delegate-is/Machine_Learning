# Progra that Performs All Compound Assignment on an integer
"""Get a number from the user.
       Store that number in the variable.
       Using compound assignment operators(+=,-=./=,*=,%=etc), perform operations on that number.
       display the result to user 
"""
num1 = int(input("Enter an integer number: "))
print(num1)
# Addition assignment operator
num1 += 5 # num+5 -> 5+5=10
print(num1)
# Subtraction assignment operator
num1 -= 5 #10-5=5
print(f"Updated value: {num1}")
# Multiplication assignment operator
num1 *= 5 #5*5=25
print(f"Updated value after multiplying: {num1}")
# Division assignment operator
num1 /= 5 # 25/5=5.0
print(f"Updated value after division: {num1}")
# Modulus assignment operator
num1 %= 5 # 5.0%5=0.0
print(f"Updated value: {num1}")
# Removed concatenation of print() results, as print() returns None.

def perform_compound_assignments():
    """
    Demonstrates compound assignment operations on an integer,
    sums the results, and displays the final sum.
    """
    print("--- Compound Assignment Operations Calculator ---")

    while True:
        try:
            # Get an initial integer from the user
            initial_value_str = input("Enter an integer to start with: ").strip()
            num = int(initial_value_str)

            # List to store all intermediate and final results
            all_results = []
            all_results.append(num) # Add the initial value

            print(f"\nStarting value: {num}")
            print("-" * 30)

            # 1. Addition Assignment (+=)
            original_num = num # Store original for display
            num += 5
            print(f"After num += 5: num is now {num}")
            all_results.append(num)

            # 2. Subtraction Assignment (-=)
            num -= 3
            print(f"After num -= 3: num is now {num}")
            all_results.append(num)

            # 3. Multiplication Assignment (*=)
            num *= 2
            print(f"After num *= 2: num is now {num}")
            all_results.append(num)

            # 4. Division Assignment (/=)
            # Be careful with division by zero. Assuming operation will not cause it.
            # If the result of division needs to remain an integer, use //=
            num /= 4
            print(f"After num /= 4: num is now {num}")
            all_results.append(num)

            # 5. Floor Division Assignment (//=)
            # Ensure num is an integer or can be converted for clear floor division
            num = int(num) # Convert to int if it's a float from previous division
            num //= 2
            print(f"After num //= 2: num is now {num}")
            all_results.append(num)

            # 6. Modulo Assignment (%=)
            num %= 3
            print(f"After num %= 3: num is now {num}")
            all_results.append(num)

            # 7. Exponentiation Assignment (**=)
            num **= 2
            print(f"After num **= 2: num is now {num}")
            all_results.append(num)

            # Add more if needed, e.g., bitwise operators <<=, >>=, &=, |=, ^=
            # For simplicity, sticking to common arithmetic ones.

            print("-" * 30)
            print(f"All intermediate results: {all_results}")

            # Sum all the results
            final_sum_of_results = sum(all_results)
            print(f"Sum of all intermediate results (including initial value): {final_sum_of_results:.2f}")

            # Ask if the user wants to run the program again
            another_round = input("\nDo you want to perform operations with another number? (yes/no): ").strip().lower()
            if another_round != 'yes':
                print("Exiting program. Goodbye!")
                break # Exit the loop and end the program

        except ValueError:
            print("Invalid input. Please enter a whole number (integer).")
        except ZeroDivisionError:
            print("Error: Division by zero occurred during an operation. Please choose a different starting number.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

if __name__ == "__main__":
    perform_compound_assignments()
