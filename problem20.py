# Get 5 Number from a User and store numbers in an Array and GET SUM
import array as arr
a= arr.array('i' , [])
s = 0
for i in range (5):
    a.append(int(input("Enter a number: ")))
for j in range(5):
    print(a[j])
    s += a[j]
print(f"Sum of the number: {s}")
# Find Maximum no from array
x = max(a)
y = min(a)
print(f"Maximum number is {str(x)}")
print(f"Manimum number is {str(y)}")