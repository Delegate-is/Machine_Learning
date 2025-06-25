# Progran getting name of week and show Holiday if input is Sunday
name = input("Enter name of the week: ")
# if (name == "Sunday") or (name == "sunday"):
if name in ("sunday", "Sunday", "friday", "Friday"):
    print("It is a Holiday")
else:
    print(f"It is {name}. It is not a holiday")

week_name = input("Enter a week name: ")
if (week_name == 'Sunday' or week_name == 'sunday'):
    print("It is a Holiday")
else:
    print("It is not a Holiday")
    
name2 = input("Enter name of the week: ")
if (name2 != 'Sunday'):
    print("It is not a holiday")
else:
    print("It is a holiday")