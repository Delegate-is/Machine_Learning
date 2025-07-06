# Bitise operators
a = 10  # 1010
b = 4   # 0100
# Bitwise AND
bitwise_and = a & b  # 0000
# Bitwise OR
bitwise_or = a | b   # 1110
# Bitwise XOR
bitwise_xor = a ^ b  # 1110
# Bitwise NOT
bitwise_not_a = ~a  # 0101
bitwise_not_b = ~b  # 1011
# Bitwise left shift
bitwise_left_shift_a = a << 2  # 101000
bitwise_left_shift_b = b << 2  # 10000
# Bitwise right shift
bitwise_right_shift_a = a >> 2  # 0010
bitwise_right_shift_b = b >> 2  # 0001
# Print results
print(f"Bitwise AND: {bitwise_and}")
print(f"Bitwise OR: {bitwise_or}")
print(f"Bitwise XOR: {bitwise_xor}")
print(f"Bitwise NOT of A: {bitwise_not_a}")
print(f"Bitwise NOT of B: {bitwise_not_b}")
print(f"Bitwise left shift A: {bitwise_left_shift_a}")
print(f"Bitwise left shift B: {bitwise_left_shift_b}")
print(f"Bitwise right shift A: {bitwise_right_shift_a}")
print(f"Bitwise right shift B: {bitwise_right_shift_b}")
# Note: The above code is a simple demonstration of bitwise operations in Python.
# It does not include any user input or error handling for simplicity.
d = 20
d <<= 2  # Left shift d by 2 bits
print(f"Value of d after left shift: {d}")  # Should print 80
# Bitwise operations on a list of numbers
numbers = [10, 20, 30, 40]
# Perform bitwise AND with 5 on each number in the list
bitwise_and_list = [num & 5 for num in numbers]
# Perform bitwise OR with 5 on each number in the list
bitwise_or_list = [num | 5 for num in numbers]
# Perform bitwise XOR with 5 on each number in the list
bitwise_xor_list = [num ^ 5 for num in numbers]
# Perform bitwise NOT on each number in the list
bitwise_not_list = [~num for num in numbers]
# Perform bitwise left shift by 1 on each number in the list
bitwise_left_shift_list = [num << 1 for num in numbers]
# Perform bitwise right shift by 1 on each number in the list
bitwise_right_shift_list = [num >> 1 for num in numbers]
# Print results
print("Bitwise AND with 5:", bitwise_and_list)
print("Bitwise OR with 5:", bitwise_or_list)
print("Bitwise XOR with 5:", bitwise_xor_list)

# Create two variables num1 and num2 with values 10 and 5 respectively.
num1 = 10
num2 = 5
# Bitwise AND
and_result = num1 & num2
# Bitwise OR
or_result = num1 | num2
# Bitwise XOR
xor_result = num1 ^ num2
# Bitwise NOT
not_num1 = ~num1
# Print the results of all the operations
print(f"Bitwise AND of num1 and num2: {and_result}")
print(f"Bitwise OR of num1 and num2: {or_result}")
print(f"Bitwise XOR of num1 and num2: {xor_result}")
print(f"Bitwise NOT of num1: {not_num1}")