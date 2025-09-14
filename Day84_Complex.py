# get filename from user without space
f_name = input("Enter a file name: ")
flag = "No"
for i in f_name:
    if i.isspace():
        flag = "Yes"
if flag == "Yes":
    print("File contain space")
else:
    print("File name is "+f_name+", there is no space")
    
# Program to replace spaces in a file name with dots

# Get file name from user
file_name = input("Enter the file name: ")

# Replace spaces with dots
cleaned_name = file_name.replace(" ", ".")

print("Updated file name:", cleaned_name)
