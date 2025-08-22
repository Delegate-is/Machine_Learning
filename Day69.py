# Python Dictionary Method -- clear{}
color = {1:"Red", 2:"Blue",3:"Yellow"}
print(color)
color.clear()
print(color)
# Python Dictionary Method -- copy{}
color_1 = {1:"Red", 2:"Blue"}
new_dict = color_1.copy()
print(new_dict)
# Python Dictionary Method -- fromkeys{}
seq_list = ["a","b","c","d","e"]# can also be a set, any sequence
new_seq_dict = dict.fromkeys(seq_list, "Max")
print(new_seq_dict)
# Python Dictionary Method -- get{}
color = {1:"Red", 2:"Blue",3:"Yellow", 4:"Pink", 5:"Green"}
color_val = color.get(3, "Not Exist")
print(color_val)
rem_item = color.popitem()
print(rem_item)
# Python Dictionary Method -- items {}
color_items = color.items()
print(color_items) 
student = {"name": "John","age": 25,"city": "New York","country": "USA"}
print(f"Original student {student}")
student.pop("city")
print(f"Updated student {student}")
# Python Dictionary Method -- keys {}
student_keys = student.keys()
print(student_keys)
student_val = student.values()
print(student_val)
# Python Dictionary Method -- setdefault {}
dict = {1:"Max", 2:"Code"}
element = dict.setdefault(2)
print(element)
element = dict.setdefault(3, "Not Exist")
print(element)
dict_1 ={4:"Python"}
dict.update(dict_1)
print(dict.values())
dict.update({5:"Friday"})
print(dict)

num = input("Enter two numbers seperated by a space: ")
num1, num2 = map(float, num.split())
sum = num1 + num2
diff_result = num1 - num2
product_result = num1 * num2
quotient_result = num1 / num2  # This gives float division
print(f"Sum: {sum}")
print("Difference:", diff_result)
print("Product:", product_result)
print("Quotient:", quotient_result)