# Type Method in Python
a = 20
print(type(20))
b = 3.4
c = "Max Delegate"
L = [1,2,34,4,5,6]
print(type(b))
print(type(c))
print(type(L))
d = '2+3'
print(type(d))
e = 4.5
print(type(e))
f = (3,4,5,6,7,9)
print(type(f))

"""Type Conversion in Python
    Two types of conversion:
    Implicit and explicit conversion."""
# Implicit conversion
v1 = 3
print(type(v1))
v1 = v1 + 3.3
print(type(v1))
#print("Faisal"+ 3234)#String cannot concatenate with int

# Explicit Conversion
str1 = '32'
print(type(str))
c_str1 = int(str1)#Conversion to integer
print(type(c_str1))
v1 = '32'
print(type(v1))
#v2 = v1 + 8 #Error: can only concatenate str
v2 = int(v1) + 8
print(v2)
v3 = 33.1
print(type(v3))
v4 = int(v3)
print(type(v4))
print(v4)
print("\n \n")
# Define two variables num1 and num2 with values 10 and 20 respectively.
num1 = 10
num2 = 20
# Implicit conversion: Add num1 and num2 and store the result in a variable named result_implicit.
print(type(num1))
print(type(num2))
result_implicit = num1 + num2
print(type(result_implicit))
print(result_implicit)
print("\n")
# Explicit conversion: Convert num1 to a string and concatenate it with the string " + " and then with num2 converted to a string. Store the result in a variable named result_explicit.
num1 = 10
num2 = 20
print(type(num1))
print(type(num2))
result_explicit = str(num1) + " + " + str(num2)
print(type(result_explicit))
print(result_explicit)
print("\n \n")
# Concatenate integer and string
#print('value'+123) :Type error
print('value'+" "+str(123))
v1 = 100
v2 = 'Age'
print(str(v1)+" "+v2)
print("\n")
print("Reasons why Python is considered Great.")

print("Easy to read and write.")

print("Python has a robust community")

print("Python has many libraries to use in various scenarios such as web development and AI")

print("Python is easy to use since it require small code chunks to run a program")

print("Python has a less complex syntax that allows creation of robust programs efficiently and in less time") 


