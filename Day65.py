# Python Dictionary -mutable/ changeable/ ordered
dict = {"name1":"Max", "town":"Naru", "subj":"Python", "school":"UON", 319:"P.O Box"}
print(dict)
print(dict["name1"])
print(dict[319])
dict_1={
    's_id':5056,
    's_name':'Dele',
    1960:'Kayole'
}
print(dict_1)

student ={
    "id":1,
    "name": "John",
    "age": 25,
    "city": "New York",
    "country": "USA",
    "contact":1234567
}
print(f"ID: {student['id']}")
print(f"Name: {student['name']}")
print(f"Age: {student['age']}")
print(f"City: {student['city']}")
print(f"Country: {student['country']}")
print(f"Contact: {student['contact']}")
student["age"]=26
print(f"Updated student {student}")
# Get 5 no from user and store sqr as value in dict
dict_2 ={}
for i in range(5):
    n = (int(input(f"Enter a number {i+1}: ")))
    dict_2[n] = n*n
    print(dict_2)