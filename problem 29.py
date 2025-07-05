# Get nummber from user and chech whether negative or positive
num = int(input("Enter a number: "))
if num> 0:
    print(str(num) + " is a positive number")
elif num < 0:
    print(str(num) + " is a negative number")
else:
    print("The number is zero")

std_name = ("Juma", "Abdi", "Ali", "Asha", "Fatuma")
print(type(std_name))  # Output: <class 'tuple'>
print(std_name[0])  # Output: Juma
name = input("Enter your name: ")
if name in std_name:
    print(f"{name} is in the list of students.")
else:
    print(f"{name} is not in the list of students.")
    