# get 2 number, pass to function and get max
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
def max_num(a, b):
    if a > b:
        print("A is greater than B")
    else:
        print("B is greater than A")

max_num(a, b)
def min_num(a, b):
    if a < b:
        print("A is less than B")
    else:
        print("B is less than A")
min_num(a, b)
def sum_num(a, b):
    return a + b
def sub_num(a, b):
    return a - b

# Example: store the sum of a and b in result and print it
result = sum_num(a, b)
print(result)