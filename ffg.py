list_1 = [ [1, 2, 3], [4, 5], [6, 7, 8, 9], ["Max", "Codeweb"], [True, False]]
total = 0
for i in list_1:
    if type(i) == list:
        total += 1
print(f"Total number of lists in the nested list: {total}")  # Display the count of lists