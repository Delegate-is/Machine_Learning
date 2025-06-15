# Program that perfoms all arithmetic operations on two numbers
n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))
print("Addition is equal to: " + str(n1 + n2))
print("Subtraction is equal to: " + str(n1 - n2))
print("Multiplication is equal to: " + str(n1 * n2))
print("Division is equal to: " + str(n1 / n2))
print("Modulus is equal to: " + str(n1 % n2))
print("Exponentiation is equal to: " + str(n1 ** n2))
print("Floor Division is equal to: " + str(n1 // n2))

def perform_arithmetic_operations():
    """
    Prompts the user to enter three numbers and performs
    addition, subtraction, multiplication, and division on them.
    """
    print("--- Arithmetic Operations on Three Variables ---")

    while True:
        try:
            # Get input for the first number
            num1_str = input("Enter the first number: ").strip()
            num1 = float(num1_str) # Use float to handle decimals

            # Get input for the second number
            num2_str = input("Enter the second number: ").strip()
            num2 = float(num2_str)

            # Get input for the third number
            num3_str = input("Enter the third number: ").strip()
            num3 = float(num3_str)

            print("\n--- Results ---")

            # Addition
            sum_result = num1 + num2 + num3
            print(f"Addition: {num1} + {num2} + {num3} = {sum_result}")

            # Subtraction (various combinations)
            sub_result1 = num1 - num2 - num3
            print(f"Subtraction (num1 - num2 - num3): {num1} - {num2} - {num3} = {sub_result1}")
            sub_result2 = num2 - num1 - num3
            print(f"Subtraction (num2 - num1 - num3): {num2} - {num1} - {num3} = {sub_result2}")

            # Multiplication
            mult_result = num1 * num2 * num3
            print(f"Multiplication: {num1} * {num2} * {num3} = {mult_result}")

            # Division (various combinations, handle division by zero)
            print("\n--- Division Results ---")
            # num1 / num2 / num3
            if num2 != 0 and num3 != 0:
                div_result1 = num1 / num2 / num3
                print(f"Division (num1 / num2 / num3): {num1} / {num2} / {num3} = {div_result1}")
            else:
                print(f"Division (num1 / num2 / num3): Cannot divide by zero if num2 or num3 is zero.")

            # num1 / (num2 + num3) - example of using parentheses
            if (num2 + num3) != 0:
                div_result_paren = num1 / (num2 + num3)
                print(f"Division (num1 / (num2 + num3)): {num1} / ({num2} + {num3}) = {div_result_paren}")
            else:
                print(f"Division (num1 / (num2 + num3)): Cannot divide by zero.")

            # Modulo (remainder) - for integer inputs typically
            print("\n--- Modulo Results (if applicable, using integers for demo) ---")
            try:
                # Convert to int for modulo, if original input was suitable
                int_num1, int_num2, int_num3 = int(num1), int(num2), int(num3)
                if int_num2 != 0:
                    mod_result1 = int_num1 % int_num2
                    print(f"Modulo (num1 % num2): {int_num1} % {int_num2} = {mod_result1}")
                else:
                    print(f"Modulo (num1 % num2): Cannot perform modulo by zero (num2).")
                if int_num3 != 0:
                    mod_result2 = int_num1 % int_num3
                    print(f"Modulo (num1 % num3): {int_num1} % {int_num3} = {mod_result2}")
                else:
                    print(f"Modulo (num1 % num3): Cannot perform modulo by zero (num3).")
            except ValueError:
                print("Modulo operations are best suited for integer inputs. Skipping for non-integer results.")
            except Exception as e:
                print(f"An error occurred during modulo calculation: {e}")


            # Exponentiation
            print("\n--- Exponentiation Results ---")
            exp_result1 = num1 ** num2
            print(f"Exponentiation (num1 ** num2): {num1} ** {num2} = {exp_result1}")
            exp_result2 = num2 ** num3
            print(f"Exponentiation (num2 ** num3): {num2} ** {num3} = {exp_result2}")


            # Ask if the user wants to perform operations again or exit
            another_check = input("\nDo you want to perform operations again? (yes/no): ").strip().lower()
            if another_check != 'yes':
                print("Exiting program. Goodbye!")
                break # Exit the loop and end the program

        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

if __name__ == "__main__":
    perform_arithmetic_operations()
