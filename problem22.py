# Program to check Alpha Character, whether Vowel or Consonant
"""Get character(a,e,i,o,u) from user
Check character using decision making structure(if)
Display vowel(a,e,i,o,u), else consonant"""
char = input("Enter a character: ")
# if(char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
if char in ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'):
    print("It is a vowel")
elif char.isalpha():
    print("It is a consonant")
else:
    print("It is a number")
"""elif(char == 'e'):
    print("It is a vowel")
elif(char == 'i'):
    print("It is a vowel")
elif(char == 'o'):
    print("It is a vowel")
elif(char == 'u'):
    print("It is a vowel")"""
