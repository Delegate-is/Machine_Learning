# Get password from user and check alphanumeric
pwd = input("Enter your password: ")
is_long_enough = len(pwd) >= 8

if is_long_enough:
    if pwd.isalnum():
        print("Yes")
        print("Your password is okey, that is " + pwd)
    else:
        print("Sorry, we did not allow white space and special character in your password that is " + pwd)
if not is_long_enough:
    print("Password length is less than 8 characters")
    
def validate_password():
    """
    Prompts the user to enter a password and validates it based on the following rules:jhgf
    - Must contain at least one digit.
    - Must contain at least one alphabetic character (letter).
    - Must be at least 8 characters long.
    """
    print("--- Password Validator ---")
    print("Password rules:")
    print("- Must contain at least one number.")
    print("- Must contain at least one letter.")
    print("- Must be at least 8 characters long.")

    while True:
        password = input("\nEnter your password: ").strip()

        has_digit = False
        has_alpha = False

        # Check for digit and alphabetic characters
        for char in password:
            if char.isdigit():
                has_digit = True
            elif char.isalpha():
                has_alpha = True

        # Check password length
        is_long_enough = len(password) >= 8

        # Evaluate all conditions
        if has_digit and has_alpha and is_long_enough:
            print("\nPassword is valid!")
            break # Exit the loop if password is valid
        else:
            print("\nPassword does not meet the requirements:")
            if not has_digit:
                print("- Missing at least one number.")
            if not has_alpha:
                print("- Missing at least one letter.")
            if not is_long_enough:
                # Based on the screenshot's wording "not be greater than or equal to 8",
                # if it meant strictly less than 8, this message would change.
                # Assuming standard interpretation: minimum 8 characters.
                print("- Password length is less than 8 characters.")
            print("Please try again.")

if __name__ == "__main__":
    validate_password()
