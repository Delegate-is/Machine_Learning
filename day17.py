# Arithmetic Operators (+/-*%)
a = 4
b = 12
print(a+b)
print(a*b)
print(a % b, "\t", a / b)

# Exercise
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))
print(f"Modulus: {num1 % num2}\tDivision: {num1 / num2}\tMultiplication: {num1 * num2}")
print(num1 + num2, "\t", num1 - num2)
num3 = int(input("Enter a number: "))
num4 = int(input("Enter a number: "))
num5 = int(input("Enter a number: "))
num6 = int(input("Enter a number: "))
r1 = num3-num4
r2 = num5+num6
print(r1*r2)

# Create three variables num1, num2, and num3 with values 10, 5, and 3 respectively.
num1 = 10
num2 = 5
num3 = 3
# Addition: Add num1 and num2 and then add num3 to the result. Store the final result in a variable named add_result.
add_result = num1+num2+num3
# Subtraction: Subtract num2 from num1 and then subtract num3 from the result. Store the final result in a variable named sub_result.
sub_result =(num1-num2)-num3
# Multiplication: Multiply num1 by num2 and then multiply the result by num3. Store the final result in a variable named mul_result.
mul_result=num1*num2*num3
# Division: Divide num1 by num2 and then divide the result by num3. Store the final result in a variable named div_result.
div_result=(num1/num2)/num3
# Exponentiation: Raise num1 to the power of num2 and then raise the result to the power of num3. Store the final result in a variable named exp_result.
exp_result = (num1**num2)**num3
print(f"Add: {add_result}")
print(f"Subtraction: {sub_result}")
print(f"Multiplication: {mul_result}")
print(f"Division: {div_result}")
print(f"exponentiation: {exp_result}")