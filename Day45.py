# Get sent from user convert into uppercase and add fullstop
sent = input("Enter a sentence:")
print(sent.upper() + ".")
total_chars = len(sent)
# Count the number of characters in the sentence
print("Total characters in the sentence:", total_chars)
if sent.isupper():
    print("The sentence is in uppercase.")
else:
    print("The sentence is not in uppercase.")
    print(sent.upper() + ".")
    
# get a numeric string from user
num = input("Enter a numeric string: ")
# Check if the string is numeric
if num.isnumeric():
    print("The string is numeric.")
else:
    print("The string is not numeric.")
    print("Please enter a valid numeric string.")

# Get name from user starting with 'a'
name = input("Enter a name starting with 'a': ")
if name.startswith('a') or name.startswith('A') and name.endswith('n'):
    print("The name starts with 'a' and ends with 'n'= "+str(name))
else:
    print("The name does not start with 'a' and end with 'n'.")
    print("Please enter a name that starts with 'a'.")
    
# Get a string and display char present on odd index 
def odd_index_chars(s):
    return ''.join([s[i] for i in range(len(s)) if i % 2 != 0])
s = input("Enter a string: ")
odd_chars = odd_index_chars(s)
print("Characters at odd indices:", odd_chars)

j = (input("Enter a sentence: "))
total_char = len(j)
for n in range(0, total_char):
    if n % 2 == 0:
        print(j[n], end="")

"""list= [a, b]
a = int(input("Enter first element: "))
b = int(input("Enter second element: "))
list.sum = a + b
print("Sum of the elements in the list:", sum(list))
list.product = a * b
print("Product of the elements in the list:", a * b)
list.difference = a - b
print("Difference of the elements in the list:", a - b)
list.quotient = a / b
print("Quotient of the elements in the list:", a / b)
"""
# Input 2 numbers separated by space and display the sum, product, difference, and quotient
def calculate_operations(a, b):
    return {
        'sum': a + b,
        'product': a * b,
        'difference': a - b,
        'quotient': a / b if b != 0 else 'undefined (division by zero)'
    }
a, b = map(int, input("Enter two numbers separated by space: ").split())
operations = calculate_operations(a, b)
print("Sum:", operations['sum'])
print("Product:", operations['product'])
print("Difference:", operations['difference'])
print("Quotient:", operations['quotient'])
