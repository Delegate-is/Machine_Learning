# Program to convert Radian to Degree
fruits = ["Apple", "Banana", "Cherry", "Date"]  # Create a list of fruits
# # Print the list to see its elements. 
print("Fruits list:", fruits)  # Print the list of fruits
# # Add a new fruit to the list.
fruits.append("Elderberry")  # Add Elderberry to the list of fruits
# # Print the updated list.
print("Updated fruits list:", fruits)  # Print the updated list of fruits
# Program to convert Radian to Degree
import math  # Import the math module for mathematical operations
def radian_to_degree(radian):
    """
    Convert radians to degrees.
    
    Parameters:
    radian (float): The angle in radians.
    
    Returns:
    float: The angle in degrees.
    """
    return radian * (180 / math.pi)  # Convert radians to degrees
# Example usage
radian = float(input("Enter angle in radians: "))  # Get input from user
degree = radian_to_degree(radian)  # Convert radians to degrees
print(f"{radian} radians is equal to {degree} degrees")  # Display the result

rad = float(input("Enter radian value: "))  # Get radian value from user
deg = math.degrees(rad)
print(f"{str(rad)} radian is equal to {str(deg)} degree")  # Display the conversion result
deg_1 = float(input("Enter degree value: "))  # Get degree value from user
rad_1 = math.radians(deg_1)  # Convert degree to radian
print(f"{str(deg_1)} degree is equal to {str(rad_1)} radian")  # Display the conversion result