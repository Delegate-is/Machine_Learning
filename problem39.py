# Program to get 5 no from user, store in list, pass in function to get * and +
num_list = []
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    num_list.append(num)  # Append the number to the list
    print(f"Number {i + 1} is: {num}")  # Display the entered number
    print(num_list)
def multiply_and_add(num_list):
    s = 0
    m = 1
    for i in num_list:
        s += i
        m *= i
        print(f"Sum of numbers is: {str(s)}")
        print(f"Multiplication of numbers is: {str(m)}")
multiply_and_add(num_list)

num_tuple = ()
for i in range(5):
    num = int(input(f"Enter number {i + 1}: "))
    num_tuple += (num,)  # Append the number to the tuple
    print(f"Number {i + 1} is: {num}")  # Display the entered number
    print(num_tuple)
def multiply_and_add(num_tuple):
    s = 0
    m = 1
    for i in num_tuple:
        s += i
        m *= i
        print(f"Sum of numbers is: {str(s)}")
        print(f"Multiplication of numbers is: {str(m)}")
multiply_and_add(num_tuple)