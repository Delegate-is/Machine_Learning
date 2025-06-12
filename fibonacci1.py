def generate_fibonacci_iterative(n_terms):
    """
    Generates the 1st n-terms of Fibonacci sequence iteratively.
    Args:
        n_terms(int): The number of terms to generate in the sequence.
        
    Retuns:
        List: a list containing the Fibonacci sequence up to n_terms.
        Returns and empty list if n_terms is 0 or negative.
    """
    if n_terms <= 0:
        return []
    elif n_terms == 1:
        return [0]
    else:
        Fibonacci_sequence = [0, 1] # Intialize the first two terms
        # Loop to generate subsequent terms
        for i in range(2, n_terms):
            next_term = Fibonacci_sequence[i - 1] + Fibonacci_sequence[i - 2]
            Fibonacci_sequence.append(next_term)
        return Fibonacci_sequence
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