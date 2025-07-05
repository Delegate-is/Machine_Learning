x = 24
x += 10 # x = x + 10, 10+24=34
print(x)
x -= 5 # x = x - 5, 34-5=29
print(x)
x *= 2 # x =x * 2, 29*2=58
print(x)
x %= 3 # x = x % 3, 58%3=1
print(x)
x //= 2 # x = x // 2, 1//2=0
print(x)
"""Assignment Operators in Python
    Get a number from user and increase one value to that number
    and decrease one value to that number
"""
num1 = int(input("Enter a number: "))
num1 += 1 #Increment by 1 value
print(f"Incremented value is :{num1}")
num1 -= 1 #Decrement by 1 value
print("Decremented value is :"+ str(num1))

# Create a variable num with an initial value of 10
num =10
# Add 5 to num using the += operator
num += 5
print(f"After adding 5, num is: {num}")
# Subtract 3 from num using the -= operator.
num -= 3
print(f"After subtracting 3, num is: {num}")
# Multiply num by 2 using the *= operator.
num *= 2
print(f"After multiplying by 2, num is: {num}")
# Divide num by 4 using the /= operator.
num /= 4
print("After dividing 4, num is:", num)
# Raise num to the power of 3 using the **= operator.
num **= 3
print("After raising to power 3, num is:", num)