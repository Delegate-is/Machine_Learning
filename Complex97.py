# match a-z, A-Z, 0-9 and _ and not ignore whitespace
import re
user_string = input("Enter a string: ")
x0 = re.search('\w+', user_string)
if x0:
    print("Matching....")
else:
    print("Not Matching....")

# match m char
import re
user_string = input("Enter a string: ")
x = re.search('m', user_string)
if x:
    print("Matching....")
else:
    print("Not Matching....")
    
# match a word containing 6 digits
import re
user_string1 = input("Enter a string: ")
x2 = re.search('\w{6}', user_string1)
if x2:
    print("Matching....")
else:
    print("Not Matching....")
    
# match a-z, A-Z, 0-9 and _ and ignore whitespace
import re
user_string2 = input("Enter a string: ")
x4 = re.search('\w+', user_string2)
if x4:
    print("Matching....")
else:
    print("Not Matching....")
    