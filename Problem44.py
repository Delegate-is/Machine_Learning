# Get largest and lowest number from user, display largest to lowest
s = int(input("Enter a larger starting number: "))#10
e = int(input("Enter a lower ending number: "))#5
numbers = []
for i in range(s, e-1, -1):
    print(i)
    numbers.append(i)
total = sum(numbers)
print(total)