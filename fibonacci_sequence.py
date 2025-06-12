def fibonacci_sequence(n_terms):
    sequence = []
    a, b = 0, 1
    for _ in range(n_terms):
        sequence.append(a)
        a, b = b, a + b
    return sequence

if __name__ == "__main__":
    try:
        n = int(input("Enter the number of terms: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            print("Fibonacci sequence:")
            print(fibonacci_sequence(n))
    except ValueError:
        print("Invalid input. Please enter an integer.")
    def main():
    """
    Prompts the user for the number of Fibonacci terms and displays the sequence.
    """
    print("--- Fibonacci Sequence Generator ---")
    while True:
        try:
            num_terms_str = input("Enter the number of Fibonacci terms to generate (or 'exit' to quit): ")

            if num_terms_str.lower() == 'exit':
                print("Exiting Fibonacci Generator. Goodbye!")
                break

            num_terms = int(num_terms_str)

            if num_terms < 0:
                print("Please enter a non-negative number of terms.")
            else:
                fib_result = generate_fibonacci_iterative(num_terms)
                print(f"The first {num_terms} Fibonacci terms are: {fib_result}")

        except ValueError:
            print("Invalid input. Please enter a valid integer or 'exit'.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()