# Get word from user, convert upper to lower and lower to upper
import re
word = input("Enter a word: ")
print(f"Original word: {word}")
re.search("[a-z]+[A-Z]", word)  # Check if there are lowercase letters
list = []
if word:
    for i in word:
        if i.isupper():
            new_word = i.lower()
            list.append(new_word)
        elif i.islower():
            new_word = i.upper()
            list.append(new_word)
    print("Okey, both upper and lower case letters are present.")
else:   
    print("No, both upper and lower case letters are not present.")
print(list)
word_1 = ''.join(list)
print(f"Converted word: {word_1}")

num = int(input("Enter a number: "))
for i in range(0, num + 1):
    print(i, end=' ')