marks = int(input("Enter your marks: "))
if marks > 70:
    print("You have an A my bro.")
else:
    print("Well there is always room for improvement.")
    
number = int(input("Enter a number: "))
if number % 2 == 0:
    print(str(number) + " : It is even.")
else:
    print(str(number) + " : It is odd.")
    
name = input("Enter your name: ")
age_1 = int(input("Enter your age: "))
if age_1 > 18:
    print(f"Your name is {name} and your {age_1} years old.")
else:
    print("Error Occurred")
    
number = int(input("Enter a number: "))
if number > 0:
    print(str(number) + " : It is positive.")
elif number < 0:
    print(str(number) + " : It is negative.")
else:
    print("Number is zero")