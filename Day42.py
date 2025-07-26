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