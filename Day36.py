# display no table using while loop
a = int(input("Enter a number: "))
i = 1
while i <= 10:
    print(i)
    print(str(a)+"\t*\t"+str(i)+"\t=\t"+str(a*i))
    i+=1
    
# Get starting and ending number, starting < ending
start = int(input("Enter a starting number: "))
end = int(input("Enter a ending number: "))
if start < end:
    i = start
    while i<=end:
        print(i)
        i+=1
else:
    print("Starting number should be less than ending number")
    
numbers = []
squares = []
i = 0
while i <= 10:
    square = i * i
    numbers.append(i)
    squares.append(square)
    print(numbers)
    print(squares)
    i+=1
    
