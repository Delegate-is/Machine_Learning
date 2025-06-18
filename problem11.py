print("Finding Maximum number")
n1= int(input("Enter First Number: "))
n2= int(input("Enter Second Number: "))
if n1 > n2:
    print(f"{n1} is greater than {n2}")
elif n2> n1:
    print(f"{n2} is greater than {n1}")

print((max(n1,n2)))

print("Finding Maximum number")
n1= int(input("Enter First Number: "))
n2= int(input("Enter Second Number: "))
n3= int(input("Enter Third Number: "))

if n1 > n2 and n1 > n3:
    print(f"{n1} is the greatest among {n2} and {n3}")
    
elif n2 > n1 and n2 > n3:
    print(f"{n2} is greatest among {n1} and {n3}")
elif n3 > n1 and n3 > n2:
    print(f"The third number: {n3}, is greatest among the second: {n1}, and the third: {n2}")
    

print((max(n1,n2,n3)))
