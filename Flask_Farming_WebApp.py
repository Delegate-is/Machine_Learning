# app.py
from flask import Flask, render_template_string, request, redirect, url_for, flash
import json
import os
from datetime import datetime

app = Flask(__name__)
# Flask requires a secret key for flashing messages
app.secret_key = 'your_super_secret_key_here' # Replace with a strong, random key in production

# --- Configuration ---
DATA_FILE = 'farm_data.json' # The file where crop and livestock data will be stored

# --- HTML Templates (Self-contained, repeating header/footer) ---

HEADER_HTML = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Farming App</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;600&display=swap" rel="stylesheet">
    <style>
        body {
            font-family: 'Inter', sans-serif;
            background-color: #f3f4f6; /* Light gray background */
        }
        .container {
            max-width: 960px;
        }
        table {
            width: 100%;
            border-collapse: collapse;
        }
        th, td {
            border: 1px solid #e5e7eb; /* Light gray border */
            padding: 12px 15px;
            text-align: left;
        }
        th {
            background-color: #e0f2fe; /* Light blue header */
            font-weight: 600;
            color: #1f2937; /* Dark gray text */
            text-transform: uppercase;
            font-size: 0.85rem;
        }
        tr:nth-child(even) {
            background-color: #f9fafb; /* Slightly darker for even rows */
        }
        tr:hover {
            background-color: #eef2ff; /* Light purple on hover */
        }
        .btn {
            display: inline-block;
            padding: 10px 20px;
            border-radius: 8px;
            font-weight: 600;
            text-decoration: none;
            transition: all 0.2s ease-in-out;
        }
        .btn-primary {
            background-color: #2563eb; /* Blue */
            color: white;
        }
        .btn-primary:hover {
            background-color: #1d4ed8; /* Darker blue */
        }
        .btn-secondary {
            background-color: #6b7280; /* Gray */
            color: white;
        }
        .btn-secondary:hover {
            background-color: #4b5563; /* Darker gray */
        }
        .alert {
            padding: 1rem;
            border-radius: 0.5rem;
            margin-bottom: 1rem;
        }
        .alert-success {
            background-color: #d1fae5; /* Light green */
            color: #065f46; /* Dark green text */
        }
        .alert-error {
            background-color: #fee2e2; /* Light red */
            color: #991b1b; /* Dark red text */
        }
    </style>
</head>
<body class="bg-gray-100 flex flex-col min-h-screen">
    <header class="bg-emerald-600 text-white p-4 shadow-md">
        <div class="container mx-auto flex justify-between items-center">
            <h1 class="text-2xl font-bold">Farming App</h1>
            <nav>
                <a href="{{ url_for('index') }}" class="text-white hover:text-emerald-200 mx-2">Crop Dashboard</a>
                <a href="{{ url_for('add_crop_form') }}" class="text-white hover:text-emerald-200 mx-2">Add Crop</a>
                <a href="{{ url_for('mark_harvest_form') }}" class="text-white hover:text-emerald-200 mx-2">Harvest Crop</a>
                <span class="text-emerald-200 mx-2">|</span> {# Separator #}
                <a href="{{ url_for('livestock_index') }}" class="text-white hover:text-emerald-200 mx-2">Livestock Dashboard</a>
                <a href="{{ url_for('add_livestock_form') }}" class="text-white hover:text-emerald-200 mx-2">Add Livestock</a>
                <a href="{{ url_for('record_breeding_form') }}" class="text-white hover:text-emerald-200 mx-2">Record Breeding</a>
                <a href="{{ url_for('record_birth_form') }}" class="text-white hover:text-emerald-200 mx-2">Record Birth</a>
            </nav>
        </div>
    </header>

    <main class="flex-grow container mx-auto p-6">
        {% with messages = get_flashed_messages(with_categories=true) %}
            {% if messages %}
                {% for category, message in messages %}
                    <div class="alert alert-{{ category }}">{{ message }}</div>
                {% endfor %}
            {% endif %}
        {% endwith %}
"""

FOOTER_HTML = """
    </main>

    <footer class="bg-gray-800 text-white p-4 text-center mt-auto shadow-inner">
        <div class="container mx-auto">
            &copy; 2025 Farming App. All rights reserved.
        </div>
    </footer>
</body>
</html>
"""

# --- Crop Management HTML ---
INDEX_HTML = HEADER_HTML + """
<div class="bg-white p-8 rounded-lg shadow-md mb-6">
    <h2 class="text-3xl font-bold text-gray-800 mb-4">Crop Dashboard</h2>
    <p class="text-gray-600 mb-6">Overview of your current farming operations.</p>

    <div class="flex space-x-4 mb-8">
        <a href="{{ url_for('add_crop_form') }}" class="btn btn-primary">Add New Crop</a>
        <a href="{{ url_for('mark_harvest_form') }}" class="btn btn-secondary">Mark Crop as Harvested</a>
    </div>

    <h3 class="text-2xl font-semibold text-gray-700 mb-4">All Crops</h3>
    {% if crops %}
    <div class="overflow-x-auto">
        <table class="min-w-full bg-white rounded-lg shadow-sm">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Type</th>
                    <th>Planting Date</th>
                    <th>Area</th>
                    <th>Status</th>
                    <th>Harvest Date</th>
                    <th>Yield</th>
                </tr>
            </thead>
            <tbody>
                {% for crop in crops %}
                <tr>
                    <td>{{ crop.id }}</td>
                    <td>{{ crop.type }}</td>
                    <td>{{ crop.planting_date }}</td>
                    <td>{{ "%.2f"|format(crop.area) }}</td>
                    <td><span class="px-2 py-1 rounded-full text-xs font-semibold
                        {% if crop.status == 'Planted' %} bg-yellow-100 text-yellow-800
                        {% elif crop.status == 'Harvested' %} bg-green-100 text-green-800
                        {% endif %}">{{ crop.status }}</span></td>
                    <td>{{ crop.harvest_date if crop.harvest_date else 'N/A' }}</td>
                    <td>{{ "%.2f"|format(crop.yield) if crop.yield is not none else 'N/A' }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
    {% else %}
    <p class="text-gray-600">No crop records found. Add your first crop!</p>
    {% endif %}
</div>
""" + FOOTER_HTML

ADD_CROP_HTML = HEADER_HTML + """
<div class="bg-white p-8 rounded-lg shadow-md">
    <h2 class="text-3xl font-bold text-gray-800 mb-4">Add New Crop</h2>
    <form method="POST" action="{{ url_for('add_crop_form') }}" class="space-y-4">
        <div>
            <label for="crop_type" class="block text-sm font-medium text-gray-700">Crop Type:</label>
            <input type="text" id="crop_type" name="crop_type" required
                   class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-emerald-500 focus:border-emerald-500">
        </div>
        <div>
            <label for="planting_date" class="block text-sm font-medium text-gray-700">Planting Date (YYYY-MM-DD):</label>
            <input type="date" id="planting_date" name="planting_date" required
                   class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-emerald-500 focus:border-emerald-500">
        </div>
        <div>
            <label for="area" class="block text-sm font-medium text-gray-700">Area Planted (e.g., acres/sq meters):</label>
            <input type="number" step="0.01" id="area" name="area" required
                   class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-emerald-500 focus:border-emerald-500">
        </div>
        <button type="submit" class="btn btn-primary w-full md:w-auto">Add Crop</button>
    </form>
</div>
""" + FOOTER_HTML

MARK_HARVEST_HTML = HEADER_HTML + """
<div class="bg-white p-8 rounded-lg shadow-md">
    <h2 class="text-3xl font-bold text-gray-800 mb-4">Mark Crop as Harvested</h2>
    {% if crops %}
    <p class="text-gray-600 mb-4">Select a crop ID from the list below to mark as harvested:</p>
    <div class="overflow-x-auto mb-6">
        <table class="min-w-full bg-white rounded-lg shadow-sm">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Type</th>
                    <th>Planting Date</th>
                    <th>Area</th>
                    <th>Status</th>
                </tr>
            </thead>
            <tbody>
                {% for crop in crops %}
                    {% if crop.status == 'Planted' %}
                    <tr>
                        <td>{{ crop.id }}</td>
                        <td>{{ crop.type }}</td>
                        <td>{{ crop.planting_date }}</td>
                        <td>{{ "%.2f"|format(crop.area) }}</td>
                        <td><span class="px-2 py-1 rounded-full text-xs font-semibold bg-yellow-100 text-yellow-800">{{ crop.status }}</span></td>
                    </tr>
                    {% endif %}
                {% endfor %}
            </tbody>
        </table>
    </div>
    {% else %}
    <p class="text-gray-600 mb-4">No planted crops to harvest.</p>
    {% endif %}

    <form method="POST" action="{{ url_for('mark_harvest_form') }}" class="space-y-4">
        <div>
            <label for="crop_id" class="block text-sm font-medium text-gray-700">Crop ID:</label>
            <input type="number" id="crop_id" name="crop_id" required
                   class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-emerald-500 focus:border-emerald-500">
        </div>
        <div>
            <label for="harvest_date" class="block text-sm font-medium text-gray-700">Harvest Date (YYYY-MM-DD):</label>
            <input type="date" id="harvest_date" name="harvest_date" required
                   class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-emerald-500 focus:border-emerald-500">
        </div>
        <div>
            <label for="yield_val" class="block text-sm font-medium text-gray-700">Yield (e.g., in kg, bushels):</label>
            <input type="number" step="0.01" id="yield_val" name="yield_val" required
                   class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-emerald-500 focus:border-emerald-500">
        </div>
        <button type="submit" class="btn btn-primary w-full md:w-auto">Mark Harvested</button>
    </form>
</div>
""" + FOOTER_HTML

# --- Livestock Management HTML ---

LIVESTOCK_INDEX_HTML = HEADER_HTML + """
<div class="bg-white p-8 rounded-lg shadow-md mb-6">
    <h2 class="text-3xl font-bold text-gray-800 mb-4">Livestock Dashboard</h2>
    <p class="text-gray-600 mb-6">Manage your farm's livestock here.</p>

    <div class="flex space-x-4 mb-8">
        <a href="{{ url_for('add_livestock_form') }}" class="btn btn-primary">Add New Livestock</a>
        <a href="{{ url_for('record_breeding_form') }}" class="btn btn-secondary">Record Breeding</a>
        <a href="{{ url_for('record_birth_form') }}" class="btn btn-secondary">Record Birth</a>
    </div>

    <h3 class="text-2xl font-semibold text-gray-700 mb-4">All Livestock</h3>
    {% if livestock %}
    <div class="overflow-x-auto">
        <table class="min-w-full bg-white rounded-lg shadow-sm">
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Type</th>
                    <th>Breed</th>
                    <th>Gender</th>
                    <th>Birth Date</th>
                    <th>Status</th>
                    <th>Notes</th>
                </tr>
            </thead>
            <tbody>
                {% for animal in livestock %}
                <tr>
                    <td>{{ animal.id }}</td>
                    <td>{{ animal.type }}</td>
                    <td>{{ animal.breed }}</td>
                    <td>{{ animal.gender }}</td>
                    <td>{{ animal.birth_date }}</td>
                    <td><span class="px-2 py-1 rounded-full text-xs font-semibold
                        {% if animal.status == 'Active' %} bg-green-100 text-green-800
                        {% elif animal.status == 'Bred' %} bg-blue-100 text-blue-800
                        {% elif animal.status == 'Pregnant' %} bg-purple-100 text-purple-800
                        {% elif animal.status == 'Sold' %} bg-red-100 text-red-800
                        {% endif %}">{{ animal.status }}</span></td>
                    <td>{{ animal.notes if animal.notes else 'N/A' }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>
    </div>
    {% else %}
    <p class="text-gray-600">No livestock records found. Add your first animal!</p>
    {% endif %}
</div>
""" + FOOTER_HTML

ADD_LIVESTOCK_HTML = HEADER_HTML + """
<div class="bg-white p-8 rounded-lg shadow-md">
    <h2 class="text-3xl font-bold text-gray-800 mb-4">Add New Livestock</h2>
    <form method="POST" action="{{ url_for('add_livestock_form') }}" class="space-y-4">
        <div>
            <label for="animal_type" class="block text-sm font-medium text-gray-700">Type (e.g., Cow, Pig, Chicken):</label>
            <input type="text" id="animal_type" name="animal_type" required
                   class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-emerald-500 focus:border-emerald-500">
        </div>
        <div>
            <label for="breed" class="block text-sm font-medium text-gray-700">Breed:</label>
            <input type="text" id="breed" name="breed"
                   class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-emerald-500 focus:border-emerald-500">
        </div>
        <div>
            <label for="gender" class="block text-sm font-medium text-gray-700">Gender:</label>
            <select id="gender" name="gender" required
                    class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-emerald-500 focus:border-emerald-500">
                <option value="">Select Gender</option>
                <option value="Male">Male</option>
                <option value="Female">Female</option>
            </select>
        </div>
        <div>
            <label for="birth_date" class="block text-sm font-medium text-gray-700">Birth Date (YYYY-MM-DD):</label>
            <input type="date" id="birth_date" name="birth_date" required
                   class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-emerald-500 focus:border-emerald-500">
        </div>
        <div>
            <label for="notes" class="block text-sm font-medium text-gray-700">Notes:</label>
            <textarea id="notes" name="notes" rows="3"
                      class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-emerald-500 focus:border-emerald-500"></textarea>
        </div>
        <button type="submit" class="btn btn-primary w-full md:w-auto">Add Livestock</button>
    </form>
</div>
""" + FOOTER_HTML

RECORD_BREEDING_HTML = HEADER_HTML + """
<div class="bg-white p-8 rounded-lg shadow-md">
    <h2 class="text-3xl font-bold text-gray-800 mb-4">Record Breeding Event</h2>
    <p class="text-gray-600 mb-4">Select the female and male involved in the breeding.</p>

    {% if females and males %}
    <form method="POST" action="{{ url_for('record_breeding_form') }}" class="space-y-4">
        <div>
            <label for="female_id" class="block text-sm font-medium text-gray-700">Female ID:</label>
            <select id="female_id" name="female_id" required
                    class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-emerald-500 focus:border-emerald-500">
                <option value="">Select Female</option>
                {% for animal in females %}
                    <option value="{{ animal.id }}">{{ animal.id }} - {{ animal.type }} ({{ animal.breed }})</option>
                {% endfor %}
            </select>
        </div>
        <div>
            <label for="male_id" class="block text-sm font-medium text-gray-700">Male ID:</label>
            <select id="male_id" name="male_id" required
                    class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-emerald-500 focus:border-emerald-500">
                <option value="">Select Male</option>
                {% for animal in males %}
                    <option value="{{ animal.id }}">{{ animal.id }} - {{ animal.type }} ({{ animal.breed }})</option>
                {% endfor %}
            </select>
        </div>
        <div>
            <label for="breeding_date" class="block text-sm font-medium text-gray-700">Breeding Date (YYYY-MM-DD):</label>
            <input type="date" id="breeding_date" name="breeding_date" required
                   class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-emerald-500 focus:border-emerald-500">
        </div>
        <div>
            <label for="expected_birth_date" class="block text-sm font-medium text-gray-700">Expected Birth Date (YYYY-MM-DD, optional):</label>
            <input type="date" id="expected_birth_date" name="expected_birth_date"
                   class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-emerald-500 focus:border-emerald-500">
        </div>
        <button type="submit" class="btn btn-primary w-full md:w-auto">Record Breeding</button>
    </form>
    {% else %}
    <p class="text-gray-600">Please add at least one male and one female livestock before recording breeding.</p>
    {% endif %}
</div>
""" + FOOTER_HTML

RECORD_BIRTH_HTML = HEADER_HTML + """
<div class="bg-white p-8 rounded-lg shadow-md">
    <h2 class="text-3xl font-bold text-gray-800 mb-4">Record Birth Event</h2>
    <p class="text-gray-600 mb-4">Record the birth of new offspring.</p>

    {% if breeding_females %}
    <form method="POST" action="{{ url_for('record_birth_form') }}" class="space-y-4">
        <div>
            <label for="mother_id" class="block text-sm font-medium text-gray-700">Mother ID:</label>
            <select id="mother_id" name="mother_id" required
                    class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-emerald-500 focus:border-emerald-500">
                <option value="">Select Mother</option>
                {% for animal in breeding_females %}
                    <option value="{{ animal.id }}">{{ animal.id }} - {{ animal.type }} ({{ animal.breed }})</option>
                {% endfor %}
            </select>
        </div>
        <div>
            <label for="birth_date" class="block text-sm font-medium text-gray-700">Birth Date (YYYY-MM-DD):</label>
            <input type="date" id="birth_date" name="birth_date" required
                   class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-emerald-500 focus:border-emerald-500">
        </div>
        <div>
            <label for="num_offspring" class="block text-sm font-medium text-gray-700">Number of Offspring:</label>
            <input type="number" id="num_offspring" name="num_offspring" min="1" required value="1"
                   class="mt-1 block w-full border border-gray-300 rounded-md shadow-sm p-2 focus:ring-emerald-500 focus:border-emerald-500">
        </div>
        <p class="text-gray-600 text-sm italic">You can add details for each offspring after recording the birth.</p>
        <button type="submit" class="btn btn-primary w-full md:w-auto">Record Birth</button>
    </form>
    {% else %}
    <p class="text-gray-600">No female livestock recorded as 'Bred' or 'Pregnant' to record birth for.</p>
    {% endif %}
</div>
""" + FOOTER_HTML


# --- Data Management ---

def load_data():
    """Loads crop and livestock data from the JSON file."""
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                data = json.load(f)
                # Ensure livestock and next_livestock_id exist, initialize if not
                if "livestock" not in data:
                    data["livestock"] = []
                if "next_livestock_id" not in data:
                    data["next_livestock_id"] = 1
                return data
        except json.JSONDecodeError:
            app.logger.error(f"Error decoding JSON from {DATA_FILE}. Starting with empty data.")
            return {"crops": [], "next_crop_id": 1, "livestock": [], "next_livestock_id": 1}
    return {"crops": [], "next_crop_id": 1, "livestock": [], "next_livestock_id": 1} # Return initial structure if file doesn't exist

def save_data(data):
    """Saves crop and livestock data to the JSON file."""
    try:
        with open(DATA_FILE, 'w') as f:
            json.dump(data, f, indent=4)
    except IOError as e:
        app.logger.error(f"Error saving data to {DATA_FILE}: {e}")
        return False
    return True

# Helper to find livestock by ID
def find_livestock_by_id(data, animal_id):
    for animal in data["livestock"]:
        if animal["id"] == animal_id:
            return animal
    return None

# --- Flask Routes (Crop Management) ---

@app.route('/')
def index():
    """Main dashboard showing all crops."""
    farm_data = load_data()
    return render_template_string(INDEX_HTML, crops=farm_data["crops"])

@app.route('/add', methods=['GET', 'POST'])
def add_crop_form():
    """Handles displaying the add crop form and processing its submission."""
    if request.method == 'POST':
        farm_data = load_data()
        crop_type = request.form['crop_type'].strip()
        planting_date_str = request.form['planting_date'].strip()
        area_str = request.form['area'].strip()

        if not crop_type:
            flash('Crop type cannot be empty.', 'error')
            return redirect(url_for('add_crop_form'))

        try:
            datetime.strptime(planting_date_str, '%Y-%m-%d')
        except ValueError:
            flash('Invalid planting date format. Please use YYYY-MM-DD.', 'error')
            return redirect(url_for('add_crop_form'))

        try:
            area = float(area_str)
            if area <= 0:
                flash('Area must be a positive number.', 'error')
                return redirect(url_for('add_crop_form'))
        except ValueError:
            flash('Invalid input for area. Please enter a number.', 'error')
            return redirect(url_for('add_crop_form'))

        crop_id = farm_data["next_crop_id"]
        new_crop = {
            "id": crop_id,
            "type": crop_type,
            "planting_date": planting_date_str,
            "area": area,
            "status": "Planted",
            "harvest_date": None,
            "yield": None
        }
        farm_data["crops"].append(new_crop)
        farm_data["next_crop_id"] += 1

        if save_data(farm_data):
            flash(f"Crop '{crop_type}' (ID: {crop_id}) added successfully!", 'success')
        else:
            flash("Failed to save crop data. Check server logs.", 'error')
        return redirect(url_for('index')) # Redirect to dashboard after adding

    return render_template_string(ADD_CROP_HTML)

@app.route('/harvest', methods=['GET', 'POST'])
def mark_harvest_form():
    """Handles displaying the mark harvest form and processing its submission."""
    farm_data = load_data()
    planted_crops = [crop for crop in farm_data["crops"] if crop["status"] == "Planted"]

    if request.method == 'POST':
        crop_id_str = request.form['crop_id'].strip()
        harvest_date_str = request.form['harvest_date'].strip()
        yield_str = request.form['yield_val'].strip()

        try:
            crop_id_to_harvest = int(crop_id_str)
        except ValueError:
            flash('Invalid Crop ID. Please enter a number.', 'error')
            return redirect(url_for('mark_harvest_form'))

        found_crop = None
        for crop in farm_data["crops"]:
            if crop["id"] == crop_id_to_harvest:
                found_crop = crop
                break

        if not found_crop:
            flash(f"Crop with ID {crop_id_to_harvest} not found.", 'error')
            return redirect(url_for('mark_harvest_form'))

        if found_crop["status"] == "Harvested":
            flash(f"Crop ID {crop_id_to_harvest} is already marked as harvested.", 'error')
            return redirect(url_for('mark_harvest_form'))

        try:
            datetime.strptime(harvest_date_str, '%Y-%m-%d')
        except ValueError:
            flash('Invalid harvest date format. Please use YYYY-MM-DD.', 'error')
            return redirect(url_for('mark_harvest_form'))

        try:
            yield_val = float(yield_str)
            if yield_val < 0:
                flash("Yield cannot be negative.", 'error')
                return redirect(url_for('mark_harvest_form'))
        except ValueError:
            flash('Invalid input for yield. Please enter a number.', 'error')
            return redirect(url_for('mark_harvest_form'))

        found_crop["status"] = "Harvested"
        found_crop["harvest_date"] = harvest_date_str
        found_crop["yield"] = yield_val

        if save_data(farm_data):
            flash(f"Crop '{found_crop['type']}' (ID: {found_crop['id']}) marked as harvested with yield: {yield_val}.", 'success')
        else:
            flash("Failed to save crop data. Check server logs.", 'error')
        return redirect(url_for('index')) # Redirect to dashboard after harvesting

    return render_template_string(MARK_HARVEST_HTML, crops=planted_crops)

# --- Flask Routes (Livestock Management) ---

@app.route('/livestock')
def livestock_index():
    """Livestock dashboard showing all animals."""
    farm_data = load_data()
    return render_template_string(LIVESTOCK_INDEX_HTML, livestock=farm_data["livestock"])

@app.route('/livestock/add', methods=['GET', 'POST'])
def add_livestock_form():
    """Handles displaying the add livestock form and processing its submission."""
    if request.method == 'POST':
        farm_data = load_data()
        animal_type = request.form['animal_type'].strip()
        breed = request.form.get('breed', '').strip() # breed is optional
        gender = request.form['gender'].strip()
        birth_date_str = request.form['birth_date'].strip()
        notes = request.form.get('notes', '').strip()

        if not animal_type or not gender or not birth_date_str:
            flash('Type, Gender, and Birth Date are required fields.', 'error')
            return redirect(url_for('add_livestock_form'))

        if gender not in ["Male", "Female"]:
            flash('Gender must be Male or Female.', 'error')
            return redirect(url_for('add_livestock_form'))

        try:
            datetime.strptime(birth_date_str, '%Y-%m-%d')
        except ValueError:
            flash('Invalid birth date format. Please use YYYY-MM-DD.', 'error')
            return redirect(url_for('add_livestock_form'))

        animal_id = farm_data["next_livestock_id"]
        new_animal = {
            "id": animal_id,
            "type": animal_type,
            "breed": breed,
            "gender": gender,
            "birth_date": birth_date_str,
            "status": "Active", # Default status
            "notes": notes,
            "breeding_history": [], # To store breeding records
            "offspring_history": [] # To store offspring IDs
        }
        farm_data["livestock"].append(new_animal)
        farm_data["next_livestock_id"] += 1

        if save_data(farm_data):
            flash(f"Livestock '{animal_type}' (ID: {animal_id}) added successfully!", 'success')
        else:
            flash("Failed to save livestock data. Check server logs.", 'error')
        return redirect(url_for('livestock_index'))

    return render_template_string(ADD_LIVESTOCK_HTML)

@app.route('/livestock/breed', methods=['GET', 'POST'])
def record_breeding_form():
    """Handles displaying the record breeding form and processing its submission."""
    farm_data = load_data()
    females = [animal for animal in farm_data["livestock"] if animal["gender"] == "Female" and animal["status"] == "Active"]
    males = [animal for animal in farm_data["livestock"] if animal["gender"] == "Male" and animal["status"] == "Active"]

    if request.method == 'POST':
        female_id_str = request.form['female_id'].strip()
        male_id_str = request.form['male_id'].strip()
        breeding_date_str = request.form['breeding_date'].strip()
        expected_birth_date_str = request.form.get('expected_birth_date', '').strip()

        try:
            female_id = int(female_id_str)
            male_id = int(male_id_str)
        except ValueError:
            flash('Invalid ID. Please enter numbers.', 'error')
            return redirect(url_for('record_breeding_form'))

        female_animal = find_livestock_by_id(farm_data, female_id)
        male_animal = find_livestock_by_id(farm_data, male_id)

        if not female_animal or female_animal["gender"] != "Female" or female_animal["status"] != "Active":
            flash(f"Female with ID {female_id} not found or not active.", 'error')
            return redirect(url_for('record_breeding_form'))
        if not male_animal or male_animal["gender"] != "Male" or male_animal["status"] != "Active":
            flash(f"Male with ID {male_id} not found or not active.", 'error')
            return redirect(url_for('record_breeding_form'))

        try:
            datetime.strptime(breeding_date_str, '%Y-%m-%d')
            if expected_birth_date_str:
                datetime.strptime(expected_birth_date_str, '%Y-%m-%d')
        except ValueError:
            flash('Invalid date format. Please use YYYY-MM-DD.', 'error')
            return redirect(url_for('record_breeding_form'))

        breeding_record = {
            "mate_id": male_id,
            "breeding_date": breeding_date_str,
            "expected_birth_date": expected_birth_date_str if expected_birth_date_str else None,
            "status": "Bred"
        }
        female_animal["breeding_history"].append(breeding_record)
        # Optionally update female status to 'Bred' or 'Pregnant'
        female_animal["status"] = "Bred" # Or 'Pregnant' if you want a more distinct status

        if save_data(farm_data):
            flash(f"Breeding recorded for Female ID {female_id} with Male ID {male_id} on {breeding_date_str}.", 'success')
        else:
            flash("Failed to save breeding data. Check server logs.", 'error')
        return redirect(url_for('livestock_index'))

    return render_template_string(RECORD_BREEDING_HTML, females=females, males=males)

@app.route('/livestock/birth', methods=['GET', 'POST'])
def record_birth_form():
    """Handles displaying the record birth form and processing its submission."""
    farm_data = load_data()
    # Only show females marked as bred or pregnant for birth records
    breeding_females = [animal for animal in farm_data["livestock"] if animal["gender"] == "Female" and animal["status"] in ["Bred", "Pregnant"]]

    if request.method == 'POST':
        mother_id_str = request.form['mother_id'].strip()
        birth_date_str = request.form['birth_date'].strip()
        num_offspring_str = request.form['num_offspring'].strip()

        try:
            mother_id = int(mother_id_str)
            num_offspring = int(num_offspring_str)
            if num_offspring <= 0:
                flash('Number of offspring must be a positive integer.', 'error')
                return redirect(url_for('record_birth_form'))
        except ValueError:
            flash('Invalid input for ID or number of offspring. Please enter numbers.', 'error')
            return redirect(url_for('record_birth_form'))

        mother_animal = find_livestock_by_id(farm_data, mother_id)

        if not mother_animal or mother_animal["gender"] != "Female":
            flash(f"Mother with ID {mother_id} not found or is not a female.", 'error')
            return redirect(url_for('record_birth_form'))

        try:
            datetime.strptime(birth_date_str, '%Y-%m-%d')
        except ValueError:
            flash('Invalid birth date format. Please use YYYY-MM-DD.', 'error')
            return redirect(url_for('record_birth_form'))

        # Update mother's status
        mother_animal["status"] = "Active" # Or 'Lactating'/'Nursing' if more detailed statuses are added

        offspring_ids = []
        for _ in range(num_offspring):
            new_offspring_id = farm_data["next_livestock_id"]
            offspring_animal = {
                "id": new_offspring_id,
                "type": mother_animal["type"], # Assume same type as mother for simplicity
                "breed": mother_animal["breed"], # Assume same breed
                "gender": "Unknown", # Gender can be updated later via an edit feature
                "birth_date": birth_date_str,
                "status": "Active",
                "notes": f"Born from Mother ID: {mother_id}",
                "breeding_history": [],
                "offspring_history": []
            }
            farm_data["livestock"].append(offspring_animal)
            offspring_ids.append(new_offspring_id)
            farm_data["next_livestock_id"] += 1

        mother_animal["offspring_history"].extend(offspring_ids)

        if save_data(farm_data):
            flash(f"Birth recorded for Mother ID {mother_id} on {birth_date_str}. {num_offspring} offspring added (IDs: {', '.join(map(str, offspring_ids))}).", 'success')
        else:
            flash("Failed to save birth data. Check server logs.", 'error')
        return redirect(url_for('livestock_index'))

    return render_template_string(RECORD_BIRTH_HTML, breeding_females=breeding_females)

# --- Application Entry Point ---
if __name__ == '__main__':
    app.run(debug=True) # Run the Flask development server
