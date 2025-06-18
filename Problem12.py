# Create a shape in Python using for loop

for i in range(6): #0,1,2,3,4,5
    for j in range(i+1):
        print("*", end=" ")
    print("")
    
def generate_star_pattern():
    """
    Generates and displays a specific star pattern using a for loop,
    as depicted in the assignment image.
    """
    print("--- Star Pattern Generator ---")

    # The pattern appears to be:
    # ....*
    # ...**
    # ..***
    # .****
    # *****
    # The image shows a right-aligned triangle with height 5.

    height = 5 # The height of the triangle pattern

    for i in range(1, height + 1):
        # Calculate number of spaces: total height - current row number
        num_spaces = height - i
        # Calculate number of stars: current row number
        num_stars = i

        # Print spaces followed by stars
        print(" " * num_spaces + "*" * num_stars)

    print("\nPattern displayed successfully!")

if __name__ == "__main__":
    generate_star_pattern()

for i in range(6): #0,1,2,3,4,5
    for j in range(i-1):
        print("*", end=" ")
    print("")
    