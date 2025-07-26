#   Get alpha numeric password
password= input("Enter your password: ")
def check_password():
    if (password.isalnum() and not password.isalpha() and not password.isdigit()):
        if(len(password)>8 and len(password)<20):
            print("Password is alright")
        else:
            print("Password should be more than 8 and less than 20")
    else:
        print("Sorry, enter alphanumeric characters")
check_password()

import string

def validate_password():
    """
    Prompts the user to enter a password and validates it against the following rules:
    - Must contain alphanumeric characters (a-z, 0-9).
    - Must contain special characters.
    - Length must be between 9 and 19 characters (inclusive).
    - Must NOT contain uppercase letters.
    - Must NOT contain spaces.
    """
    print("--- Password Validator ---")
    print("Password Rules:")
    print("  - Must be between 9 and 19 characters long.")
    print("  - Must contain lowercase letters and numbers.")
    print("  - Must contain special characters (e.g., !, @, #, $).")
    print("  - Must NOT contain uppercase letters.")
    print("  - Must NOT contain spaces.")

    while True:
        password = input("\nEnter your password: ")

        # Rule 1: Check length (more than 8 and less than 20 characters)
        # This means length should be between 9 and 19 (inclusive)
        if not (8 < len(password) < 20):
            print("Validation Failed: Password must be between 9 and 19 characters long.")
            continue

        # Rule 2: Restrict uppercase letters
        if any(char.isupper() for char in password):
            print("Validation Failed: Password must not contain uppercase letters.")
            continue

        # Rule 3: Restrict spaces
        if ' ' in password:
            print("Validation Failed: Password must not contain spaces.")
            continue

        # Rule 4: Must contain alphanumeric (lowercase letters and digits)
        has_lowercase = any(char.islower() for char in password)
        has_digit = any(char.isdigit() for char in password)
        if not (has_lowercase and has_digit):
            print("Validation Failed: Password must contain both lowercase letters and numbers.")
            continue

        # Rule 5: Must contain special characters
        # We define special characters as anything that's not a letter, digit, or space.
        # string.punctuation contains common special characters.
        special_chars = string.punctuation
        has_special_char = any(char in special_chars for char in password)

        if not has_special_char:
            print("Validation Failed: Password must contain at least one special character.")
            continue

        # If all checks pass
        print("Password is valid!")
        break

# Call the function to run the program
if __name__ == "__main__":
    validate_password()
