# Store color and count then display to user
colors_list =['Red', 'Green', 'Blue', 'Yellow', 'Black', 'White', 'Pink', 'Purple', 'Orange', 'Gray']
print("Colors in the list are: "+str(colors_list))
print("Total colors in the list = " +str(len(colors_list)))

# Program to get element from the user, store in the list and count that element and display to user
color = input("Enter the color you want to count: ").capitalize()
if color in colors_list:
    count = colors_list.count(color)
    print(f"The color {color} appears {count} time(s) in the list.")
else:
    print(f"The color {color} is not in the list.")
# Program to get element from the user, store in the list and display index of that element
color_index = input("Enter the color you want to find the index of: ").capitalize()
if color_index in colors_list:
    index = colors_list.index(color_index)
    print(f"The color {color_index} is at index {index} in the list.")
else:
    print(f"The color {color_index} is not in the list.")
    