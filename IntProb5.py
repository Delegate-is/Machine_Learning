# Program storing student records and deleting any student from record on run time
list = []
for i in range(3):
    list.append(input("Enter a student name: "))
    i += 1
    print(list)
std_name = input("Enter std name you want to delete: ")
list.remove(std_name)
print("Student List "+str(list))
new_name = input("Enter name you want to update: ")
index_of_name = int(input("Enter index of name to update: "))
list[index_of_name] = new_name
print("Student List "+str(list))

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
if n1 > n2:
    print(str(n2)+", n1 is the max number")
else:
    print(str(n2)+", n2 is the max number")
char = input("Enter a character: ")
if char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u':
    print(str(char)+", is a vowel")
else:
    print(str(n2)+", is a consonant")