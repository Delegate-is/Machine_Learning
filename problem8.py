# Find diff of two sets

print("Difference of two sets")
A = {23,5,1,12,4,6,7}
B = {6,11,124,5,2,15,21,22,33}
C = B.difference(A)
print(C)

def calculate_symmetric_difference():
    """
    Calculates and displays the symmetric difference of two predefined sets.
    """
    print("--- Symmetric Difference Calculator ---")

    # Define the two sets as given in the assignment
    set_a = {12, 2, 0, 3, 8}
    set_b = {15, 10, 12, 3, 6}

    print(f"Set A: {set_a}")
    print(f"Set B: {set_b}")

    # Calculate the symmetric difference
    # Method 1: Using the symmetric_difference() method
    symmetric_diff_method = set_a.symmetric_difference(set_b)
    print(f"\nSymmetric Difference (using .symmetric_difference()): {symmetric_diff_method}")

    # Method 2: Using the ^ operator (more concise)
    symmetric_diff_operator = set_a ^ set_b
    print(f"Symmetric Difference (using ^ operator): {symmetric_diff_operator}")

    print("\nExplanation:")
    print("The symmetric difference of two sets A and B is the set of elements that are in either A or B, but not in their intersection (i.e., not in both).")
    print("In simpler terms, it's all unique elements from both sets combined.")
    print(f"Elements unique to A: {set_a - set_b}")
    print(f"Elements unique to B: {set_b - set_a}")
    print(f"Combined unique elements: {(set_a - set_b).union(set_b - set_a)}")


if __name__ == "__main__":
    calculate_symmetric_difference()
