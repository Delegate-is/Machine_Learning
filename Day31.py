# elif statements in Python
day = input("Enter a day: ")
if day == "Sunday":
    print("Today is Sunday")
elif day == "Monday":
    print("Today is Monday")
elif day == "Tuesday":
    print("Today is Tuesday")
else:
    print("No Match")
print("\n")
num = int(input("Enter a number: "))
if num > 0:
    print("No is positive")
elif num < 0:
    print("No is negative")
else:
    print("No is equal to 0")

marks = int(input("Enter your marks: "))
if(marks > 90 and marks < 100):
    print("A Grade")
elif(marks > 80 and marks < 90):
    print("B Grade")
elif(marks > 70 and marks < 80):
    print("C Grade")
elif(marks > 60 and marks < 70):
    print("D Grade")
else:
    print("Fail")