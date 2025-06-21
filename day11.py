# Create an empty dictionary named my_dict.
my_dict = {}
# Prompt the user to enter the name and age of five people.
for i in range(5):
    name = input(f"Name {i+1}: ")
    age = int(input(f"Age {i+1}: "))
    my_dict[name] = age

# Print the dictionary.
print(my_dict)
# The number of people in the dictionary.
print(len(my_dict))
# The sum of all ages.
print(sum(my_dict.values()))
# The average age of the people.
print(sum(my_dict.values()) / len(my_dict))

# The oldest person's name and age.
oldest = max(my_dict, key=my_dict.get)
print(f"Oldest: {oldest}, Age: {my_dict[oldest]}")
# The youngest person's name and age.
youngest = min(my_dict, key=my_dict.get)
print(f"Youngest: {youngest}, Age: {my_dict[youngest]}")