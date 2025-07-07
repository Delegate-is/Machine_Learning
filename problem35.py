# Program to get 10 names of students in a list, display the list, and remove the last student
student_list= []
for i in range(10):
    student_list.append(input("Enter student name: "))
# Print the list of students
print("List of students:, str(student_list)")
for j in student_list:
    print("Student name:", j)
# print list in descending order
student_list.sort(reverse=True)
print("List of students in descending order:, str(student_list)")
for d in student_list:
    print("Student name in descending order:", d)
student_list.pop()  # Remove the last student
student_list.pop(0)  # Remove the first student
print("List of students after removing the last student:", str(student_list))