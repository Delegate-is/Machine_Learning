# Program Getting Two Number and Operator to Perform Arithmetic Operation
a = int(input("Enter number 1: "))
b = int(input("Enter number 2: "))
op = input("Enter arithmetic operator: ")
if(op == '+'):
    print("Addition of two number is = "+ str(a+b))
elif(op == '-'):
    print("Subtraction of two number is = "+ str(a-b))
elif(op == '*'):
    print("Multiplication of two number is = "+ str(a*b))
elif(op == '/'):
    print("Division of two number is = "+ str(a/b))
elif(op == '%'):
    print("Modulus of two number is = "+ str(a%b))
else:
    print("Invalid Operator")

def perform_arithmetic_operation(num1, num2, operator):
    """
    Performs an arithmetic operation on two numbers based on the given operator.

    Args:
        num1 (float): The first number.
        num2 (float): The second number.
        operator (str): The arithmetic operator (+, -, *, /, %, **).

    Returns:
        float or str: The result of the operation, or an error message if
                      the operator is invalid or division by zero occurs.
    """
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        if num2 == 0:
            return "Error: Cannot divide by zero!"
        return num1 / num2
    elif operator == '%':
        if num2 == 0:
            return "Error: Cannot perform modulo by zero!"
        # Modulo is typically for integers, so convert if floats are used
        return num1 % num2
    elif operator == '**':
        return num1 ** num2
    else:
        return "Error: Invalid operator. Please use +, -, *, /, %, or **."

def run_calculator():
    """
    Gets input from the user for two numbers and an operator,
    then calls perform_arithmetic_operation and displays the result.
    Allows repeated calculations.
    """
    print("--- Simple Calculator ---")
    print("Supported operators: +, -, *, /, %, **")

    while True:
        try:
            # Get the first number
            num1_str = input("Enter the first number: ").strip()
            num1 = float(num1_str) # Allow for decimal numbers

            # Get the second number
            num2_str = input("Enter the second number: ").strip()
            num2 = float(num2_str)

            # Get the operator
            operator = input("Enter the operator (+, -, *, /, %, **): ").strip()

            # Perform the operation using the function
            result = perform_arithmetic_operation(num1, num2, operator)

            # Display the result
            print(f"\nResult: {num1} {operator} {num2} = {result}")

        except ValueError:
            print("Invalid number input. Please enter valid numerical values.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}.")

        # Ask if the user wants to perform another calculation
        another_calculation = input("\nDo you want to perform another calculation? (yes/no): ").strip().lower()
        if another_calculation != 'yes':
            print("Exiting calculator. Goodbye!")
            break # Exit the loop

if __name__ == "__main__":
    run_calculator()
