# Handle key error and index error
dict = {1:"pink", 2:"gray",3:"green",4:"yellow"}

try:
    print(dict[5])
except KeyError:
    print("Key does not exist")
    
list = ["yellow", "green", "blue", "pink"]

try:
    print(list[6])
except IndexError:
    print("Index number does not exist in the list")
    
    
def safe_division(numerator, denominator):
    try:
        print((numerator/denominator) / 0)
    except ZeroDivisionError:
        print("Cannot divide by zero")
    else:
        print((numerator/denominator) / 0)
        
safe_division(2,5)