# Create dict from existed dict and key value should be len of dict
d = {"name":"Max", "age":'34', "course":"Python", "city":"Nairobi"}
print(d)
new_d = {k: len(k) for k, v in d.items()}
print(str(new_d))
new_d_2 = {v:len(v) for k, v in d.items()}
print(new_d_2)
list = [1, 2, 3, 4, 5, 6, 7, 8]
dict = {i: i*i for i in list}
print(dict)
dict_3 = {i*i:i for i in list}
print(dict_3)
lst = [23, 345, 15, 11, 245, 7899, 12, 2, 3]
new_lst = [i for i in lst if i < 20 if i > 5]
print(new_lst)
add = 0
for i in new_lst:
    add += i
print(add)
d_2 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
list_6 = [item for item in d_2.items() if 5 < item[1] < 20]
print(list_6)