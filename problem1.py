# Area of a Cicle Calculator
radius = float(input("Enter the radius of the circle: "))
circle_area = 3.14 * radius *radius
print("The area of the circle is " + str(circle_area))
print(circle_area)

colors = ("Red", "Green", "Blue", "Yellow", "Orange")
print(colors)
n = input("Enter color to check: ")
for i in colors:
    if n in colors:
        print(n)
    else:
        print("Invalid")