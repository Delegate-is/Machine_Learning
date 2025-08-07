# Loop with Python List
language = ['Python', 'C', 'Java','R', 'React']
for i in language:
    print("Language is : " + i)
for i in range(10):
    i += 1
    print(i)
for i in range(10):
    if i %2 == 0:
        print(i)

# Get 5 word from user and display only words starting with b
list = []
for i in range(5):
    list.append(input(f"Enter  a word {i+1}: "))
    i += 1
    print(list)
for i in list:
    if i.startswith("b"):
        print(i)

# Get 10 no from user and display no <20 and>10
num = []
for i in range(10):
    num.append(int(input(f"Enter a number {i+1} :")))
    print(num)
for i in num:
    if i <= 20 and i >= 10:
        print(i)
num_1 = int(input(f"Enter a number: "))
for i in range(10):
    i += 1
    soln = num_1 * i
    print(f"Multiplication of:\t{i}\t*\t{num_1}\t=\t{soln}")