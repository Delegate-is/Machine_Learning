#python list methods == max and min
num= [2,456,53,53,56,521,56,4]
maxi_num = max(num)
print(maxi_num)
min_num = min(num)
print(min_num)
# python list method = reverse
num.reverse()
print(num)
# python list method== append method
list = ["Python", "JS", "Java", "C"]
print(list)
list.append("CSS")
print(list)
# python list method== remove
list.remove("C")
print(list)
# python list method== remove
list.sort()
print(list)
lst = [4,5,3,1,0,7,6]
lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
# python list method == copy
new_list = list.copy()
print(list)
print(new_list)
list.append("R")
print(new_list)
print(list)
# python list method == join
list_1 = ["Max", "Joe", "Hope"]
joined_list = ' * '.join(list_1)
print(list_1)
print(joined_list)
# python list method == clear
print(list_1)
list_1.clear()
print(list_1)

fruits =[]
for i in range(5):
    fruits.append(input(f"Enter a fruit {i+1}"))
    print(fruits)
fruits.sort()
print(fruits)
fruits.remove(fruits[0])
print(fruits)
fruits.remove(fruits[3])
print(fruits)
# python list method == pop(remove last element)
fruits.pop()
print(fruits)
# python list method == count
len_of_item = fruits.count("Oranges")
print(len_of_item)
#python list method == len
len_fruits = len(fruits)
print(len_fruits)
#python list method == extend
lst_1 = ["Beets", "Pineapple"]
fruits.extend(lst_1)
print(fruits)
# python list method == index
fruits.index("Oranges")
# python list method == insert
fruits.insert(0, "Mango")