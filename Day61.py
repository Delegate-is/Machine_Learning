# Loop with Python Tuple
lang = ("Python", "Java", "C", "R")
for i in lang:
    print(i.upper())
tuo = (2,3,5,6,8,3,67,8,45)
#for i in tuo:
    #if i==3:
        #tuo[i]= 5
numbers = (1,2,3,4,5,6,7,8,9,10)
for i in numbers:
    sqr = i*i
    print(f"Square of {i} is {i} x {i} = {sqr}")   
tup_1 = []
for i in range(5):
    tup_1.append(int(input(f"Enter number {i+1}: ")))
    print(tup_1)
tuop = tuple(tup_1)
for i in tup_1:
    if i%2 == 0 and i%3 == 0:
        print(i)    
# iterate tuple to get only word ending with n
tup = []
for i in range(5):
    tup.append(input(f"Enter word {i+1}: "))
    print(tup)
tple = tuple(tup)
for i in tple:
    if i.endswith("n"):
        print(i)