# get Temp in F
# Convert to K and C
f= float(input("Enter temp in F "))
# Formula F to C (F - 32) * 5/9 = C
f_to_c = (f - 32) * 5/9
print("Temp from F to C: "+ str(f_to_c) +"\n")
# Formula F to K (32F - 32) * 5/9 + 273.15 = 273.15K
f_to_k = f_to_c + 273.15
print("Temp from F to K: "+str(f_to_k))

def convert_temperature():
    """
    Prompts the user to enter a temperature in Centigrade (Celsius),
    then converts it to Fahrenheit and Kelvin, displaying the results.
    """
    print("--- Temperature Converter ---")

    while True:
        try:
            # Get temperature in Centigrade from the user
            temp_celsius_str = input("Enter temperature in Centigrade (°C): ")
            temp_celsius = float(temp_celsius_str)
            break  # Exit loop if input is a valid number
        except ValueError:
            print("Invalid input. Please enter a numerical value for the temperature.")

    # Convert Centigrade to Fahrenheit
    # Formula: F = (C * 9/5) + 32
    temp_fahrenheit = (temp_celsius * 9/5) + 32

    # Convert Centigrade to Kelvin
    # Formula: K = C + 273.15
    temp_kelvin = temp_celsius + 273.15

    print(f"\n--- Conversion Results ---")
    print(f"Centigrade (°C): {temp_celsius:.2f}")
    print(f"Fahrenheit (°F): {temp_fahrenheit:.2f}")
    print(f"Kelvin (K): {temp_kelvin:.2f}")

# Call the function to run the program
if __name__ == "__main__":
    convert_temperature()
