# Get two number from user, power three and sum
num = input("Enter two numbers seperated by space: ")
num1, num2 = map(float, num.split())
pow_num1 = pow(num1, 3)  # Raise num1 to the power of 3
pow_num2 = pow(num2, 3)  # Raise num2 to the power of 3
print(f"Power of {num1} to 3 is: {pow_num1}")  # Output: Power of num1 to 3
print(f"Power of {num2} to 3 is: {pow_num2}")  # Output: Power of num2 to 3
result_sum = pow_num1 + pow_num2  # Sum of the two powered numbers
print(f"Sum of the two powered numbers is: {result_sum}")
# Get 5 no from user, find max and min
num = []
for i in range(3):
    num.append(int(input(f"Enter number {i + 1}: ")))
    i+=1
    print(num)
max_num = max(num)  # Find the maximum number
min_num = min(num)  # Find the minimum number
print(f"Maximum number is: {str(max_num)}")  # Output: Maximum number
print(f"Minimum number is: {min_num}")  # Output: Minimum number
average_num = sum(num) / len(num)  # Calculate the average
print(f"Average of the numbers is: {average_num}")  # Output: Average
# Get no from user find square root, find sqrt of answer and add to previous sln
import math
num_3 = int(input("Enter a number to find its square root: "))
sqrt_num = math.sqrt(num_3)  # Find the square root of the number
print(f"Square root of {num_3} is: {sqrt_num}")
sqrt_sln = math.sqrt(sqrt_num)  # Find the square root of the previous solution
print(f"Square root of the previous solution is: {sqrt_sln}")
print(f"Final solution after adding both square roots is: {sqrt_num + sqrt_sln}")
# get float no from user and round
num_float = float(input("Enter a float number: "))
rounded_float = round(num_float, 2)  # Round the float number to 2decimal places
print(f"Rounded float number is: {rounded_float}")  # Output: Rounded float number