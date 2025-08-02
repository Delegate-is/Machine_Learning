# Lambda Function in Python
test = lambda x: x +1
print(test(3))
test_1 = lambda x, y: x + y
print(test_1(3, 5))
show_name = lambda name: print("Hi,"+name)
show_name("Max")
# Get first name and last name and display full using lambda
f_name = input("Enter your first_name: ")
l_name = input("Enter your last_name: ")

show_fullname = lambda f_name, l_name: print("Hi,"+ f_name +" "+ l_name)
show_fullname(f_name, l_name)

# Get 3 no from user and add usin lambda
a = int(input("Enter a number: "))
b = int(input("Enter b number: "))
c = int(input("Enter c number: "))
add = lambda a, b , c: a+b+c
print(add(a,b,c))

x = int(input("Enter a number: "))
square = lambda x: x * x
print(square(x))
# Enter 3 numbers seperated by space and find the largest number and smallest plus average
numbers = input("Enter three numbers separated by space: ")
numbers_list = list(map(int, numbers.split()))
largest = max(numbers_list)
smallest = min(numbers_list)
total = sum(numbers_list)
average = total / len(numbers_list)
print(f"Largest: {largest}, Smallest: {smallest}, Average: {average}")
num = input("Enter 3 numbers seperated by a space: ")
num1_str, num2_str, num3_str = num.split()
num1 = float(num1_str)
num2 = float(num2_str)
num3 = float(num3_str)
ave = (num1 + num2 + num3) / 3

print(f"Average of 3 numbes: {ave}")
print(min(num1, num2, num3))
print(max(num1, num2, num3))