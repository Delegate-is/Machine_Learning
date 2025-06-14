import json
import os
from datetime import datetime

# --- Configuration ---
DATA_FILE = 'farm_data.json' # The file where crop data will be stored

# --- Data Management ---

def load_data():
    """Loads crop data from the JSON file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                return json.load(f)
        except json.JSONDecodeError:
            print("Warning: Data file corrupted or empty. Starting with empty data.")
            return {"crops": [], "next_crop_id": 1}
    return {"crops": [], "next_crop_id": 1} # Return initial structure if file doesn't exist

def save_data(data):
    """Saves crop data to the JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)
    print("Data saved successfully.")

# --- Core Application Functions ---

def display_main_menu():
    """Displays the main menu options to the user."""
    print("\n--- Farming App Menu ---")
    print("1. Add New Crop")
    print("2. View All Crops")
    print("3. Mark Crop as Harvested")
    print("4. Exit")
    print("------------------------")

def add_crop(data):
    """Prompts the user for new crop details and adds it to the data."""
    print("\n--- Add New Crop ---")
    crop_type = input("Enter crop type (e.g., Maize, Beans, Wheat): ").strip()
    if not crop_type:
        print("Crop type cannot be empty. Operation cancelled.")
        return

    while True:
        planting_date_str = input("Enter planting date (YYYY-MM-DD): ").strip()
        try:
            # Validate date format
            datetime.strptime(planting_date_str, '%Y-%m-%d')
            break
        except ValueError:
            print("Invalid date format. Please use YYYY-MM-DD.")

    while True:
        try:
            area = float(input("Enter area planted (in acres or sq meters): ").strip())
            if area <= 0:
                print("Area must be a positive number.")
                continue
            break
        except ValueError:
            print("Invalid input for area. Please enter a number.")

    crop_id = data["next_crop_id"]
    new_crop = {
        "id": crop_id,
        "type": crop_type,
        "planting_date": planting_date_str,
        "area": area,
        "status": "Planted",
        "harvest_date": None,
        "yield": None
    }
    data["crops"].append(new_crop)
    data["next_crop_id"] += 1
    print(f"Crop '{crop_type}' (ID: {crop_id}) added successfully!")

def view_all_crops(data):
    """Displays all current crop records in a formatted table."""
    print("\n--- All Crops ---")
    if not data["crops"]:
        print("No crop records found.")
        return

    # Print header
    print(f"{'ID':<4} | {'Type':<15} | {'Planting Date':<15} | {'Area':<10} | {'Status':<10} | {'Harvest Date':<15} | {'Yield':<10}")
    print("-" * 90) # Separator line

    # Print each crop record
    for crop in data["crops"]:
        harvest_date = crop.get('harvest_date', 'N/A') or 'N/A' # Handle None or missing key
        yield_val = crop.get('yield', 'N/A')
        if yield_val is None: yield_val = 'N/A'

        print(f"{crop['id']:<4} | {crop['type']:<15} | {crop['planting_date']:<15} | {crop['area']:<10.2f} | {crop['status']:<10} | {harvest_date:<15} | {str(yield_val):<10}")
    print("-" * 90)

def mark_crop_as_harvested(data):
    """Allows the user to mark a crop as harvested and record its yield."""
    print("\n--- Mark Crop as Harvested ---")
    view_all_crops(data) # Show existing crops first

    if not data["crops"]:
        print("No crops to harvest.")
        return

    while True:
        try:
            crop_id_to_harvest = int(input("Enter the ID of the crop to mark as harvested: ").strip())
            break
        except ValueError:
            print("Invalid input. Please enter a valid crop ID (a number).")

    found_crop = None
    for crop in data["crops"]:
        if crop["id"] == crop_id_to_harvest:
            found_crop = crop
            break

    if found_crop:
        if found_crop["status"] == "Harvested":
            print(f"Crop ID {crop_id_to_harvest} is already marked as harvested.")
            return

        while True:
            harvest_date_str = input("Enter harvest date (YYYY-MM-DD): ").strip()
            try:
                datetime.strptime(harvest_date_str, '%Y-%m-%d')
                break
            except ValueError:
                print("Invalid date format. Please use YYYY-MM-DD.")

        while True:
            try:
                yield_val = float(input("Enter yield (e.g., in kg, bushels, etc.): ").strip())
                if yield_val < 0:
                    print("Yield cannot be negative.")
                    continue
                break
            except ValueError:
                print("Invalid input for yield. Please enter a number.")

        found_crop["status"] = "Harvested"
        found_crop["harvest_date"] = harvest_date_str
        found_crop["yield"] = yield_val
        print(f"Crop '{found_crop['type']}' (ID: {found_crop['id']}) marked as harvested with yield: {yield_val}.")
    else:
        print(f"Crop with ID {crop_id_to_harvest} not found.")

# --- Main Application Loop ---

def run_app():
    """Main function to run the farming application."""
    farm_data = load_data() # Load data when the app starts

    while True:
        display_main_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == '1':
            add_crop(farm_data)
        elif choice == '2':
            view_all_crops(farm_data)
        elif choice == '3':
            mark_crop_as_harvested(farm_data)
        elif choice == '4':
            save_data(farm_data) # Save data before exiting
            print("Thank you for using the Farming App. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

# --- Application Entry Point ---

if __name__ == "__main__":
    run_app()
