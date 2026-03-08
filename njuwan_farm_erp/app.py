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
from flask import Flask, render_template, request, redirect, url_for
from config import Config
from database import db
from datetime import datetime, timedelta
from datetime import date
from models import MilkProduction, Transaction, Cow, Vaccination, Breeding, Crop, Feed, HealthRecord
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

app = Flask(__name__)
app.config.from_object(Config)

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
        milk = MilkProduction(
            cow_id=request.form.get("cow_id"),
            litres=float(request.form.get("litres")),
            session=request.form.get("session"), # AM/PM
            date=datetime.utcnow()
        )
        db.session.add(milk)
        db.session.commit()
        return redirect('/')
    
    cows = Cow.query.all()
    return render_template('add_milk.html', cows=cows)


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

if __name__ == "__main__":
    with app.app_context():
        db.create_all() # Ensures tables exist
    app.run(debug=True)