# Program to get email from user
import re
email = input("Enter a email: ")

x = re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$', email)
if x:
    print("Email is valid")
else:
    print("Email is invalid")

import re

def is_valid_url(url_string):
    """
    Checks if a given string is a valid URL using a regular expression.
    This regex is a common pattern for URL validation, but might not cover
    every single edge case according to RFCs, which are very complex.
    It generally checks for:
    - A scheme (http, https, ftp, etc.)
    - Optional user:pass@
    - A domain name (with at least one dot)
    - Optional port
    - Optional path, query string, and fragment

    Args:
        url_string (str): The string to validate as a URL.

    Returns:
        bool: True if the URL is considered valid, False otherwise.
    """
    # Regex pattern for URL validation.
    # This pattern is robust enough for common URL formats.
    # It checks for a scheme (http, https, ftp, sftp),
    # then a domain, and optional path/query/fragment.
    url_pattern = re.compile(
        r'^(?:http|ftp|https|sftp)://'  # Scheme (http, https, ftp, sftp)
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|' # Domain name
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})' # IP address
        r'(?::\d+)?'  # Optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE) # Optional path, query, fragment

    return re.match(url_pattern, url_string) is not None

def main():
    """
    Prompts the user to enter a URL and then checks its validity,
    displaying whether it's a valid URL or not.
    """
    print("--- URL Validator Program ---")

    while True:
        user_url = input("Please enter a URL to check (e.g., https://www.example.com): ")

        if user_url.strip() == "":
            print("URL cannot be empty. Please enter a URL.")
            continue

        if is_valid_url(user_url):
            print(f"'{user_url}' is a VALID URL.")
        else:
            print(f"'{user_url}' is NOT a valid URL.")

        another_check = input("\nDo you want to check another URL? (yes/no): ").lower()
        if another_check != 'yes':
            break

    print("Exiting URL validator. Goodbye!")

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
