# Loop in Python Dictionary
student ={
    "id":1,
    "name": "John",
    "age": 25,
    "city": "New York",
    "country": "USA",
    "contact":1234567
}
# Iterating items
for key, value in student.items():
    print(key, ':', value)
# Iterating Keys
for key in student.keys():
    print(f"KEY {key}")
# Iterating Values
for value in student.values():
    print(F"VALUE {value}")

dict = {"name1":"Max", "town":"Naru", "subj":"Python", "school":"UON", 319:"P.O Box"}
print(dict)
for k, v in dict.items():
    print(str(k)+ ' : '+str(v))

# Prob 1 : get marks in key value form
dict_1 = {}
for i in range(3):
    name = input("Enter student name: ")
    marks = int(input("Enter student marks: "))
    dict_1[name] = marks
print(dict_1)
for k in dict_1.keys():
    print(k)
    
# Prob 2 : digital product and price
dict_2 = {}
for i in range(3):
    product = input("Enter product name: ")
    price = int(input("Enter product price: "))
    print(str(product)+' : '+str(price))
    dict_2[product]=price
print(dict_2)
sum = 0
for i in dict_2.values():
    sum += i
print(f"Total price = {sum}")