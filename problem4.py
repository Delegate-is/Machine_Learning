name = input("Enter your name: ")
age = int(input("Enter your age: "))
x = 18 - age
if age >= 18:
    print(name, "can participate in voting")
else:
    print("Sorry", name,"You cannot participate in voting, you will be able to vote in", x, "years")
    
def check_admission_eligibility():
    """
    Prompts the user for marks and checks if they are eligible for college admission.
    Requires marks to be 60 or more.
    """
    print("--- College Admission Eligibility Checker ---")
    while True:
        try:
            # Prompt the user to enter marks
            marks_input = input("Enter your marks: ").strip()

            # Convert input to an integer
            marks = int(marks_input)

            # Check if marks are valid (e.g., not negative)
            if marks < 0:
                print("Marks cannot be negative. Please enter a valid score.")
                continue # Ask for input again

            # Define the minimum required marks
            MIN_MARKS_FOR_ADMISSION = 60

            # Check eligibility
            if marks >= MIN_MARKS_FOR_ADMISSION:
                print(f"Congratulations! With {marks} marks, you are eligible for admission.")
            else:
                marks_needed = MIN_MARKS_FOR_ADMISSION - marks
                print(f"Sorry! You cannot take admission, you need {marks_needed} numbers more to take admission.")

            # Ask if the user wants to check another number or exit
            another_check = input("\nDo you want to check another score? (yes/no): ").strip().lower()
            if another_check != 'yes':
                print("Exiting admission checker. Goodbye!")
                break # Exit the loop and end the program

        except ValueError:
            print("Invalid input. Please enter a valid number for marks.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

if __name__ == "__main__":
    check_admission_eligibility()
