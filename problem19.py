"""Program From User to Get 3 Number and put in Equation:
    a+b+ca/b(2a + 3b)"""
# for i in range(3):
a=int(input("Enter a number: "))
b=int(input("Enter b number: "))
c=int(input("Enter c number: "))

result = (a+b+c)*(a/b)*(2*a+3*b)
print("Result is = "+ str(result))

# Assgn
d=int(input("Enter d number: "))
e=int(input("Enter e number: "))
f=int(input("Enter f number: "))
g=int(input("Enter g number: "))
result1 = g+d+((2*d*e)/g)*(4*f+10)
print("Result is = "+ str(result1))