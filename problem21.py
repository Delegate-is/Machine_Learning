# Get 5 Number from a User and store numbers in an Array and GET SUM
import array as arr
a= arr.array('i' , [])
s = 0
for i in range (5):
    a.append(int(input("Enter a number: ")))
x = a[0]
y = a[0]
for j in range(5):
    print(a[j])
    s += a[j]
    if (a[j] > x):
        x = a[j]
    else:
        if a[j] < y:
            y = a[j]
print(f"Sum of the number: {s}")
# Find Maximum no from array
# x = max(a) ; One way
print(f"Maximum number is {str(x)}")
print(f"Manimum number is {str(y)}")