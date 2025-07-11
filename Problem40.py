# Get username from user
# Make condition to check, it should contain alpha numeric char
u = input("Enter your username: ")
def check_user(u):
    if(u.isalnum()):
        if(len(u) > 8):
            print("Okey your username is " + u)
        else:
            print("Username length should not be less than or equal to 8")
    else:
        print("Use alphanumeric without whitespace")
check_user(u)