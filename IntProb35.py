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