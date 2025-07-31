# ISALNUM - chec whether str is alpha numeric
str = "234343"
print(str.isalnum())  # True, all characters are alphanumeric
str = "234343a"
print(str.isalnum())  # True, all characters are alphanumeric
str = "234343a!"
print(str.isalnum())  # False, '!' is not alphanumeric
# ISALPHA - check whether str is alphabetic
str = "234343"  
print(str.isalpha())  # False, contains digits
str = "234343a"
print(str.isalpha())  # False, contains digits
str = "abcde"
print(str.isalpha())  # True, all characters are alphabetic
str = "abcde!"
print(str.isalpha())  # False, '!' is not alphabetic
# ISDIGIT - check whether str is digit
str = "234343"
print(str.isdigit())  # True, all characters are digits
str = "234343a"
print(str.isdigit())  # False, contains alphabetic character
str = "abcde"
print(str.isdigit())  # False, contains alphabetic characters
str = "12345"
print(str.isdigit())  # True, all characters are digits
# ISDECIMAL - check whether str is decimal
str = "234343"
print(str.isdecimal())  # True, all characters are decimal digits
str = "234343a"
print(str.isdecimal())  # False, contains alphabetic character
str = "abcde"
print(str.isdecimal())  # False, contains alphabetic characters
str = "12345"
print(str.isdecimal())  # True, all characters are decimal digits
# ISLOWER - check whether str is lower case
str = "234343"
print(str.islower())  # False, contains digits
str = "234343a"
print(str.islower())  # True, all characters are lower case
str = "abcde"
print(str.islower())  # True, all characters are lower case
str = "abcde!"
print(str.islower())  # True, all characters are lower case
str = "ABCDE"
print(str.islower())  # False, all characters are upper case
str = "abcde!"
print(str.islower())  # True, all characters are lower case
# ISUPPER - check whether str is upper case
str = "234343"
print(str.isupper())  # False, contains digits
str = "234343a"
print(str.isupper())  # False, contains lower case character
str = "abcde"
print(str.isupper())  # False, contains lower case characters
str = "ABCDE"
print(str.isupper())  # True, all characters are upper case
str = "ABCDE!"
print(str.isupper())  # True, all characters are upper case
str = "abcde!"
print(str.isupper())  # False, contains lower case character
# ISNUMERIC - check whether str is numeric, not a fraction
# Note: isdigit() and isdecimal() are more commonly used for numeric checks
str = "234343"
print(str.isnumeric())  # True, all characters are numeric
str = "234343a"
print(str.isnumeric())  # False, contains alphabetic character
str = "abcde"
print(str.isnumeric())  # False, contains alphabetic characters
str = "12345"
print(str.isnumeric())  # True, all characters are numeric
str = "123.45"
print(str.isnumeric())  # False, contains a decimal point
# ISSPACE - check whether str contains only whitespace characters
str = "234343"
print(str.isspace())  # False, contains digits
str = "   "
print(str.isspace())  # True, contains only whitespace characters
str = "234343a"
print(str.isspace())  # False, contains alphabetic character
str = "abcde"
print(str.isspace())  # False, contains alphabetic characters
str = "   abcde   "
print(str.isspace())  # False, contains alphabetic characters and whitespace
str = "   "
print(str.isspace())  # True, contains only whitespace characters
# ISPRINTABLE - check whether str is printable
str = "234343"
print(str.isprintable())  # True, all characters are printable
str = "234343a"
print(str.isprintable())  # True, all characters are printable
str = "abcde"
print(str.isprintable())  # True, all characters are printable
a = "\u0030" # Unicode for '0'
b = "\u00B2" # Unicode for subscript '²'
c = "\u2081" # Unicode for subscript '₁'
d = "\u00B9" # Unicode for subscript '¹'
e = "\u00BC" # Unicode for fraction '¼'
f = "\u00BD" # Unicode for fraction '½'
g = "\u2081" # Unicode for subscript '₁'
print(d.isdigit())  # True, '¹' is a digit
print(e.isdigit())  # False, '¼' is not a digit
print(f.isdigit())  # False, '½' is not a digit
print(f.isnumeric())  # True, '½' is numeric
print(f.isdecimal())  # False, '½' is not a decimal digit
print(a.isdigit())  # True, '0' is a digit
print(a.isnumeric())  # True, '0' is numeric
print(a.isdecimal())  # True, '0' is a decimal digit
print(a.isprintable())  # True, '0' is printable
print(a.isalnum())  # True, '0' is alphanumeric
# STARTSWITH - check whether str starts with a specific substring
str = "Hello, World!"
print(str.startswith("Hello"))  # True, starts with 'Hello'
print(str.startswith("World"))  # False, does not start with 'World'
print(str.startswith("Hello, World!"))  # True, starts with the full string
print(str.startswith("Hello, W"))  # True, starts with 'Hello, W'
print(str.startswith("Hello, World! "))  # False, does not start with 'Hello, World! '
print(str.startswith("Hello, World! ", 0, 13))  # True, starts with 'Hello, World!' in the specified range
print(str.startswith("Hello, World! ", 0, 12))  # False, does not start with 'Hello, World! ' in the specified range
# ENDSWITH - check whether str ends with a specific substring
str = "Hello, World!"
print(str.endswith("World!"))  # True, ends with 'World!'
print(str.endswith("Hello"))  # False, does not end with 'Hello'
print(str.endswith("Hello, World!"))  # True, ends with the full string
print(str.endswith("World! ", 0, 13))  # False, does not end with 'World! ' in the specified range
print(str.endswith("World!", 0, 12))  # True, ends with 'World!' in the specified range
print(str.endswith("!"))  # True, ends with '!'
print(str.endswith("! ", 0, 13))  # False, does not end with '! ' in the specified range
print(str.endswith("! ", 0, 12))  # False, does not end
# LOWER - convert str to lower case
str = "Hello, World!"
print(str.lower())  # "hello, world!"
# UPPER - convert str to upper case
str = "Hello, World!"
print(str.upper())  # "HELLO, WORLD!"
# TITLE - convert str to title case
str = "hello, world!"
print(str.title())  # "Hello, World!"
# CAPITALIZE - convert str to capitalized case
str = "hello, world!"
print(str.capitalize())  # "Hello, world!"