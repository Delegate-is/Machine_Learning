# Get number from user and check it is divisible by 2 and 3
num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0:
    print(f"{num} is divisible by both 2 and 3")
else:
    print(f"{num} is not divisible by both 2 and 3. Not a required number.")
    
num2 = int(input("Enter a number: "))
if num2 % 5 == 0 and num2 % 6 == 0:
    print(f"{num2} is divisible by both 5 and 6")
else:
    print(f"{num2} is not divisible by both 5 and 6. Not a required number.")