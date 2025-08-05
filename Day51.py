import math
# No built in method power: pow()
result = pow(9, 3)  # Output: 27
print(result)
# Custom implementation of pow() function
def custom_pow(base, exponent):
    result = 1
    for _ in range(exponent):
        result *= base
    return result
print(custom_pow(3, 3))  # Output: 27
# No built in method exponentiation: exp()
# Custom implementation of exp() function
def custom_exp(x):
    result = 1.0
    term = 1.0
    n = 1
    while n < 100:  # Limit to 100 terms for convergence
        term *= x / n
        result += term
        n += 1
    return result
print(custom_exp(1))  # Output: 2.718281828459045 (approximation of e)
num = 4
result = math.exp(num)  # Output: 54.598150033144236
print(result)
print(pow(2.71828, 4))
# Number built in method max()
list_1 = [[1, 2, 3], [4, 5], [6, 7, 8, 9], ["Max", "Codeweb"], [True, False]]
max_list = max(list_1, key=len)  # Find the longest list
print(f"The longest list is: {max_list}")  # Output: [6, 7, 8, 9]
# Number built in method min()
min_list = min(list_1, key=len)  # Find the shortest list
print(f"The shortest list is: {min_list}")  # Output: [4, 5]
# Number built in method round()
number = 3.14159
rounded_number = round(number, 2)  # Round to 2 decimal places
print(f"Rounded number: {rounded_number}")  # Output: 3.14
# Number built in method sqrt()
sqrt_value = math.sqrt(16)  # Output: 4.0
print(f"Square root of 16 is: {sqrt_value}")  # Output: 4.0
# Number built in method choice()
import random
list_2 = [1, 2, 3, 4, 5]
random_choice = random.choice(list_2)  # Randomly select an element from the list
print(f"Random choice from the list: {random_choice}")  # Output: Random element from list_2
# Number built in method randrange()
random_range = random.randrange(1, 10, 3)  # Randomly select a number between
# 1 and 10 (exclusive of 10)
print(f"Random number from range 1 to 10: {random_range}")  # Output: Random number from range 1 to 10
# Number built in method random()
random_number = random.random()  # Generate a random float between 0.0 and 1.0
print(f"Random float between 0.0 and 1.0: {random_number}")  # Output: Random float between 0.0 and 1.0

nom = int(input("Enter a number: "))
print(abs(nom))  # Output: Absolute value of the number
print(math.sqrt(nom))  # Output: Square root of the number
# Get floor value of a number
print(math.floor(nom))  # Output: Floor value of the number
# Get ceiling value of a number
print(math.ceil(nom))  # Output: Ceiling value of the number
nom = int(input("Enter a number: "))
print(abs(nom))  # Output: Absolute value of the number
print(math.sqrt(nom))  # Output: Square root of the number
# Get floor value of a number
print(math.floor(nom))  # Output: Floor value of the number
# Get ceiling value of a number
print(math.ceil(nom))  # Output: Ceiling value of the number
# Number built in method shuffle()
list_3 = [1, 2, 3, 4, 5]
random.shuffle(list_3)  # Shuffle the list in place
print(f"Shuffled list: {list_3}")  # Output: Shuffled version