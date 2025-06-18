# Program that gets 6 subject marks from the user and calculates the average
def get_marks():
    marks  = []
    for i in range(6):
        while True:
            try:
                mark = float(input(f"Enter mark for subject {i + 1}: "))
                if 0<= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Please enter a valid mark between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
    return marks

marks = get_marks()

average = sum(marks) / len(marks)
print(average)
total = sum(marks)
print(total)
#percentage = (marks / 600) * 100
#print(percentage)

def calculate_student_marks():
    """
    Gets marks for 6 subjects from the user, calculates total, average,
    and percentage, and displays the results.
    """
    print("--- Student Marks Calculator ---")
    num_subjects = 6
    marks_list = []
    total_marks = 0

    print(f"Please enter the marks for {num_subjects} subjects (out of 100 per subject).")

    # Loop to get marks for each subject
    for i in range(1, num_subjects + 1):
        while True:
            try:
                mark_input = input(f"Enter marks for Subject {i}: ").strip()
                mark = float(mark_input) # Use float to allow for decimal marks

                # Validate marks: ensure they are within a reasonable range (e.g., 0-100)
                if 0 <= mark <= 100:
                    marks_list.append(mark)
                    total_marks += mark
                    break # Exit inner loop if input is valid
                else:
                    print("Invalid marks. Please enter a value between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter a number for marks.")
            except Exception as e:
                print(f"An unexpected error occurred: {e}. Please try again.")

    # Calculate Average
    average_marks = total_marks / num_subjects

    # Calculate Percentage
    # Assuming each subject is out of 100, the total possible marks is num_subjects * 100
    max_possible_total_marks = num_subjects * 100
    percentage = (total_marks / max_possible_total_marks) * 100

    print("\n--- Results ---")
    print(f"Marks entered: {marks_list}")
    print(f"Total Marks: {total_marks:.2f}") # Display total with 2 decimal places
    print(f"Average Marks: {average_marks:.2f}") # Display average with 2 decimal places
    print(f"Percentage: {percentage:.2f}%") # Display percentage with 2 decimal places

    # Provide a simple pass/fail indication (optional)
    if percentage >= 40: # Example pass percentage
        print("Status: Pass")
    else:
        print("Status: Fail")

if __name__ == "__main__":
    calculate_student_marks()
