import csv

def create_number_csv(start, end, filename):
    """
    Creates a CSV file with a single column containing a range of numbers.

    Args:
        start (int): The starting number of the range (inclusive).
        end (int): The ending number of the range (inclusive).
        filename (str): The name of the CSV file to be created.
    """
    try:
        # Open the file in write mode ('w'). The newline='' argument is crucial
        # to prevent extra blank rows on some operating systems.
        with open(filename, 'w', newline='') as file:
            # Create a writer object
            writer = csv.writer(file)

            # Write the header row
            writer.writerow(['Number'])

            # Iterate through the range of numbers and write each one to a new row
            for number in range(start, end + 1):
                writer.writerow([number])

        print(f"Successfully created '{filename}' with numbers from {start} to {end}.")
    
    except IOError as e:
        print(f"An error occurred while writing the file: {e}")

# Call the function to create the CSV file
# The numbers will be from 100 to 200, inclusive
create_number_csv(100, 200, 'numbers.csv')

# Program to get current user of computer
import os
c_user = os.getlogin()
print(c_user)
import psutil

def get_ram_info():
    """
    Retrieves and prints detailed RAM information.
    """
    print("--- RAM Information ---")
    
    # Get the memory details
    ram = psutil.virtual_memory()

    # Convert bytes to gigabytes for readability
    total_ram_gb = ram.total / (1024 ** 3)
    used_ram_gb = ram.used / (1024 ** 3)
    free_ram_gb = ram.free / (1024 ** 3)
    
    print(f"Total: {total_ram_gb:.2f} GB")
    print(f"Used: {used_ram_gb:.2f} GB")
    print(f"Free: {free_ram_gb:.2f} GB")
    print(f"Used Percentage: {ram.percent}%")

def get_cpu_info():
    """
    Retrieves and prints detailed CPU information.
    """
    print("\n--- CPU Information ---")

    # Get the CPU usage as a percentage. The interval=1 argument means
    # it will wait for 1 second to get a meaningful value.
    cpu_percent = psutil.cpu_percent(interval=1)
    
    # Get the number of physical and logical cores
    logical_cores = psutil.cpu_count(logical=True)
    physical_cores = psutil.cpu_count(logical=False)

    print(f"CPU Usage: {cpu_percent}%")
    print(f"Physical Cores: {physical_cores}")
    print(f"Logical Cores: {logical_cores}")

# Call the functions to get and display the information
if __name__ == "__main__":
    get_ram_info()
    get_cpu_info()
