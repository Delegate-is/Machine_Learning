# Comprehension in tuple - create new sequence from given sequence
t1 = (1,2,3,4,5,6,7,8,9,10)
t2 = tuple(i for i in t1 if i % 4 == 0)
print(t2)
t3 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
squares = tuple(i ** 2 for i in t3)
print(squares)