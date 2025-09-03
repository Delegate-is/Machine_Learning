# Python SET Comprehension
# Set comprehension is a concise way to create sets in Python using a single line of code.
# It is similar to list comprehension but uses curly braces {} instead of square brackets [].
# Set comprehension allows you to generate a set by applying an expression to each item in an iterable,
# optionally filtering items with a condition.
# Syntax: {expression for item in iterable if condition}
# Example 1: Creating a set of squares of numbers from 0 to 9
squares = {x**2 for x in range(10)}
print(squares)  # Output: {0, 1, 4, 9, 16, 25, 36, 49, 64, 81}
# Example 2: Creating a set of unique vowels from a given string
vowels = {char for char in 'Hello World' if char in 'aeiouAEIOU'}
print(vowels)  # Output: {'e', 'o'}
list = [1,2,3,4,5,6,7,8,9]
new_set = {i+3 for i in list}
print(f"New set {new_set}")
# Output: {4, 5, 6, 7, 8, 9, 10, 11, 12}
# Example 3: Creating a set of even numbers from a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = {num for num in numbers if num % 2 == 0}
print(even_numbers)  # Output: {2, 4, 6, 8, 10}
# Example 4: Creating a set of characters from a string, excluding spaces
string = "Hello World"
char_set = {char for char in string if char != ' '}
print(char_set)  # Output: {'H', 'e', 'l', 'o', 'W', 'r', 'd'}
# Example 5: Creating a set of lengths of words in a list
words = ["apple", "banana", "cherry", "date"]
word_lengths = {len(word) for word in words}
print(word_lengths)  # Output: {4, 5, 6}
# get only odd numbers from 1 to 100
odd_numbers = {num for num in range(1, 101) if num % 2 != 0}
print(odd_numbers)  # Output: {1, 3, 5, 7, 9, ..., 99}
# Example 6: Creating a set of uppercase letters from a string
string = "Hello World"
uppercase_letters = {char for char in string if char.isupper()}
print(uppercase_letters)  # Output: {'H', 'W'}
# get student name ending with 'a'
student_names = ["Alice", "Bob", "Catherine", "David", "Eva"]
names_ending_with_a = {name for name in student_names if name.endswith('a')}
print(names_ending_with_a)  # Output: {'Eva'}
# Example 7: Creating a set of unique characters from a string
string = "Hello World"
unique_chars = {char for char in string}
print(unique_chars)  # Output: {'H', 'e', 'l', 'o', ' ', 'W', 'r', 'd'}
def squared_set(input_list):
    return {x**2 for x in input_list}
print(squared_set([1, 2, 3, 4, 5]))  # Output: {1, 4, 9, 16, 25}
a = set()
b = set()
for i in range(5):
    a.add(i)
    b.add(i*2)
c = {i for i in a if i in b}
print(c)  # Output: {0, 2, 4}
u = a.union(b)
print(f"Union {u}")  # Output: {0, 1, 2, 3, 4, 6, 8}
i = a.intersection(b)
print(f"Intersection {i}")  # Output: {0, 2, 4}
d = a.difference(b)
print(f"Difference {d}")  # Output: {1, 3}
# Symmetric difference
s = a.symmetric_difference(b)
print(f"Symmetric difference {s}")  # Output: {1, 3, 6, 8}
# find sum of union, intersection, difference, symmetric difference
print(f"Sum of union {sum(u)}")  # Output: 24
print(f"Sum of intersection {sum(i)}")  # Output: 6
print(f"Sum of difference {sum(d)}")  # Output: 4
print(f"Sum of symmetric difference {sum(s)}")  # Output: 18
print(f"Length of union {len(u)}")  # Output: 7
print(f"Length of intersection {len(i)}")  # Output: 3
print(f"Length of difference {len(d)}")  # Output: 2
print(f"Length of symmetric difference {len(s)}")  # Output: 4
print(f"Max of union {max(u)}")  # Output: 8
print(f"Min of union {min(u)}")  # Output: 0
print(f"Max of intersection {max(i)}")  # Output: 4
print(f"Min of intersection {min(i)}")  # Output: 0
print(f"Max of difference {max(d)}")  # Output: 3
print(f"Min of difference {min(d)}")  # Output: 1
print(f"Max of symmetric difference {max(s)}")  # Output: 8
print(f"Min of symmetric difference {min(s)}")  # Output: 1   