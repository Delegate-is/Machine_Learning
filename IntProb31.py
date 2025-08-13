# Dict displaying only value with vowel char
dict = {1:"Red", 2:"Blue",3:"Green"}
print(dict)
for value in dict.values():
    if 'a' in value or 'e' in value or 'i' in value or 'o' in value or 'u' in value:
        print(value)
numbers = []        
for i in range(4):
    numbers.append(input(f"Enter a number {i+1}: "))
    
print(max(numbers))
print(min(numbers))
# If you want to check if any number starts with a specific digit, for example '1':
print([num for num in numbers if num.startswith('1')])