# Get no from user and find number from 1 and their addition
num = int(input("Enter a number: "))
sum = 0
for i in range(1, num+ 1):
    print(i)
    sum += i
print(f"Sum of numbers from 1 to {num} is: {sum}")
# Get a strinf and display in reverse order
str_input = input("Enter a string: ")
print(f"Reversed string: {str_input[::-1]}")  # Display the string in reverse order
# Get a string and display its length
str_input = input("Enter a string: ")
print(f"Length of the string: {len(str_input)}")  # Display the length of the string
f = "sjdhfgetwy"
print(f[::-1])
def reverse_string(f):
    for i in f:
        f = i + f
    return (f)
print(reverse_string(f))  # Function to reverse a string
# Get sentence and system have ability to replace words
sentence = input("Enter a sentence: ")
word_to_replace = input("Enter the word to replace: ")
replacement_word = input("Enter the replacement word: ")
modified_sentence = sentence.replace(word_to_replace, replacement_word)
print(f"Modified sentence: {modified_sentence}")  # Display the modified sentence
str_3 = " "
if str_3.isspace():
    print("The string contains whitespace characters.")
else:
    print("The string does not contain whitespace characters.")
    # Get 3 marks from user and find total, average and percentage
sum = 0
for i in range(3):
    mark = int(input(f"Enter mark {i+1}: "))
    sum += mark
total = sum
average = total / 3
percentage = (total / 3) * 100
print(f"Total: {total}, Average: {average}, Percentage: {percentage}%")
# Enter 3 numbers seperated by space and find the largest number and smallest plus average
numbers = input("Enter three numbers separated by space: ")
numbers_list = list(map(int, numbers.split()))
largest = max(numbers_list)
smallest = min(numbers_list)
total = sum(numbers_list)
average = total / len(numbers_list)
print(f"Largest: {largest}, Smallest: {smallest}, Average: {average}")