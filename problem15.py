# Get 6 numbers from user
my_list = []
for i in range(6):
    my_list.append(int(input("Enter a number: ")))
print("This is my list")
print(my_list)
print(sum(my_list))
# Clear the List
my_list.clear()
print("We have removed the list items")
# Display list again
print(my_list)

temp_list = []
for i in range(6):
    temp_list.append(int(input("Enter a number: ")))
Tupl = tuple(temp_list)
print(Tupl)
print("Sum: " + str(sum(Tupl)))
# Tuples are immutable and do not have a clear() method
# To "clear" a tuple, you can assign an empty tuple if needed
Tupl = ()
print("We have assigned an empty tuple to Tupl")
print(Tupl)