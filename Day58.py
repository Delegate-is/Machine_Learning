# list
numbers = []
for i in range(5):
    num = int(input(f"Enter a number {i+1}:"))
    numbers.append(num)
    print(numbers)
    for n in numbers:
        print(str(n) + " have square is " + str(n * n))
numbers.remove(numbers[0])
print(numbers)
word = []
for i in range(5):
    name = input(f"Enter a word {i+1}:")
    word.append(name)
    print(word)
for j in word:
    if j.endswith("n"):
        print(j)
index =int(input("Enter position to change item"))
new_value = input("New value")
word[index] = new_value
print(word)

num = int(input("Enter two numbers separated by space: "))
num1, num2 = map(num.split)
print(f"Sum = {num1+num2}")
