# Comprehension - creating new sequence from exixting sequences
# Comprehension with dictionaries
dict = {'a':4, 'b':3, 'c':5, 'd':6}
new_d ={k.upper():v*3+2 for k,v in dict.items()}
print(new_d)
new_d2 = {k:('even' if v%2 == 0 else 'odd') for (k,v) in dict.items()}
print(new_d2)
dict = {'red':32,'blue':82, "black":234, 'white':89, 'indigo':6}
simple_dict = {k:v+3  for (k,v)in dict.items() if v % 2 == 0}
print(simple_dict)
nested_dict = {k:v for (k,v) in dict.items() if v%2==0 if v%3==0}
print(nested_dict)
# Prob 1 = create dict displau leng of word as value
list =['a', 'boy', 'cat', 'donkey', 'goat']
list_dict = {i:len(i) for i in list if len(i)<5}
print(list_dict)
num = [1,2,3,4,5,6,7,8,9,10]
squares = {i:i*i for i in num}
print(squares)
squares = {i:i**2 for  i in range(1, 10+1)}
print(squares)
# Prob 2: dict from list