mm = float(input("Enter the length of the object (in mm): "))

m = mm / 1000  # Convert mm to meters
km = mm / 1000000  # Convert mm to kilometers
print("Length in meters:", m)
print("Length in kilometers:", km)
# Get length in cm and convert to m and km
def convert_length(cm):
    m = cm / 100  # Convert cm to meters
    km = cm / 1000  # Convert cm to kilometers
    return m, km
cm = float(input("Enter the length of the object (in cm): "))
m, km = convert_length(cm)
print("Length in meters:", m)
print("Length in kilometers:", km)