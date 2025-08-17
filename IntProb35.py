import numpy as np

a1 = np.array([
    [1,2,3],
    [4,5,6]
])
a2 = np.array([
    [-1,-2,5],
    [8,10,-6]
])
print(a1)
print(a2)

add_array = np.add(a1,a2)  
print(add_array)
sub_array = np.subtract(a1,a2)
print(sub_array)
mul_array = np.multiply(a1,a2)
print(mul_array)
ar = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
new_ar = np.zeros_like(ar)
print(new_ar)

# Get num from user in array and find max
import numpy as np

numbers = np.array([int(input(f"Enter your number-{i+1}: ")) for i in range(5)])
print("Array:", numbers)
print("Maximum:", np.max(numbers))

char = input("Enter a char")# a e i o u or = ||
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print("It is vowel")
else:
    print("It is cons..")
    
user = input("Enter username ")
def check_user(u):
    if u.isalnum():
        print("Your Username "+str(u)+" is Okay")
    else:
        print("Sorry, use only alpha or numaric without whitespace")
check_user(user)

day = input("Enter name days: ").strip().lower()
if day == "sunday":
    print("Holiday")
else:
    print("Not holiday")