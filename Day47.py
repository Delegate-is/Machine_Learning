# ISUPPER # check whether str is upper case
# str = "234343"
s = "234343"
print(s.isupper())  # False, contains digits
s = "234343a"
print(s.isupper())  # False, contains lower case character
s = "abcde"
print(s.isupper())  # False, contains lower case characters
s = "MAXi ahsgewal"
print(s.isupper())  # False, contains lower case character
s = "ABCDE"
print(s.isupper())  # True, all characters are upper case
# Strin method index() - find the index of a substring in a string
s = "Hello, world!"
print(s.index("world"))  # 7, index of the substring "world"
str = "maxi codeweb"
print(str.index("code"))  # 5, index of the substring "code"
# If the substring is not found, it raises a ValueError
try:
    print(s.index("Python"))  # Raises ValueError
except ValueError as e:
    print(f"Error: {e}")
print(str.index("m"))
# String method replace() - replace a substring with another substring
s = "Hello, world!"
print(s.replace("world", "Python"))  # "Hello, Python!"
str = "maxi codeweb"
print(str.replace("code", "web"))  # "maxi webweb"
# String method split() - split a string into a list of substrings
s = "Hello, world!"
print(s.split(", "))  # ['Hello', 'world!'] 
str = "maxi codeweb"
print(str.split(" "))  # ['maxi', 'codeweb']
# String method join() - join a list of strings into a single string
s_list = ['Hello', 'world!']
print(", ".join(s_list))  # "Hello, world!"
str_list = ['maxi', 'codeweb']
print(" ".join(str_list))  # "maxi codeweb"
# String method title() - convert a string to title case
s = "hello, world!"
print(s.title())  # "Hello, World!"
str = "maxi codeweb"
print(str.title())  # "Maxi Codeweb"
# String method isspace() - check whether a string contains only whitespace characters
s = "   "
print(s.isspace())  # True, contains only whitespace characters 
str = "   abcde   "
print(str.isspace())  # False, contains alphabetic characters and whitespace
str_2 = input("Enter a string: ")
print(len(str_2))  # Print the length of the input string
print(str_2.title())  # Convert the input string to title case
print(str_2.index(str_2[0]))  # Find the index of the first character in the input string
if str_2.endswith("!"):
    print(str_2 + " is a great string!")  # If the input string ends with '!', print a message
else:
    print(str_2 + " is not a great string!")