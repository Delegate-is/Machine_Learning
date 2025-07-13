# For loop in Python
for x in range(20, 50):
    print(x)
name = "Faisal Zamir"
for i in name:
    print(i)
list = [3,1,54,5,23,51]
for y in list:
    print(y)
for j in range(50, 0, -1):
    if j%2 != 0:
        print(j)
# Prompt the user to enter a number.
n1 = int(input("Enter a number: "))
# Print the multiplication table of the entered number from 1 to 10 using a for loop.
for a in range(11):
    print(n1 * a)

num = int(input("Enter a Number: "))
for b in range(10):
    mult = (b+1) * num
    print(str(num)+"\tx\t"+str(b+1)+"\t=\t"+str(mult))
list_odd = []
for n in range(50, 0, -1):
    if n%2 != 0:
        list_odd.append(n)
        print(list_odd)
total = sum(list_odd)
print(total)