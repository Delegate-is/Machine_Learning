# Program that stores name, address contact and update contact number in the dictionary
# Key:value
user_dict ={"Name":"Ali", "Address":"Kagio", "Age":32, "Contact":710230344}
print("First Record")
print(user_dict)
user_dict.update({"Contact":1234567})
print("Updated Record")
print(user_dict)
user_dict.update({"Contact": int(input("Enter a number:"))})
print("Updated Record Again, this time by User during run time")
print(user_dict)