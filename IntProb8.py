# Get string from user and reverse
user_string = input("Enter a string: ")
s = int(input("Enter a starting number"))
e = int(input("Enter a ending number"))
user_sub_s = user_string[s:e]
print(user_sub_s)
print(user_sub_s[::-1])
print(user_string)

import random
import string

def generate_strong_password():
    """
    Generates a strong password based on user-defined length.
    The password will include a mix of lowercase letters, uppercase letters,
    digits, and special characters to ensure strength.
    """
    print("--- Strong Password Generator ---")

    while True:
        try:
            # Get the desired password length from the user
            length_str = input("Enter the desired password length (minimum 8 characters): ")
            password_length = int(length_str)

            if password_length < 8:
                print("Password length must be at least 8 characters. Please try again.")
            else:
                break # Exit loop if length is valid
        except ValueError:
            print("Invalid input. Please enter a whole number for the length.")

    # Define character sets for different types of characters
    lowercase_chars = string.ascii_lowercase
    uppercase_chars = string.ascii_uppercase
    digit_chars = string.digits
    # Common special characters, excluding space and characters that might cause issues
    # in some contexts (e.g., backslash, quotes if not escaped properly)
    special_chars = string.punctuation.replace(' ', '')

    # Ensure the password contains at least one of each required type
    # This guarantees a strong password with varied characters
    password_chars = []
    password_chars.append(random.choice(lowercase_chars))
    password_chars.append(random.choice(uppercase_chars))
    password_chars.append(random.choice(digit_chars))
    password_chars.append(random.choice(special_chars))

    # Combine all possible character sets
    all_chars = lowercase_chars + uppercase_chars + digit_chars + special_chars

    # Fill the rest of the password length with random choices from all characters
    for _ in range(password_length - 4): # -4 because we already added 4 characters
        password_chars.append(random.choice(all_chars))

    # Shuffle the list of characters to ensure randomness and avoid predictable patterns
    random.shuffle(password_chars)

    # Join the list of characters to form the final password string
    generated_password = "".join(password_chars)

    print(f"\nGenerated Strong Password: {generated_password}")
    print(f"Password Length: {len(generated_password)}")

# Call the function to run the program
if __name__ == "__main__":
    generate_strong_password()
