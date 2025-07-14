# Functions in Python
def fun_name():
    print("I am inside the function")
fun_name()
def test(a, name, b=3):
    print(a + b)
    print("Hello,", name)

name = input("Enter your name: ")
test(2, name)

# Get 3 no and find greatest number
def find_great():
    n1 = int(input("Enter 1st num"))
    n2 = int(input("Enter 2nd num"))
    n3 = int(input("Enter 3rd num"))
    if n1 > n2 and n1 > n3:
        largest = n1
        print("largest number is the "+str(largest))
    elif n2 > n1 and n2 > n3:
        largest = n2
        print("largest number is the "+str(largest))
    else:
        print("largest number is the "+str(n3))
find_great()

# get no from user, send to function as parameter and find table in reverse mode
def table(num):
    print("Table of number")
    # 4 * 10 = 40
    #
    for i in range(10,0,-1):
        print(str(num)+" * "+str(i)+" = "+str(num*i))
    
x = int(input("Enter a number"))
table(x)

def calculate_area(length, width):
    print("area = "  + str(length * width))
length = int(input("Enter rectangle length: "))
width = int(input("Enter rectangle width: "))
calculate_area(length, width)