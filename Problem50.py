# Get base and height from user and find triangle area
height = float(input("Enter triangle height: "))
base = float(input("Enter triangle base: "))
area_triangle = (base * height)/2
print("Triangle area = "+str(area_triangle))
num = float(input("Enter a number: "))
sq_num = num*num
print("Square of num plus triangle area = "+str(sq_num+area_triangle))