# Get angle from use and find its sin and cos value in radian
import math
angle = float(input("Enter angle: "))
sin_value = math.sin(angle)
cos_value = math.cos(angle)
print("Sin Value =" +str(sin_value)+" rad")
print("Cos Value =" +str(cos_value)+" rad")

angle1 = float(input("Enter angle: "))
sin_value1_rad = math.sin(angle)
cos_value1_rad = math.cos(angle)
print(cos_value1_rad)
print(sin_value1_rad)
sin_value1_deg = math.degrees(sin_value1_rad)
cos_value1_deg = math.degrees(cos_value1_rad)
print("Sin Value =" +str(sin_value1_deg)+" deg")
print("Cos Value =" +str(cos_value1_deg)+" deg")

import math

def calculate_trig_values():
    """
    Prompts the user for an angle in degrees, calculates its sine and cosine
    values (using radians internally), and then displays the results.
    It also shows the input angle's radian equivalent.
    """
    print("--- Angle Sine and Cosine Calculator ---")

    while True:
        try:
            # 1. Get an angle from the user in degrees
            angle_str = input("Please enter an angle in degrees: ")
            angle_degrees = float(angle_str)
            break  # Exit loop if input is a valid number
        except ValueError:
            print("Invalid input. Please enter a numerical value for the angle.")

    # 2. Convert the angle from degrees to radians
    # The math.sin() and math.cos() functions expect angles in radians.
    angle_radians = math.radians(angle_degrees)

    # 3. Find its Sin and Cos Value in Radian (calculation using radians)
    sin_value = math.sin(angle_radians)
    cos_value = math.cos(angle_radians)

    # 4. Display results. The problem statement "Convert Their Result Into Degree Unit"
    # is ambiguous for sin/cos *values* as they are unitless ratios.
    # The most logical interpretation is to display the original angle in degrees,
    # its radian equivalent, and the calculated sin/cos values clearly.
    # If the intention was to find the angle *from* the sin/cos values,
    # that would involve math.asin() or math.acos() and then math.degrees().
    # For this assignment, we'll stick to the common interpretation of showing
    # the input angle's representation and the calculated ratios.

    print(f"\n--- Results for Angle: {angle_degrees}° ---")
    print(f"Angle in Radians: {angle_radians:.4f} radians") # Display radians for context
    print(f"Sine (sin) of {angle_degrees}°: {sin_value:.4f}")
    print(f"Cosine (cos) of {angle_degrees}°: {cos_value:.4f}")

    # Optional: Demonstrate converting back from a sin/cos value to an angle in degrees
    # This part addresses the "convert their result into degree unit" more literally,
    # showing what angle has that sine/cosine, if that was the intent.
    # Note: asin/acos return values in radians, which then need to be converted to degrees.
    # Also, asin/acos only return values in a specific range (e.g., -90 to 90 for asin).
    try:
        angle_from_sin_degrees = math.degrees(math.asin(sin_value))
        print(f"\nAngle whose Sine is {sin_value:.4f}: {angle_from_sin_degrees:.4f}° (from asin)")
    except ValueError:
        print(f"\nCould not calculate angle from sine value (asin) for {sin_value:.4f}")

    try:
        angle_from_cos_degrees = math.degrees(math.acos(cos_value))
        print(f"Angle whose Cosine is {cos_value:.4f}: {angle_from_cos_degrees:.4f}° (from acos)")
    except ValueError:
        print(f"Could not calculate angle from cosine value (acos) for {cos_value:.4f}")

# Run the program
if __name__ == "__main__":
    calculate_trig_values()
