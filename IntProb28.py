# Get max ey in a dictionary(with number data type key)
dict = {1:"Uno",2:"Dooh", 3:"Euros", 14:"Ends"}
print(dict)
keys =[]
for k in dict.keys():
    keys.append(k)
print(keys)
keys.sort()
print(keys[-1])
dict1 = {"Uno":12,"Dooh":123, "Euros":76, "Ends":90}
values = []
for v in dict1.values():
    values.append(v)
print(values)
values.sort()
print(values[-1])