import subprocess
import platform
import sys

def check_python_installation():
    """
    Checks if the 'python' command is accessible in the system's PATH
    and provides instructions if it's not.
    """
    print("--- Python Installation Checker ---")

    # Try to run 'python --version' command
    try:
        # Use shell=True for simple commands; for more complex or untrusted inputs,
        # shell=False and passing commands as a list is safer.
        # Here, it's for checking system command availability.
        result = subprocess.run(['python', '--version'],
                                capture_output=True,
                                text=True,
                                check=True, # Raise an exception for non-zero exit codes
                                encoding='utf-8')

        # If successful, Python is installed and accessible
        print("Python is installed and accessible!")
        print(f"Version: {result.stdout.strip()}")
        print("\n--- You can now run Python scripts! ---")

    except (subprocess.CalledProcessError, FileNotFoundError):
        # If the command fails or 'python' is not found
        print("\nPython is NOT found in your system's PATH or not installed.")
        print("Please follow these instructions to install Python on Windows:")
        print("\n--- Python Installation Instructions (Windows) ---")
        print("1. Go to the official Python website: https://www.python.org/downloads/")
        print("2. Download the latest Python 3 installer (.exe file) for Windows.")
        print("3. Run the installer.")
        print("4. IMPORTANT: On the first screen, make sure to check the box 'Add Python 3.x to PATH'.")
        print("5. Click 'Install Now' (or 'Customize installation' if you need specific options).")
        print("6. Follow the on-screen prompts to complete the installation.")
        print("7. After installation, CLOSE and REOPEN your Command Prompt/PowerShell window.")
        print("8. Verify by typing 'python --version' or 'py --version' in the new terminal.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        print("Could not determine Python installation status.")

if __name__ == "__main__":
    check_python_installation()

