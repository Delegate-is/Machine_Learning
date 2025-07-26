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
