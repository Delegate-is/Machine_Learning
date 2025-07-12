# Get no from user and display next and previous number
num = int(input("Enter a number: "))
pre_num = num - 1
next_num = num + 1
print("User Entered Number = "+str(num))
print("Previous Number = "+str(pre_num))
print("Next Number = "+str(next_num))

# Get two number from user, find square of 1st and cube of 2nd and add
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
Square = num1*num1
Cube = num2*num2*num2
Add = Square + Cube
print(str(Square)+" = square of 1st Number"+"\t\t"+str(Cube)+" = cube of 2nd Number"+"\t\t"+str(Add)+" = addition of Square and Cube")

# Get character from user and check if it is vowel
char = input("Enter a character: ")
if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
    print("It is a vowel")
else:
    print("It is not a vowwel")
    
# Get 6 subject marks to get total, average, percentage
list = []
for i in range(6):
    list.append(int(input("Enter marks: " + str({i+1}))))
    print(str(list))
total = sum(list)
ave = total / 6
per = (total * 100) / 600
print("The total is " + str(total))
print("The average is " + str(ave))
print("The percentage is " + str(per))

# Get short name of week and display full name
short_name = input("Enter a name of week: ")
if short_name == 'Mon' or short_name == 'mon':
    print("It is Monday")
elif short_name == 'Tue' or short_name == 'tue':
    print("It is Tuesday")
elif short_name == 'Wed' or short_name == 'wed':
    print("It is Wednesday")
elif short_name == 'Thur' or short_name == 'thur':
    print("It is Thursday")
elif short_name == 'Fri' or short_name == 'fri':
    print("It is Friday")
elif short_name == 'Sat' or short_name == 'sat':
    print("It is Saturday")
elif short_name == 'Sun' or short_name == 'sun':
    print("It is Sunday")
else:
    print("No Match")