import math

name = input("Enter your name: ")
age = int(input("Enter your age: "))

nm = float(input("Enter number to find sqrt: "))

try:
    print("name"+age)
except TypeError:
    print("You are concatenating two different data types, int and string")

try:
    sq = math.sqrt(nm)
    print("Square root of "+str(nm)+" is "+str(sq))

except ValueError:
    print("There is an issue with value you are passing")

else:
    print("There is no error")
finally:
    print("Code is completed")