# Program to Check a Year, whether leap or not
year = int(input("Enter a year: "))
if (year%4 == 0):
    print("It is aleap year")
else:
    print("It is not a leap year")
    
array = []
for i in range(5):
    year = array.append(int(input("Enter a year: ")))
    if (array[i] % 4 == 0):
        print(array[i])
        
# Step 1: Input all years into an array
years = []
for i in range(5):
    year = int(input(f"Enter year {i+1}: "))
    years.append(year)

# Step 2: Check and print leap years from the array
print("Leap years in the array:")
for year in years:
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year)