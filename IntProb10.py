# Get gravity force
n1 = float(input("Enter the mass of the first object (in kg): "))
n2 = float(input("Enter the mass of the second object (in kg): "))
r = float(input("Enter the radius(in meters): "))
product = n1 * n2
G = 0.00000000006674  # Gravitational constant
force = ((G * product))/ (r * r)
print("The gravitational force between the objects is:", force, "N")
# find columb force between two charges
q1 = float(input("Enter the charge of the first object (in coulombs): "))
q2 = float(input("Enter the charge of the second object (in coulombs): "))
r = float(input("Enter the distance between the charges (in meters): "))
k = 8.9875517873681764e9  # Coulomb's constant
force_coulomb = (k * q1 * q2) / (r * r)
print("The Coulomb force between the charges is:", force_coulomb, "N")
