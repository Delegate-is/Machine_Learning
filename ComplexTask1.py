# Get sent from user, find len, total char, no of words with and without space
sent = input("Enter a Sentence: ")
total_char_with_space = len(sent)
spaces = 0
for i in range(0, total_char_with_space):
    if sent[i] == " ":
        spaces +=1
total_vowel_char_with_spaces = 0
total_char_without_spaces = total_char_with_space-spaces
for i in range(0, total_char_with_space):
    if sent[i] == "a" or sent[i] == "e" or sent[i] == "i" or sent[i] == "o" or sent[i] == "u":
        total_vowel_char_with_spaces +=1
print(total_vowel_char_with_spaces)
total_words = spaces + 1
print("Total Char with space " +str(total_char_with_space))
print("Total Char without space "+str(total_char_without_spaces))
print("Total words "+str(total_words))
print("Total spaces "+str(spaces))
# Find roots of Quadratic Equation
# get a,b,c then r = b**2-4*a*c
from math import sqrt
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))
r = b*b-4*a*c
print(r)
if r > 0:
    x1 = (-b + sqrt(r))/2*a
    x2 = (-b - sqrt(r))/2*a
    print("There are two roots")
elif r == 0:
    x = -b/2*a
    print("There is one root")
else:
    print("There are no roots")
    
import cmath # Import cmath for handling complex numbers (for negative discriminant)

def find_quadratic_roots(a, b, c):
    """
    Calculates the roots of a quadratic equation ax^2 + bx + c = 0.

    Args:
        a (float): Coefficient of x^2.
        b (float): Coefficient of x.
        c (float): Constant term.

    Returns:
        tuple: A tuple containing the roots of the equation.
               Returns (root,) if there's one real root.
               Returns (root1, root2) if there are two real or complex roots.
               Returns an error message if 'a' is zero (not a quadratic equation).
    """
    if a == 0:
        return "Error: 'a' cannot be zero for a quadratic equation."

    discriminant = (b**2) - 4*(a*c)

    if discriminant > 0:
        # Two distinct real roots
        root1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        # One real root (repeated)
        root = -b / (2 * a)
        return root,
    else:
        # Two complex roots
        root1 = (-b - cmath.sqrt(discriminant)) / (2 * a)
        root2 = (-b + cmath.sqrt(discriminant)) / (2 * a)
        return root1, root2

# Example usage:
a_val = float(input("Enter coefficient 'a': "))
b_val = float(input("Enter coefficient 'b': "))
c_val = float(input("Enter coefficient 'c': "))

roots = find_quadratic_roots(a_val, b_val, c_val)

if isinstance(roots, str):
    print(roots)
else:
    print(f"The roots of the quadratic equation are: {roots}")