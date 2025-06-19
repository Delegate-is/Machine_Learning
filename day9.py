str1 = "LKJHGFDSSD(;';)LKJHGFDSXC"
str2 = """This is a multi-line string
that spans multiple lines"""
print(str1)
print(str2)

print("Number type")
a = 30
b = '30.3'
c = 3 + 67j
result = a + float(b)
print(result)
print(type(result))
print(type(a))
print(type(b))
print(type(c))
# type conversion
print("Type conversion")

list = [3,43,5,6,7,5,"Max"]
print(list)
print(type(list))
print(list[0])
print(list[1:4])
list[0] = "Jap"
print(list)

tuple = (3, 34, 5, 6, 7, 4, 'Jua', 89.3)
print(type(tuple))
print(tuple)
print(tuple[-2])
#tuple[4] = 10
print(tuple[4])

# Range function
print("Range function")
for i in range(10):
    print(str(i) + " *", end=" ")
    print("\n")

for i in range(1, 11, 1):
    print(i)
    for i in range(1, 20, 1):
        print(i)
print(type(range(1, 11, 1)))

        
# String Sequence types
print("String Sequence types")
str1 = "Hello, World!"
name = "Max Delegate"
print(name[0:3]) # slicings
print(str1[0])

for i in name:
    print(i)

# Create an empty list named my_list.
my_list = []
n1= int(input("Enter 1st number: "))
n2= int(input("Enter 2nd number: "))
n3= int(input("Enter 3rd number: "))
n4= int(input("Enter 4th number: "))
n5= int(input("Enter 5th number: "))
print("Input 5 numbers")
for i in range(5):
  num = int(input(f"Number {i+1} :"))
  my_list.append(num) # add to the list
# Prompt the user to enter five numbers and store them in the list.
my_list.append(n1)
my_list.append(n2)
my_list.append(n3)
my_list.append(n4)
my_list.append(n5)
print(my_list)
# Print the list.
# Find and print the following:
# The length of the list.
print(len(my_list))
# The sum of all the numbers in the list.
print(sum(my_list))
# The largest number in the list.
print(max(my_list))
# The smallest number in the list.
print(min(my_list))