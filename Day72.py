# Set Union method -- assumes duplicated elements
def set_union(set1, set2, set3):
    c = set1.union(set2, set3)
    print(c)
set1 = {3,5,67,8}
set2 = {4,3,567,9,0,8}
set3 = {23,4,9,3,6,8}
set_union(set1, set2, set3)

# Set Intersection -- will take duplicated elements
def common_elements(set1,set2):
    result = set1.intersection(set2)
    print(result)
set1 = {1,2,3,4}
set2 = {3,2,4}
common_elements(set1,set2)

def unique_elements():
    input_list = [12,3,3,2,4,56,12,45,654,43,3,2]
    st3 = set(input_list)
    print(st3)
unique_elements()

# Create a set and update with item from user
st1 = {"pink", "black", "boy", "girl"}
print(f"Original Set: {st1}")
item = input("Enter item to update: ")
user_item = {item}
st1.update(user_item)
print(f"Updated SET: {st1}")

# Get 5 no from user, find add and mul
st2 = set()
for i in range(5):
    num = int(input("Enter number to set"))
    st2.add(num)
print(st2)
add = 0
for i in st2:
    add += i
print(f"Addition = {add}")
mul = 1
for i in st2:
    mul *= i
print(f"Multiplication = {mul}")

# Get 5 item from user and store in both lower and upper
st = set()
for i in range(5):
    item = input("Enter set item: ")
    st.add(item)
print(st)
for i in st:
    print(i.upper())
for i in st:
    print(i.lower())