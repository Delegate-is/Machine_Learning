# Using input and output in Python
print("Hi, How are you?")
    
name = input("Enter your name: ")
name2 = input("Enter your last name: ")
n1 = input("Enter your phone nember: ")
n2 = input("Enter your email: ")
n3 = input("Enter a number: ")
n4 = input("Enter another number: ")
n5 = int(input("Enter a number to minus: "))
n6 = int(input("Enter another number: "))
result = (n5 - n6)

print(f"Hello, {name}!")
print("Hello my full name is " + name + " " + name2)
print(f"Your phone number is {n1}")
print(f"Your email is {n2}")
print(f"{int(n3)} + {int(n4)} = {int(n3) + int(n4)}")
print("Answer of minus is: " + str(result))
print("\nThank You")