# Program to check a-z, A-Z, 0-9 & _ from user string at start
import re
# ^ maens at start
# . means any char
# * 0 or many
# $ means at end
# \w means a-z, A-Z, 0-9 and _

user_string = input("Enter a string: ")
x = re.search('^\w+', user_string)

if x:
    print("Matching....")
else:
    print("Not Matching....")
    

import re

s = input("Enter a string: ")

# Regex pattern: string must end with a-z, A-Z, 0-9, or underscore
pattern = r"[a-zA-Z0-9_]$"

if re.search(pattern, s):
    print("Matching: The string ends with a-z, A-Z, 0-9, or _")
else:
    print("Not Matching")
