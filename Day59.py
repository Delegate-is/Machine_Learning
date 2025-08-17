# Tuple == Immutable data type
tup = (3,) * 5# use a comma at the end of single item
land = ("private", "public", "leasehold", "freehold")
print(type(tup))
print(land)
tuo_1 = tup + land
print(tuo_1)
print(3 in tuo_1)
for i in tup:
    print(i)
# Tuple Access Methods
# index number
print(land[-1])
# We  cannot change tuple items-- tup[3] ="New Value"(get error)
# land[-1] = "join"
t = ("sea",)
t_1 =land + t
print(t_1)
# Store in tuple
student = []
for i in range(5):
    student.append(input(f"Enter a name {i+1}: "))
    print(student)
tuple_std = tuple(student)
print(tuple_std)
for i in tuple_std:
    print(i.upper())
# Odd No
num = []
for i in range(5):
    num.append(int(input(f"Enter a number {i+1}: ")))
    print(num)
tuple_num = tuple(num)
print(tuple_num)
for i in tuple_num:
    if i%2 != 0:
        print(i)

colors = ("Red", "Green", "Blue", "Yellow", "Orange")
print(colors)
for i in colors:
    if n in colors:
        print(n)
n = input("Enter color to check: ")