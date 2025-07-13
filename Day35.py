i = 0
while i < 10:
    print(i)
    i += 1
j = 10
while j > 0:
    print(j)
    j -= 1
num = 10
while num <20:
    print("Python")
    num += 1
    
print("From 100 to 1")
n = 100
while n >= 1:
    if n%2 != 0:
        print(n)
    n -= 1
n = 1
print("From 1 to 100")
while n <= 100:
    if n%2 == 0:
        print(n)
    n += 1

list = []
x = 50
while x > 10:
    list.append(x)
    print(list)
    x -= 1
total = sum(list)
print(total)

# Prompt the user to enter a number.
n1 = int(input("Enter a number: "))
a = 1
while a <= 10:
    print(str(n1)+"\tx\t"+str(a)+"\t=\t"+str(n1*a))
    a += 1