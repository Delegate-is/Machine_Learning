# Python program that calculates union of two sets
A = {3,2,4.5,6,7,8}
B = {4,12,5,1,6,8}
C = A.union(B)
print("Union of A and B is: ", C)

D = {5,12,52,0,8}
E = {2,5,1,9,8}
F = {4,5,6,0,10}
G = D.union(E).union(F)
print("Union of D, E and F is: ", G)
