# Program to get 5 color from user, display list, remove last color, and display again
list_colors = []
for i in range(5):
    color = input("Enter color: ")
    list_colors.append(color)
print("List of colors:", str(list_colors))
list_colors.pop()  # Remove the last color
print("List of colors after removing the last color:", str(list_colors))
list_colors.pop(0) # Remove the first color
print("List of colors after removing the first color:", str(list_colors))