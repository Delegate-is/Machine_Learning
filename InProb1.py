# Program to get any file extension
import os
file = input("Enter a file with extension: ")
file_name, file_extension = os.path.splitext(file)
"""file_extension_lower = file_extension.lower()
if file_extension.lower == '.mp3':
    print("This File is Not Allowed")
else:
    print(f"File '{file_name}' with extension '{file_extension}' is allowed")
"""
print("File name is "+ file_name)
print("File extension is "+ file_extension)

import os

def check_file_extension():
    """
    Prompts the user to enter a filename, then checks if its extension
    is '.mp3'. If it is, a message "This File Is Not Allowed" is displayed.
    Otherwise, a message indicating the file is allowed is shown.
    """
    print("--- File Extension Checker ---")

    while True:
        # Get the filename from the user
        filename = input("Enter the filename (e.g., song.mp3, document.pdf): ")

        if filename.strip() == "":
            print("Filename cannot be empty. Please enter a filename.")
            continue

        # Use os.path.splitext to separate the filename and its extension
        # It returns a tuple: (root, ext)
        # Example: os.path.splitext("song.mp3") returns ('song', '.mp3')
        # Example: os.path.splitext("document.pdf") returns ('document', '.pdf')
        # Example: os.path.splitext("archive.tar.gz") returns ('archive.tar', '.gz')
        # Note: It only gets the last extension.

        file_root, file_extension = os.path.splitext(filename)

        # Convert the extension to lowercase for case-insensitive comparison
        # e.g., '.MP3' should also be caught
        file_extension_lower = file_extension.lower()

        # Check if the lowercase extension is '.mp3'
        if file_extension_lower == '.mp3':
            print("This File Is Not Allowed")
        else:
            print(f"File '{filename}' with extension '{file_extension}' is allowed.")

        # Ask if the user wants to check another file
        another_check = input("\nDo you want to check another file? (yes/no): ").lower()
        if another_check != 'yes':
            break

    print("Exiting file extension checker. Goodbye!")

# Call the function to run the program
if __name__ == "__main__":
    check_file_extension()
