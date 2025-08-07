# Python list Comprehension= creating new list from given list
# Without Comprehension 
language = ['Python', 'C', 'Java','R', 'React']
print(language)
new_lang = []
for i in language:
    if "P" in i:
        new_lang.append(i)
    print(new_lang)
# With Comprehension
language = ['Python', 'C', 'Java','R', 'React']
print(language)
new_lang = [i for i in language if "a" in i]
print(new_lang)
# What is Comprehension= create a sequence(tuple, list, string, range) from a given sequence
# Why? Filtering, Searching, Fast, simple

## Get only even no from other list
even_num = [i for i in range(1, 21) if i%2==0]
print(even_num)
# Get only student name starting with a
list = ["Max", "ali", "alvin", "joan"]
new_std = [i for i in list if i.startswith("a")]
print(new_std)
squares = [i**2 for i in range(1,11)]
print(squares)
