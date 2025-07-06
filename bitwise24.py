a= int(input("Enter first number: "))
b= int(input("Enter second number: "))
# Bitwise AND
bitwise_and = a & b  # 0100
# Bitwise OR
bitwise_or = a | b   # 1110
# Bitwise XOR
bitwise_xor = a ^ b  # 1010
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
