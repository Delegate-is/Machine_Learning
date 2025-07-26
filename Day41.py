# Return statement in Python
def show():
    a = 32
    b = 12
    return(a+b)
    # print("Cannot execute- gives error")
print(show())

def show_name():
    name = input("Enter your name")
    return name

user_name = show_name()
print(user_name)

# Python Pass Keyword
a = 30
if a > 30:
    pass
def show():
    pass
show()
for i in range(1,10):
    pass

# Python Variable Scope
# Local Scope and Global Scope
name = "Max"
def test():
    print("How are you")
    x = 10
    print(x)
    print(name)
test()

a =30
x = 10
if a > 30:
    b = a
    print(x)
print(x)

def check_even_odd(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
number = int(input("Enter a number: "))
print(check_even_odd(number))
