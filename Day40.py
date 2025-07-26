# Find circle and square area
r = float(input("Enter a radius value: "))
pi = 3.14
area = pi*r*r
print("area of a circle = "+str(area))

l = float(input("Enter a length value: "))
w = float(input("Enter a width value: "))
area_square = l*w
print("area of square = "+str(area_square))

# get sentence from user and count total
s = input("Enter a sentence: ")
total_char = len(s)
print(total_char)
if total_char >= 11:
    print("VALID")
else:
    print("INVALID")
    
# Percentage calculator
total_ammount = float(input("Enter a total ammount: "))
percentage_required = float(input("Enter a how much percentage you need: "))
per = (total_ammount *percentage_required)/ 100
print("Total ammount = "+str(total_ammount))
print("Required percentage = "+str(percentage_required))
print("Percentage = "+str(per))

# Get user name = 8 / <20 and only alpha/ numeric data without white space or special chars
user_name = input("Enter username: ")
if user_name.isalnum() and (len(user_name) == 8 or len(user_name) < 20):
    print("User name "+str(user_name)+" is valid.")
else:
    print("Username is invalid")
    
def print_multiples(number, limit):
    for i in range(1, limit+1):
        mult = number * i
        print(mult)
        i += 1
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a Limit Value: "))
print("Multiples of "+str(n1)+" up to", str(n2))
print_multiples(n1,n2)