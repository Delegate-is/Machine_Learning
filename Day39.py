#Parameters in Python Function
def fun(par):
    print(par)
fun(65)

def full_name(f_name, l_name):
    print(f_name, l_name)
# Arguments in Python - Keyword Argument, Default Argument and Required Argument
f_name = "Max"
l_name = "Dee"
full_name("Max", "Dee")

# Keyword argument
def show(name, num):
    print("name = "+name)
    print("num = "+str(num))
show(name ="Max", num =345)

def check_even_odd(number):
    if number % 2 == 0:
        print(str(number)+" is Even")
    else:
        print(str(number)+" is Odd")
number = int(input("Enter a number: "))
check_even_odd(number)

# Default Argument in Python
def fullname(fname, lname = "Dee"):
    print(fname, lname)
# Arguments in Python - Keyword Argument, Default Argument and Required Argument
f_name = "Max"
fullname("Max", "Jap")

# Required Argument in Python
def show_value(a, b, c):
    print("a = "+ str(a))
    print("b = "+ str(b))
    print("c = "+ str(c))
show_value(3,5,1)

def add_num(num1, num2= 34):
    print(num1 + num2)
add_num(2)