# pip install -r requirements.txt
""" 1. Type 'python' in your terminal and press Enter
from app import app, db
#after new updates to models.py, run this to refresh your database tables with the new relationships:
with app.app_context():
    # Warning: This deletes existing data to apply the new schema
    db.drop_all() 
    db.create_all()
    print("Database tables refreshed with new relationships!")"""
# flask --app app run --debug
from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from database import db
from datetime import datetime, timedelta
from datetime import date
from collections import defaultdict
from models import MilkProduction, Transaction, Cow, Vaccination, Breeding, Crop, Feed, HealthRecord, Inventory, CalfHealth
from analytics import monthly_milk_data, revenue_vs_expense, cow_profitability # crop_roi_analysis
from projection import three_year_projection
from analytics import feed_efficiency_model
from analytics import cow_feed_efficiency
from yoghurt_engine import yoghurt_profit_analysis
from valuation_engine import farm_valuation
from version import increment_version
from project_state import load_state
from flask import jsonify
from flask_migrate import Migrate
import os
import glob
# Email setup for notifications (e.g., calving alerts, health issues)
from flask_mail import Mail, Message

app = Flask(__name__)
app.config.from_object(Config)
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = 'ariallogistics@gmail.com'
app.config['MAIL_PASSWORD'] = 'your-app-password'
mail = Mail(app)
app.secret_key = 'dev-key-njuwan-farm-2026' # Add this line!

# 3. Initialize the app with the db instance
db.init_app(app)

with app.app_context():
    # This creates the tables based on tag_number and other fields in models.py
    db.create_all()
migrate = Migrate(app, db)
#flask db init
#flask db migrate -m "added planting_date"
#flask db upgrade  

current_version = increment_version()
print(f"Njuwan Farm ERP Version: {current_version}")

with app.app_context():
    db.create_all()

# ======================
# DASHBOARD
# ======================

"""@app.route("/")
def dashboard():
    total_milk = db.session.query(db.func.sum(MilkProduction.litres)).scalar() or 0
    total_income = db.session.query(db.func.sum(Transaction.amount)).filter_by(type="Income").scalar() or 0
    total_expense = db.session.query(db.func.sum(Transaction.amount)).filter_by(type="Expense").scalar() or 0

    cost_per_litre = round(total_expense / total_milk, 2) if total_milk > 0 else 0
    net_profit = total_income - total_expense

    return render_template(
        "dashboard.html",
        total_milk=total_milk,
        cost_per_litre=cost_per_litre,
        net_profit=net_profit
    )"""#Initial dashboard code, replaced by more detailed one below with cows count and feed cost

from datetime import date, timedelta
from sqlalchemy import func

import requests # Add this at the very top

def get_weather():
    # Use your actual API Key here
    api_key = "d8416cb9184ae71b2fa72f263607bd10"
    city = "Nyeri"
    # unit=metric gives us Celsius
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    
    try:
        response = requests.get(url, timeout=3) # Timeout prevents app from hanging
        data = response.json()
        if data.get("main"):
            return {
                "temp": round(data["main"]["temp"]),
                "desc": data["weather"][0]["description"].capitalize(),
                "icon": data["weather"][0]["icon"]
            }
    except Exception as e:
        print(f"Weather error: {e}")
    return None

@app.route('/')
def dashboard():
    # --- Your Existing Financial Logic ---
    cows_count = Cow.query.count()
    total_milk_all = db.session.query(func.sum(MilkProduction.litres)).scalar() or 0
    total_feed_cost = db.session.query(func.sum(Feed.cost)).scalar() or 0
    milk_price = 50
    revenue = total_milk_all * milk_price
    profit = revenue - total_feed_cost

    # --- New Logic: Calving Alerts (Next 7 Days) ---
    today = date.today()
    alert_limit = today + timedelta(days=7)
    alerts = Breeding.query.filter(
        Breeding.expected_calving.between(today, alert_limit)
    ).all()

    # --- New Logic: Per-Cow Production Summary ---
    # This joins cows with their specific milk records to get lifetime totals
    cows_with_totals = db.session.query(
        Cow, 
        func.sum(MilkProduction.litres).label('lifetime_milk')
    ).outerjoin(MilkProduction).group_by(Cow.id).all()

    return render_template(
        "dashboard.html",
        cows=cows_count,
        milk=total_milk_all,
        revenue=revenue,
        feed_cost=total_feed_cost,
        profit=profit,
        alerts=alerts,
        cows_with_totals=cows_with_totals,
        date=date # Required for the "Days to Calving" calculation in HTML
    )
# ADD COW
# ======================
from datetime import datetime, timedelta

@app.route('/add_cow', methods=['GET', 'POST'])
def add_cow():
    if request.method == 'POST':
        # 1. Handle Basic Cow Information
        raw_birth_date = request.form.get("birth_date")
        birth_date = None
        if raw_birth_date:
            try:
                birth_date = datetime.strptime(raw_birth_date, '%Y-%m-%d').date()
            except ValueError:
                birth_date = None

        new_cow = Cow(
            tag_number=request.form.get("tag_number"),
            name=request.form.get("name"),
            breed=request.form.get("breed"),
            status=request.form.get("status", "Active"),
            weight_kg=float(request.form.get("weight_kg") or 0),
            birth_date=birth_date
        )
        
        db.session.add(new_cow)
        db.session.flush()  # Use flush to get the new_cow.id for the linked records

        # 2. Add Vaccination Record (Same Line logic)
        v_type = request.form.get('vaccine')
        v_date_raw = request.form.get('vaccination_date')
        if v_type and v_date_raw:
            try:
                v_date = datetime.strptime(v_date_raw, '%Y-%m-%d').date()
                new_vac = Vaccination(
                    cow_id=new_cow.id, 
                    vaccine=v_type, 
                    due_date=v_date
                )
                db.session.add(new_vac)
            except ValueError:
                pass

        # 3. Add Breeding Record & Calculate Expectant Date
        ins_date_raw = request.form.get('insemination_date')
        if ins_date_raw:
            try:
                ins_date = datetime.strptime(ins_date_raw, '%Y-%m-%d').date()
                # Standard gestation for a cow is approximately 283 days
                calving_date = ins_date + timedelta(days=283)
                
                new_breeding = Breeding(
                    cow_id=new_cow.id,
                    insemination_date=ins_date,
                    bull=request.form.get('bull'),
                    expected_calving=calving_date,
                    pregnancy_status="Confirmed" # Sets status automatically upon entry
                )
                db.session.add(new_breeding)
            except ValueError:
                pass

        db.session.commit() # Save everything to the database
        return redirect(url_for('cow_profile_list'))
        
    return render_template('add_cow.html')

"""@app.route('/add_cow', methods=['GET', 'POST'])
def add_cow():
    if request.method == 'POST':
        # Prevent ValueError by checking if date exists before parsing
        raw_date = request.form.get("birth_date")
        birth_date = None
        if raw_date:
            try:
                birth_date = datetime.strptime(raw_date, '%Y-%m-%d').date()
            except ValueError:
                birth_date = None

        cow = Cow(
            tag_number=request.form.get("tag_number"),
            name=request.form.get("name"),
            breed=request.form.get("breed"),
            status=request.form.get("status", "Active"),
            weight_kg=float(request.form.get("weight_kg") or 0),
            birth_date=birth_date
        )
        
        db.session.add(cow)
        db.session.commit()
        
        
        return redirect('/')
    return render_template('add_cow.html')"""


# =================b=====
# ADD MILK RECORD
# ======================

@app.route('/add_milk', methods=['GET', 'POST'])
def add_milk():
    if request.method == 'POST':
        cow_id = request.form.get('cow_id')
        now = datetime.now()

        # 1. THE SAFETY CHECK (Withdrawal Logic)
        # Checks if cow is 'Under Treatment' OR within the 72h clearance window
        withdrawal_active = HealthRecord.query.filter(
            HealthRecord.cow_id == cow_id,
            (HealthRecord.status == 'Under Treatment') | (HealthRecord.clearance_date > now)
        ).first()

        if withdrawal_active:
            if withdrawal_active.status == 'Under Treatment':
                msg = "Safety Block: This cow is currently under active medical treatment."
            else:
                # Calculate remaining hours for the alert
                time_left = withdrawal_active.clearance_date - now
                hours = int(time_left.total_seconds() // 3600)
                msg = f"Safety Block: Milk withdrawal period active. {hours} hours remaining."
            
            flash(msg, "danger")
            return redirect(url_for('add_milk'))

        # 2. THE SAVE LOGIC (Original Code)
        try:
            milk = MilkProduction(
                cow_id=cow_id,
                litres=float(request.form.get("litres") or 0.0),
                session=request.form.get("session"), 
                date=datetime.now() # Using local time for Kenyan records
            )
            db.session.add(milk)
            db.session.commit()
            flash("Milk record saved successfully!", "success")
            return redirect('/')
        except Exception as e:
            db.session.rollback()
            flash(f"Error saving record: {str(e)}", "danger")
            return redirect(url_for('add_milk'))

    # GET logic: Only show records for cows NOT currently under withdrawal
    # We find IDs of cows under treatment first
    unsafe_cow_ids = [r.cow_id for r in HealthRecord.query.filter_by(status='Under Treatment').all()]
    
    # Then we fetch records, excluding those IDs
    recent_records = MilkProduction.query.filter(
        ~MilkProduction.cow_id.in_(unsafe_cow_ids)
    ).order_by(MilkProduction.date.desc()).limit(10).all()
    
    # GET Logic: 7-Day Matrix
    today = datetime.now().date()
    week_dates = [today - timedelta(days=i) for i in range(7)]
    
    # Fetch all records for the last 7 days
    records = MilkProduction.query.filter(MilkProduction.date >= (today - timedelta(days=7))).all()
    
    # matrix[cow_name][date][session] = litres
    matrix = defaultdict(lambda: defaultdict(lambda: defaultdict(float)))
    # daily_totals[date][session] = sum_of_all_cows
    daily_totals = defaultdict(lambda: defaultdict(float))
    
    for r in records:
        day = r.date.date()
        # Session mapping (AM, PM, EV)
        if r.session in ['Morning', 'AM']: col = 'AM'
        elif r.session in ['NOON', 'Lunch', 'PM']: col = 'PM'
        elif r.session in ['Evening', 'EV']: col = 'EV'
        else: col = 'PM'
        
        matrix[r.cow.name][day][col] += r.litres
        daily_totals[day][col] += r.litres # Add to the daily sum
    
    # Create a trends dictionary: trends[day] = 'up', 'down', or 'stable'
    trends = {}
    for i in range(len(week_dates) - 1):
        current_day = week_dates[i]
        previous_day = week_dates[i+1] # week_dates is [today, yesterday, ...]
        
        current_total = sum(daily_totals[current_day].values())
        previous_total = sum(daily_totals[previous_day].values())
        
        if current_total > previous_total:
            trends[current_day] = 'up'
        elif current_total < previous_total:
            trends[current_day] = 'down'
        else:
            trends[current_day] = 'stable'
    
    weather_data = get_weather()
    # Temporarily force fake data to test the UI
    # weather_data = {"temp": 24, "desc": "Sunny in Nyeri", "icon": "01d"}
    
    cows = Cow.query.all()
    return render_template('add_milk.html', 
                           cows=cows, 
                           matrix=matrix, 
                           week_dates=week_dates,
                           cow_names=sorted(matrix.keys()),
                           recent_records=recent_records,
                           daily_totals=daily_totals,
                           now=today,
                           trends=trends,
                           weather=weather_data)

@app.route('/delete_milk/<int:record_id>', methods=['POST'])
def delete_milk(record_id):
    record = MilkProduction.query.get_or_404(record_id)
    try:
        db.session.delete(record)
        db.session.commit()
        flash("Record deleted successfully.", "info")
    except Exception as e:
        db.session.rollback()
        flash(f"Error deleting record: {str(e)}", "danger")
    
    return redirect(url_for('add_milk'))

# ======================
# ADD TRANSACTION
# ======================

@app.route("/add_transaction", methods=["GET", "POST"])
def add_transaction():
    if request.method == "POST":
        t = Transaction(
            category=request.form["category"],
            amount=float(request.form["amount"]),
            type=request.form["type"]
        )
        db.session.add(t)
        db.session.commit()
        return redirect("/")
    return render_template("add_transaction.html")

@app.route("/progress")
def progress():
    state = load_state()
    return render_template("progress.html", state=state)

@app.route("/analytics")
def analytics_dashboard():
    months, milk_totals = monthly_milk_data()
    income, expense = revenue_vs_expense()
    cow_rank = cow_profitability()
    #crop_data = crop_roi_analysis()

    return render_template(
        "analytics.html",
        months=months,
        milk_totals=milk_totals,
        income=income,
        expense=expense,
        cow_rank=cow_rank,
        # crop_data=crop_data
    )

@app.route("/projection")
def projection_dashboard():
    data = three_year_projection()
    return render_template("projection.html", data=data)

@app.route("/feed-efficiency")
def feed_efficiency():
    data = feed_efficiency_model()
    return render_template("feed_efficiency.html", data=data)

@app.route("/cow_efficiency")
def cow_efficiency():
    data = cow_feed_efficiency()
    return render_template("cow_efficiency.html", data=data)

@app.route("/yoghurt")
def yoghurt_dashboard():
    data = yoghurt_profit_analysis()
    return render_template("yoghurt.html", data=data)

@app.route('/valuation')
def valuation():
    cows = Cow.query.all()
    total_value = 0
    valuation_details = []

    for cow in cows:
        # Basic valuation logic based on breed and status
        base_price = 120000 
        if cow.breed in ['Holstein', 'Ayrshire']:
            base_price += 30000
        
        if cow.status == 'Lactating':
            base_price += 30000
        elif cow.status == 'Quarantined' or cow.status == 'Sick':
            base_price -= 50000
        
        total_value += base_price
        valuation_details.append({
            'tag': cow.tag_number,
            'name': cow.name,
            'breed': cow.breed,   # Add this line
            'status': cow.status,
            'value': base_price
        })

    return render_template('valuation.html', 
                           total_value=total_value, 
                           details=valuation_details,
                           count=len(cows))

@app.route('/add_crop', methods=['GET', 'POST'])
def add_crop():
    if request.method == 'POST':
        # Your logic to save the crop to the database
        crop = Crop(
            id=request.form["tag"],
            name=request.form["crop"],
            acreage=float(request.form["acre"]),
            planting_date=datetime.strptime(request.form["planting_date"], "%Y-%m-%d")
        )
        db.session.add(crop)
        db.session.commit()
        return redirect("/")
    return render_template('add_crop.html')

@app.route('/add_feed', methods=['GET', 'POST'])
def add_feed_entry():  # Unique name to avoid AssertionError
    if request.method == 'POST':
        # Data cleaning and validation logic
        cow_id = request.form.get('cow_id')
        feed_type = request.form.get('feed_type')
        quantity = float(request.form.get('quantity'))
        cost = float(request.form.get('cost'))
        if cow_id:
            # Save to database (assumes you have a Feed model
            new_feed = Feed(cow_id=cow_id, f_type=feed_type, qty=quantity, cost=cost)
            db.session.add(new_feed)
            db.session.commit()
            return redirect('/')# Redirect to dashboard or feed list after adding     

    # Fetch all cows so you can pick them by name/tag in the UI
    all_cows = Cow.query.all()
    return render_template('add_feed.html', cows=all_cows)

@app.route("/api/kpis")
def api_kpis():
    total_milk = db.session.query(db.func.sum(MilkProduction.litres)).scalar() or 0
    total_income = db.session.query(db.func.sum(Transaction.amount)).filter_by(type="Income").scalar() or 0
    total_expense = db.session.query(db.func.sum(Transaction.amount)).filter_by(type="Expense").scalar() or 0
    
    return jsonify({
        "milk": total_milk,
        "income": total_income,
        "expense": total_expense
    })

# --- ROUTES ---

@app.route('/cow_profile', strict_slashes=False)
def cow_profile_list():
    # This matches the endpoint 'cow_profile_list' in your url_for
    cows = Cow.query.all()
    
    # Calculate Herd-Wide Stats
    total_incidents = HealthRecord.query.count()
    pending_vaccines = Vaccination.query.filter_by(status="Pending").count()
    upcoming_calvings = Breeding.query.filter(
        Breeding.expected_calving >= date.today()
    ).count()

    return render_template(
        'cow_profile.html', 
        cows=cows, 
        total_incidents=total_incidents,
        pending_vaccines=pending_vaccines,
        upcoming_calvings=upcoming_calvings,
        date=date
    )

@app.route('/view_profile/<int:cow_id>')
def view_profile(cow_id):
    # This matches the endpoint 'view_profile' that caused your BuildError
    cow = Cow.query.get_or_404(cow_id)
    # Since you don't have single_cow.html yet, we use cow_profile.html 
    # but pass only one cow in a list so the loop doesn't break
    return render_template('cow_profile.html', cows=[cow])

from datetime import datetime, date, timedelta

# Route for Health Records
@app.route('/add_health/<int:cow_id>', methods=['POST'])
def add_health(cow_id):
    disease = request.form.get('disease')
    treatment = request.form.get('treatment')
    vet = request.form.get('vet_name')
    
    new_health = HealthRecord(
        cow_id=cow_id, 
        disease=disease, 
        treatment=treatment, 
        vet_name=vet
    )
    db.session.add(new_health)
    db.session.commit()
    return redirect(url_for('dashboard'))

# Route for Vaccinations
@app.route('/add_vaccination/<int:cow_id>', methods=['POST'])
def add_vaccination(cow_id):
    vaccine = request.form.get('vaccine')
    due = datetime.strptime(request.form.get('due_date'), '%Y-%m-%d').date()
    
    new_vac = Vaccination(
        cow_id=cow_id, 
        vaccine=vaccine, 
        due_date=due, 
        status="Pending" # Default as per your model
    )
    db.session.add(new_vac)
    db.session.commit()
    return redirect(url_for('dashboard'))

# Route for Breeding (includes the 283-day calculation)
@app.route('/add_breeding/<int:cow_id>', methods=['POST'])
def add_breeding(cow_id):
    ins_date_str = request.form.get('insemination_date')
    ins_date = datetime.strptime(ins_date_str, '%Y-%m-%d').date()
    
    # Calculate expected calving (approx 283 days for cows)
    expected = ins_date + timedelta(days=283)
    
    new_breed = Breeding(
        cow_id=cow_id,
        insemination_date=ins_date,
        bull=request.form.get('bull'),
        expected_calving=expected,
        pregnancy_status="Confirmed" # Example status
    )
    db.session.add(new_breed)
    db.session.commit()
    return redirect(url_for('dashboard'))

@app.route('/toggle_vaccination/<int:vac_id>')
def toggle_vaccination(vac_id):
    vac = Vaccination.query.get_or_404(vac_id)
    # Flip the status
    vac.status = "Completed" if vac.status == "Pending" else "Pending"
    db.session.commit()
    return redirect(url_for('cow_profile_list'))

@app.route('/health_check')
# Logic to trigger alerts
def check_for_alerts():
    health_incidents = Cow.query.filter(Cow.status == 'Sick').count()
    if health_incidents > 5:
        send_system_alert(
            "Njuwan ERP: High Health Risk Alert",
            f"Alert: {health_incidents} cows are currently marked as Sick/Quarantined. Please check the Wellness Overview."
        )
def send_system_alert(subject, body):
    msg = Message(subject, 
                  sender='kelvinjua903@gmail.com', 
                  recipients=['ariallogistics@gmail.com'])
    msg.body = body
    mail.send(msg)
    # The fix for your TypeError
    if health_incidents > 5:
        send_system_alert(
            subject="Njuwan ERP: High Health Risk Alert",
            body=f"Attention: {health_incidents} cows are currently marked as Sick."
            )
        
    return render_template('health_check.html', status=health_status)
# You can call check_for_alerts() at the end of your dashboard route or set it up as a scheduled task.

@app.route('/health_check')  # Renamed to match your browser
def health_check():
    health_status = {
        "database": "Offline",
        "cow_count": 0,
        "pdf_engine": "Ready",
        "last_backup": "None Found"
    }
    
    try:
        # Check DB connection for your 30 cows
        health_status["cow_count"] = Cow.query.count()
        health_status["database"] = "Online"
        
        # TRIGGER ALERT: Pass the 2 required arguments to fix TypeError
        if health_status["cow_count"] > 0: 
             send_system_alert("System Check", "Database is active and healthy.")
    except Exception as e:
        health_status["database"] = f"Error: {str(e)}"

    # Check for latest backup file
    backup_dir = os.path.join(app.root_path, 'backups')
    if os.path.exists(backup_dir):
        files = glob.glob(os.path.join(backup_dir, '*.db'))
        if files:
            latest_file = max(files, key=os.path.getctime)
            health_status["last_backup"] = os.path.basename(latest_file)

    return render_template('health_check.html', status=health_status)

# --- FIX 1: Consolidated Calving Logic ---
@app.route('/confirm_calving/<int:breeding_id>', methods=['POST'])
def confirm_calving(breeding_id):
    breeding_record = Breeding.query.get_or_404(breeding_id)
    mother = Cow.query.get(breeding_record.cow_id)
    
    # Update Mother
    mother.status = 'Lactating'
    
    # Create Calf
    new_tag = f"C-{mother.name.upper()}-{datetime.now().strftime('%y%m%d')}"
    new_calf = Cow(
        tag_number=new_tag,
        name=request.form.get("calf_name") or f"Calf of {mother.name}",
        breed=mother.breed,
        status='Young',
        weight_kg=float(request.form.get("calf_weight") or 0.0)
    )
    db.session.add(new_calf)
    
    # Inventory Auto-Deduct
    deduct_inventory("Iodine", 0.05)
    if request.form.get("hand_raised"):
        deduct_inventory("Milk Replacer", 2.0)
    
    db.session.delete(breeding_record) 
    db.session.commit()
    flash(f"Success! {new_calf.name} recorded and inventory updated.", "success")
    return redirect(url_for('dashboard'))

if __name__ == "__main__":
    
    with app.app_context():
        db.create_all() # Ensures tables exist
    app.run(debug=True)