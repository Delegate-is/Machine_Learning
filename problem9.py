num = int(input("Enter a number: "))
print("You entered: " + str(num))
# 1*2=4
for i in range(1, 11):
    print(str(i) + "*" + str(num) + "=" + str(i * num))
def table(num):
    for i in range(1, 11):
        print(str(i) + "*" + str(num) + "=" + str(i * num))

table(num)

def generate_two_number_tables():
    """
    Prompts the user to enter two numbers and displays their multiplication tables
    from 1 to 10.
    """
    print("--- Two Number Table Generator ---")

    while True:
        try:
            # Get the first number from the user
            num1_str = input("Enter the first number: ").strip()
            num1 = int(num1_str)

            # Get the second number from the user
            num2_str = input("Enter the second number: ").strip()
            num2 = int(num2_str)

            print(f"\n--- Multiplication Table for {num1} ---")
            for i in range(1, 11): # Loop from 1 to 10
                result = num1 * i
                print(f"{num1} x {i} = {result}")

            print(f"\n--- Multiplication Table for {num2} ---")
            for i in range(1, 11): # Loop from 1 to 10
                result = num2 * i
                print(f"{num2} x {i} = {result}")

            # Ask if the user wants to generate tables for other numbers
            another_round = input("\nDo you want to generate tables for other numbers? (yes/no): ").strip().lower()
            if another_round != 'yes':
                print("Exiting table generator. Goodbye!")
                break # Exit the loop and end the program

        except ValueError:
            print("Invalid input. Please enter whole numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}. Please try again.")

if __name__ == "__main__":
    generate_two_number_tables()
