# Create numeric dict and display only even keys
num = {1:2345, 2:23456, 3:23456, 4:34567}
for k,v in num.items():
    if v%2 == 0:
        print(k)
# Create dict from list
lst = [1,2,3,4,4,5,6]
dict = {i:i*5 for i in lst}
print(dict)
# Display min and max from dict
num_dict = {1: 5, 2: 10, 3: 15, 4: 20, 5: 25, 6: 30}
print(num_dict.items())
max_val = max(num_dict.values())
print(max_val)
min_val = min(num_dict.values())
print(min_val)
# Check whether a specific key exist or not
n = int(input("Enter key to check: "))
for k in num_dict.keys():
    if n == k:
        print(str(n) + " Key exists")
    else:
        print(str(n) + " Key does not exist")
#prob
colors = {}
for i in range(5):
    color_name = input("Enter color name: ")
    color_code = int(input("Enter color code: "))
    colors[color_name] = color_code
print(colors)
new_colors = {k.upper():v for (k,v) in colors.items()}
print(new_colors)
for k,v in new_colors.iten():
    print(str(k)+":"+str(v))