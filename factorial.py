def calculate_factorial(n):
    """Calculate factorial of a non negative integer n."""
    if n < 0:
        raise ValueError("Factorial is not defined for negative integers.")
    if n == 0 or n==1:
        return 1
    result = 1
    # Calculate factorial iteratively - loop from 2 to n
    for i in range(2, n + 1):
        result *= i
    return result

# Prompt the user for input
try:
    n = int(input("Enter a non-negative integer: "))
    result = calculate_factorial(n)
    print(f"The factorial of {n} is {result}.")
except ValueError as e:
    print(e)
    # Example usage:
    # n = 5
    # print(f"The factorial of {n} is {factorial(n)}.")