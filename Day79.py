# Python string Formmatting -- way of  inserting custom string / variable in a string
name = "Juma"
age = 20
# print("My name is " + name + " and I am " + str(age) + " years old")
# print("My name is {} and I am {} years old".format(name, age))
print(f"My name is {name} and I am {age} years old")
# Python f string -- way of inserting custom string / variable in a string
# f string is faster than format method and concatenation method
# f string is available in python 3.6 and above
# f string is more readable than format method and concatenation method
# f string is more efficient than format method and concatenation method
# f string is more flexible than format method and concatenation method
# f string is more powerful than format method and concatenation method
# f string is more concise than format method and concatenation method
# f string is more elegant than format method and concatenation method
# f string is more pythonic than format method and concatenation method
# f string is more modern than format method and concatenation method
# f string is more versatile than format method and concatenation method
# f string is more dynamic than format method and concatenation method
# f string is more expressive than format method and concatenation method
# f string is more intuitive than format method and concatenation method
# f string is more user-friendly than format method and concatenation method
# f string is more developer-friendly than format method and concatenation method

# Formatting with % operator ---oldest way
print("My name is %s and I am %d years old" % (name, age))
# %s is for string
# %d is for integer
# %f is for float
print("My name is %s and I am %.2f years old" % (name, 20.5))
# %.2f is for float with 2 decimal places
# %x is for hexadecimal
print("My name is %s and I am %x years old" % (name, age))
# %o is for octal
print("My name is %s and I am %o years old" % (name, age))
# %e is for scientific notation
print("My name is %s and I am %e years old" % (name, age))
# %c is for character
print("My name is %s and I am %c years old" % (name, age))
# %r is for raw string
print("My name is %s and I am %r years old" % (name, age))
# %a is for ascii string
print("My name is %s and I am %a years old" % (name, age))
# %b is for binary
#print("My name is %s and I am %b years old" % (name, age))
# %u is for unsigned integer
print("My name is %s and I am %u years old" % (name, age))
# %g is for general format
print("My name is %s and I am %g years old" % (name, age))
# %p is for pointer
#print("My name is %s and I am %p years old" % (name, age))


# Formatting with format{} method -- Python 3
print("My name is {} and I am {} years old".format(name, age))
# {} is a placeholder
# {0} is for first argument
print("My name is {0} and I am {1} years old".format(name, age))
# {1} is for second argument   {{{POSITIONAL ARGUMENT}}}
print("My name is {1} and I am {0} years old".format(age, name))
# {name} is for named argument
print("My name is {name} and I am {age} years old".format(name="Ali", age=23))
# {age} is for named argument --{{{KEYWORD ARGUMENT}}}


# Formatting with Template class method -- Python 3
# we have to use the $ sign to indicate a placeholder
from string import Template
t = Template("My name is $name and I am $age years old")
print(t.substitute(name=name, age=age))
# $name is a placeholder
# $age is a placeholder
# ${name} is for named argument
t = Template("My name is ${name} and I am ${age} years old")
print(t.substitute(name="Alooo", age=80))
# ${age} is for named argument --{{{KEYWORD ARGUMENT}}}
# Template class is not as powerful as format method and f string
# Template class is not as flexible as format method and f string
# Template class is not as efficient as format method and f string
# Template class is not as readable as format method and f string
# Template class is not as concise as format method and f string
# Template class is not as elegant as format method and f string
# Template class is not as pythonic as format method and f string
# Template class is not as modern as format method and f string
# Template class is not as versatile as format method and f string
# Template class is not as dynamic as format method and f string

# Prob 1 == 1st name, last name and email
first_name = input("Enter your first name: ")
last_name = input("Enter your last name: ")
email = input("Enter your email: ")
temp_obj = Template("Your first name is $first_name and last name $last_name. Your email is $email")
print(temp_obj.substitute(first_name=first_name, last_name=last_name, email=email))
print("Your first name is {first_name} and last name {last_name}. Your email is {email}".format(first_name=first_name, last_name=last_name, email=email))

# Get 3 subject marks
math = int(input("Enter your math marks: "))
eng = int(input("Enter your english marks: "))
kis = int(input("Enter your kiswahili marks: "))
print(f"Your math marks is {math}, english marks is {eng} and kiswahili marks is {kis}. Your total marks is {math + eng + kis} and your average marks is {(math + eng + kis) / 3}")#using f string
print("Your math marks is {}, english marks is {} and kiswahili marks is {}. Your total marks is {} and your average marks is {}".format(math, eng, kis, math + eng + kis, (math + eng + kis) / 3))#using format method
#using % operator
print("Your math marks is %d, english marks is %d and kiswahili marks is %d. Your total marks is %d and your average marks is %.2f" % (math, eng, kis, math + eng + kis, (math + eng + kis) / 3))#using % operator

def format_name(first_name, last_name):
    return f"Your first name is {first_name} and last name {last_name}"
print(format_name("Juma", "Kipkemoi"))
print(format_name("Alooo", "Kipkemoi"))

# Get the string from the user
user_string = input("Enter a string: ")

# Get the required character from the user
required_char = input("Enter the character to find at odd index positions: ")

# Initialize a list to store found characters at odd indexes
found_chars = []

# Loop through the string at odd index positions
for i in range(1, len(user_string), 2):
    if user_string[i] == required_char:
        found_chars.append(user_string[i])

# Display the result
if found_chars:
    print(f"Character '{required_char}' found at odd index positions in the string.")
else:
    print(f"Character '{required_char}' NOT found at odd index positions in the string.")
